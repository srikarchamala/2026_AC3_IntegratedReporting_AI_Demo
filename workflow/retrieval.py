"""Fetch and verify approved public original articles, without model fallback.

The manifest identifies sources and section boundaries, not diagnostic rules.
Snapshots preserve complete source sections and table footnotes. HTML access
walls, wrong articles, incomplete sections, and unexpected redirects fail closed.
Only a PDF input requires the optional pypdf package.
"""
from __future__ import annotations

import hashlib
import http.client
import io
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

from .common import WorkflowError


MAX_BYTES = 16 * 1024 * 1024
FETCH_TIMEOUT = 20
MANIFEST_PATH = Path(__file__).with_name("sources.json")


class RetrievalError(WorkflowError):
    """A required authoritative source could not be safely read and verified."""


def _normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).split())


def _key(text: str) -> str:
    return "".join(c for c in _normalize(text).casefold() if c.isalnum())


def _tag(node: ET.Element) -> str:
    return node.tag.rsplit("}", 1)[-1].lower() if isinstance(node.tag, str) else ""


def _plain(node: ET.Element) -> str:
    return _normalize("".join(node.itertext()))


def _check_url(url: str, allowed_hosts: list[str]) -> None:
    try:
        parsed = urllib.parse.urlsplit(url)
        port = parsed.port
    except ValueError as exc:
        raise RetrievalError("Invalid source URL") from exc
    if (parsed.scheme != "https" or parsed.username or parsed.password
            or parsed.hostname not in allowed_hosts or port not in (None, 443)):
        raise RetrievalError("Source URL or redirect is outside the approved HTTPS hosts")


class _AllowedRedirects(urllib.request.HTTPRedirectHandler):
    max_redirections = 3
    max_repeats = 2

    def __init__(self, allowed_hosts: list[str]):
        super().__init__()
        self.allowed_hosts = allowed_hosts

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _check_url(newurl, self.allowed_hosts)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _fetch_url(url: str, allowed_hosts: list[str]) -> tuple[bytes, str, str]:
    """Bounded HTTPS fetch; never follows a redirect outside this source's list."""
    _check_url(url, allowed_hosts)
    opener = urllib.request.build_opener(_AllowedRedirects(allowed_hosts))
    request = urllib.request.Request(url, headers={
        "User-Agent": "AC3-Synthetic-Teaching-Workflow/1.0",
        "Accept": "application/xml,text/html,application/pdf;q=0.9,*/*;q=0.1",
        "Accept-Encoding": "identity",
    })
    deadline = time.monotonic() + FETCH_TIMEOUT
    try:
        with opener.open(request, timeout=FETCH_TIMEOUT) as response:
            final_url = response.geturl()
            _check_url(final_url, allowed_hosts)
            if not 200 <= response.status < 300:
                raise RetrievalError(f"Source returned HTTP {response.status}")
            declared_size = response.headers.get("Content-Length")
            if declared_size and int(declared_size) > MAX_BYTES:
                raise RetrievalError("Source exceeds the download size limit")
            reader = getattr(response, "read1", response.read)
            chunks, size = [], 0
            while True:
                if time.monotonic() > deadline:
                    raise RetrievalError("Source retrieval exceeded the time limit")
                chunk = reader(min(65536, MAX_BYTES + 1 - size))
                if not chunk:
                    break
                chunks.append(chunk)
                size += len(chunk)
                if size > MAX_BYTES:
                    raise RetrievalError("Source exceeds the download size limit")
            if not size:
                raise RetrievalError("Source returned no content")
            return b"".join(chunks), response.headers.get_content_type(), final_url
    except RetrievalError:
        raise
    except (OSError, ValueError, urllib.error.URLError, http.client.HTTPException) as exc:
        # URLs are manifest-controlled; never include response bodies or credentials.
        raise RetrievalError(f"Public source fetch failed: {type(exc).__name__}") from exc


_BLOCKS = {"sec", "section", "title", "h1", "h2", "h3", "h4", "h5", "h6",
           "p", "div", "list", "list-item", "ul", "ol", "li", "caption", "label",
           "table-wrap", "table-wrap-foot", "fn", "fn-group", "fig", "blockquote"}
_SKIP_HTML = {"script", "style", "nav", "footer", "noscript", "form", "svg"}


def _render(node: ET.Element, html: bool = False) -> str:
    """Render source text with paragraph, table-cell, and footnote boundaries."""
    tag = _tag(node)
    if html and tag in _SKIP_HTML:
        return ""
    if tag == "table":
        rows = []
        for row in node.iter():
            if _tag(row) == "tr":
                cells = [_normalize(_render(cell, html)) for cell in row
                         if _tag(cell) in {"th", "td"}]
                if cells:
                    rows.append(" | ".join(cells))
        return "\n" + "\n".join(rows) + "\n"
    if tag == "br":
        return "\n"
    text = node.text or ""
    for child in node:
        text += _render(child, html) + (child.tail or "")
    return "\n" + text + "\n" if tag in _BLOCKS else text


def _clean_rendered(text: str) -> str:
    return "\n".join(line for line in (_normalize(t) for t in text.splitlines()) if line)


def _wall_check(text: str) -> None:
    head = _normalize(text[:8000]).casefold()
    markers = ("checking your browser", "verify you are human", "access denied",
               "subscription required", "sign in to access this article",
               "purchase access to this article", "enable javascript and cookies",
               "just a moment...", "recaptcha")
    if any(marker in head for marker in markers):
        raise RetrievalError("Source returned an access wall or browser challenge")


def _verify_identity(source: dict, title: str, identifiers: dict, text: str) -> dict:
    if _key(source["title"]) != _key(title):
        raise RetrievalError("Article title does not match the approved source")
    expected = source["identity"]
    doi = identifiers.get("doi", "").lower().removeprefix("https://doi.org/")
    if doi:
        if doi != expected["doi"].lower():
            raise RetrievalError("Article DOI does not match the approved source")
    elif expected["doi"].lower() not in _normalize(text).lower():
        raise RetrievalError("Cannot verify the approved article DOI")
    for name in ("pmid", "pmcid"):
        if name in expected and identifiers.get(name):
            if identifiers[name].upper() != expected[name].upper():
                raise RetrievalError(f"Article {name.upper()} does not match the approved source")
    return {"doi": expected["doi"], "title": source["title"],
            "verification": "matching article title and DOI",
            "observed_identifiers": identifiers}


def _passage(spec: dict, text: str, **metadata) -> dict:
    text = _clean_rendered(text)
    if len(text) < spec.get("min_chars", 1):
        raise RetrievalError(f"Required section is missing or incomplete: {spec['title']}")
    for required in spec.get("required_text", []):
        if _key(required) not in _key(text):
            raise RetrievalError(f"Required table or context is missing in: {spec['title']}")
    return {"id": spec["id"], "section": spec["title"], "text": text,
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), **metadata}


def _parse_xml(data: bytes, source: dict) -> tuple[list[dict], dict]:
    # ElementTree does not fetch external DTDs. Reject internal entity declarations.
    if re.search(br"<!ENTITY\b", data, re.I):
        raise RetrievalError("Article XML contains unsupported entity declarations")
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise RetrievalError("Source is not readable article XML") from exc
    meta = next((n for n in root.iter() if _tag(n) == "article-meta"), None)
    if meta is None:
        raise RetrievalError("Source XML is not an identifiable original article")
    title_node = next((n for n in meta.iter() if _tag(n) == "article-title"), None)
    if title_node is None:
        raise RetrievalError("Article title is missing")
    identifiers = {n.attrib.get("pub-id-type", ""): _plain(n)
                   for n in meta if _tag(n) == "article-id"}
    identity = _verify_identity(source, _plain(title_node), identifiers, _plain(meta))
    passages = []
    for spec in source["sections"]:
        matches = [n for n in root.iter() if _tag(n) == "sec"
                   and any(_tag(c) == "title" and _key(_plain(c)) == _key(spec["title"])
                           for c in n)]
        if len(matches) != 1:
            raise RetrievalError(f"Required article section not uniquely found: {spec['title']}")
        section = matches[0]
        text = _render(section)
        # Some JATS layouts place tables outside the section that references them.
        included = {id(n) for n in section.iter()}
        table_ids = {rid for n in section.iter() if _tag(n) == "xref"
                     and n.attrib.get("ref-type") == "table"
                     for rid in n.attrib.get("rid", "").split()}
        for table in root.iter():
            if (_tag(table) == "table-wrap" and table.get("id") in table_ids
                    and id(table) not in included):
                text += _render(table)
        passages.append(_passage(spec, text, original_section_id=section.get("id")))
    for spec in source.get("tables", []):
        matches = [n for n in root.iter() if _tag(n) == "table-wrap"
                   and any(_tag(c) == "label" and _key(_plain(c)) == _key(spec["label"])
                           for c in n)]
        if len(matches) != 1:
            raise RetrievalError(f"Required table not uniquely found: {spec['label']}")
        passages.append(_passage(spec, _render(matches[0])))
    return passages, identity


class _HTMLTree(HTMLParser):
    _VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = ET.Element("document")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = ET.SubElement(self.stack[-1], tag, dict((k, v or "") for k, v in attrs))
        if tag not in self._VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self._VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        parent = self.stack[-1]
        if len(parent):
            parent[-1].tail = (parent[-1].tail or "") + data
        else:
            parent.text = (parent.text or "") + data


def _parse_html(data: bytes, source: dict) -> tuple[list[dict], dict]:
    parser = _HTMLTree()
    try:
        parser.feed(data.decode("utf-8"))
        parser.close()
    except (UnicodeError, ValueError) as exc:
        raise RetrievalError("Source HTML is unreadable") from exc
    root = parser.root
    visible = _clean_rendered(_render(root, html=True))
    _wall_check(visible)
    metadata = {n.get("name", n.get("property", "")).lower(): n.get("content", "")
                for n in root.iter("meta")}
    title = metadata.get("citation_title") or next((_plain(n) for n in root.iter("h1")), "")
    identifiers = {"doi": metadata.get("citation_doi", ""),
                   "pmid": metadata.get("citation_pmid", "")}
    identity = _verify_identity(source, title, identifiers, visible)
    parents = {child: parent for parent in root.iter() for child in parent}
    passages = []
    for spec in source["sections"]:
        matches = [n for n in root.iter() if _tag(n) in {"h2", "h3", "h4"}
                   and _key(_plain(n)) == _key(spec["title"])]
        selected = None
        for heading in matches:
            parent = parents.get(heading)
            while parent is not None and _tag(parent) not in {"section", "article", "body", "document"}:
                parent = parents.get(parent)
            if parent is not None and _tag(parent) == "section":
                selected = parent
                break
        if selected is None:
            raise RetrievalError(f"Cannot identify a complete HTML section: {spec['title']}")
        passages.append(_passage(spec, _render(selected, html=True)))
    for spec in source.get("tables", []):
        matches = [n for n in root.iter() if _tag(n) == "section"
                   and any(_tag(h) in {"h2", "h3", "h4"}
                           and _key(spec["label"]) in _key(_plain(h))
                           and _key(spec["title"]) in _key(_plain(h)) for h in n.iter())]
        if not matches:
            raise RetrievalError(f"Cannot identify complete HTML table and footnotes: {spec['label']}")
        selected = min(matches, key=lambda n: len(_plain(n)))
        passages.append(_passage(spec, _render(selected, html=True)))
    return passages, identity


def _heading_pattern(title: str) -> re.Pattern:
    words = re.split(r"\s+", title.strip())
    return re.compile(r"(?im)^\s*" + r"\s+".join(re.escape(w) for w in words) + r"\s*$")


def _parse_pdf(data: bytes, source: dict) -> tuple[list[dict], dict]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RetrievalError("PDF source requires pypdf; install the workflow dependencies") from exc
    try:
        reader = PdfReader(io.BytesIO(data), strict=False)
        if reader.is_encrypted:
            raise RetrievalError("Encrypted source PDFs are not supported")
        if len(reader.pages) > 100:
            raise RetrievalError("Source PDF exceeds the page limit")
        pages = [p.extract_text() or "" for p in reader.pages]
    except RetrievalError:
        raise
    except Exception as exc:
        raise RetrievalError("Source PDF cannot be read") from exc
    full_text = "\n".join(pages)
    if _key(source["title"]) not in _key("\n".join(pages[:2])):
        raise RetrievalError("PDF opening pages do not match the approved article title")
    metadata = str(reader.metadata or "")
    identity = _verify_identity(source, source["title"], {}, full_text + "\n" + metadata)
    passages = []
    for spec in source["sections"]:
        starts = [i for i, text in enumerate(pages) if _heading_pattern(spec["title"]).search(text)]
        if not starts:
            raise RetrievalError(f"Required PDF section missing: {spec['title']}")
        start = starts[0]
        ends = [i for i in range(start, len(pages))
                if _heading_pattern(spec["end_title"]).search(pages[i])]
        if not ends:
            raise RetrievalError(f"Cannot establish complete PDF section boundary: {spec['title']}")
        end = ends[0]
        # Complete pages preserve table continuations, columns, and footnotes.
        text = "\n".join(pages[start:end + 1])
        passages.append(_passage(spec, text, pdf_pages=list(range(start + 1, end + 2)),
                                 extraction_scope="complete pages including section and boundary context"))
    for spec in source.get("tables", []):
        matches = [i for i, text in enumerate(pages)
                   if _key(spec["label"] + " " + spec["title"]) in _key(text)]
        if not matches:
            raise RetrievalError(f"Required PDF table missing: {spec['label']}")
        idx = matches[0]
        # This source's table is self-contained on a page. Required footnote
        # anchors fail closed if a different rendering truncates the table.
        passages.append(_passage(spec, pages[idx], pdf_pages=[idx + 1],
                                 extraction_scope="complete table page including all footnotes and surrounding context"))
    return passages, identity


def _parse_document(data: bytes, media_type: str, source: dict) -> tuple[list[dict], dict, str]:
    if not data or len(data) > MAX_BYTES:
        raise RetrievalError("Source is empty or exceeds the size limit")
    head = data[:2048].lstrip()
    if head.startswith(b"%PDF-"):
        passages, identity = _parse_pdf(data, source)
        return passages, identity, "pdf"
    if "pdf" in media_type.lower():
        raise RetrievalError("Expected PDF source did not contain a PDF document")
    if ("xml" in media_type.lower() or head.startswith(b"<?xml")
            or re.search(br"<!DOCTYPE\s+article\b", head, re.I)
            or head.startswith(b"<article ")):
        passages, identity = _parse_xml(data, source)
        return passages, identity, "xml"
    passages, identity = _parse_html(data, source)
    return passages, identity, "html"


def retrieve_sources(out_dir: Path, include_risk: bool = False,
                     local_sources: dict[str, Path] | None = None) -> list[dict]:
    """Retrieve required snapshots into ``out_dir/references`` or raise.

    Local originals can be supplied by manifest source ID or aliases WHO/ELN.
    Local sources undergo the same identity/section checks; their retrieved_url
    is null and acquisition_method is local_import. No browser session or
    subscriber credentials are used. Partial successful snapshots may remain
    after a later source fails; the caller must not proceed on RetrievalError.
    """
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise RetrievalError("Approved source manifest cannot be read") from exc
    selected = [s for s in manifest["sources"] if s["default"] or include_risk]
    aliases = {"WHO": "WHO5E_MYEOID_2022", "ELN": "ELN2022_AML_RISK"}
    local = {aliases.get(key.upper(), key): Path(path) for key, path in (local_sources or {}).items()}
    selected_ids = {s["source_id"] for s in selected}
    if set(local) - selected_ids:
        raise RetrievalError("Local source ID is unknown or its optional framework is not enabled")
    reference_dir = Path(out_dir) / "references"
    reference_dir.mkdir(parents=True, exist_ok=True)
    snapshots = []
    for source in selected:
        source_id = source["source_id"]
        attempts = []
        acquisition_method = "local_import" if source_id in local else "public_https"
        retrieved_url = None
        if source_id in local:
            path = local[source_id]
            try:
                if path.suffix.lower() not in {".xml", ".html", ".htm", ".pdf"}:
                    raise RetrievalError("Local originals must be XML, HTML, or PDF files")
                if not path.is_file() or path.stat().st_size > MAX_BYTES:
                    raise RetrievalError(f"Local original is missing or too large: {path.name}")
                data = path.read_bytes()
                media_type = {".xml": "application/xml", ".pdf": "application/pdf"}.get(path.suffix.lower(), "text/html")
                passages, identity, kind = _parse_document(data, media_type, source)
            except OSError as exc:
                raise RetrievalError(f"Cannot read local original for {source_id}") from exc
        else:
            for url in source["retrieval_urls"]:
                try:
                    data, media_type, retrieved_url = _fetch_url(url, source["allowed_hosts"])
                    passages, identity, kind = _parse_document(data, media_type, source)
                    break
                except RetrievalError as exc:
                    attempts.append({"url": url, "error": str(exc)})
            else:
                reasons = "; ".join(a["error"] for a in attempts)
                raise RetrievalError(f"Required source {source_id} unavailable: {reasons}. Supply a readable original article; no model-memory fallback is allowed.")
        digest = hashlib.sha256(data).hexdigest()
        raw_name = f"{source_id}.{digest[:12]}.{kind}"
        raw_path = reference_dir / raw_name
        raw_path.write_bytes(data)
        snapshot = {key: source[key] for key in ("source_id", "title", "framework", "edition",
                    "publication_year", "source_kind", "scope", "canonical_url")}
        snapshot.update({"retrieved_url": retrieved_url,
                         "retrieved_at": datetime.now(timezone.utc).isoformat(),
                         "sha256": digest, "raw_file": f"references/{raw_name}",
                         "acquisition_method": acquisition_method, "article_identity": identity,
                         "parser": f"stdlib_{kind}" if kind != "pdf" else "pypdf",
                         "retrieval_attempts": attempts, "passages": passages})
        if source_id in local:
            snapshot["local_source_name"] = local[source_id].name
        snapshot_path = reference_dir / f"{source_id}.snapshot.json"
        snapshot_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        snapshots.append(snapshot)
    return snapshots
