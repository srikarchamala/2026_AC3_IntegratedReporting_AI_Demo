"""Fail-closed retrieval and source preservation tests, using fake transport."""
import hashlib
import io
import json
import tempfile
import unittest
import urllib.request
from email.message import Message
from pathlib import Path
from unittest.mock import patch

from workflow import retrieval


ARTICLE = b'''<?xml version="1.0"?>
<article><front><article-meta>
<article-id pub-id-type="doi">10.1000/ac3-demo</article-id>
<article-id pub-id-type="pmid">17</article-id>
<article-id pub-id-type="pmcid">PMC17</article-id>
<title-group><article-title>Example original article</article-title></title-group>
</article-meta></front><body>
<sec id="aml"><title>Selected complete section</title>
<p>A source statement retains its explicit qualification.</p>
<table-wrap id="t1"><label>Table 1.</label><caption><p>Evidence table</p></caption>
<table><tbody><tr><th>Item</th><th>Result</th></tr>
<tr><td>Test A<xref ref-type="table-fn" rid="f1">a</xref></td><td>Reported</td></tr></tbody></table>
<table-wrap-foot><fn id="f1"><label>a</label><p>This footnote contains an exception that must be retained.</p></fn></table-wrap-foot>
</table-wrap><sec><title>Additional context</title><p>Missing information remains unknown.</p></sec>
</sec></body></article>'''


def sample_source():
    return {
        "source_id": "WHO5E_MYEOID_2022", "default": True,
        "title": "Example original article", "framework": "Test framework",
        "edition": "Test edition", "publication_year": 2022,
        "source_kind": "public_author_overview", "scope": "Test source scope",
        "canonical_url": "https://doi.org/10.1000/ac3-demo",
        "identity": {"doi": "10.1000/ac3-demo", "pmid": "17", "pmcid": "PMC17"},
        "allowed_hosts": ["public.example.org"],
        "retrieval_urls": ["https://public.example.org/article.xml"],
        "sections": [{"id": "TEST-SECTION", "title": "Selected complete section",
                      "end_title": "Next section", "min_chars": 100,
                      "required_text": ["Table 1"]}],
        "tables": [],
    }


class FakeResponse(io.BytesIO):
    def __init__(self, body, content_type="application/xml", url="https://public.example.org/article.xml"):
        super().__init__(body)
        self.status = 200
        self.headers = Message()
        self.headers["Content-Type"] = content_type
        self.headers["Content-Length"] = str(len(body))
        self.url = url

    def geturl(self):
        return self.url


class FakeOpener:
    def __init__(self, body, media_type="application/xml", final_url="https://public.example.org/article.xml"):
        self.body, self.media_type, self.final_url = body, media_type, final_url

    def open(self, request, timeout):
        return FakeResponse(self.body, self.media_type, self.final_url)


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.manifest = self.root / "sources.json"
        self.manifest.write_text(json.dumps({"sources": [sample_source()]}))
        self.manifest_patch = patch.object(retrieval, "MANIFEST_PATH", self.manifest)
        self.manifest_patch.start()

    def tearDown(self):
        self.manifest_patch.stop()
        self.temp.cleanup()

    def fetch(self, data, media_type="application/xml", final_url="https://public.example.org/article.xml"):
        return patch.object(retrieval.urllib.request, "build_opener",
                            return_value=FakeOpener(data, media_type, final_url))

    def test_complete_section_preserves_table_cells_footnotes_and_provenance(self):
        with self.fetch(ARTICLE):
            snapshots = retrieval.retrieve_sources(self.root / "run")
        snapshot = snapshots[0]
        text = snapshot["passages"][0]["text"]
        self.assertIn("Item | Result", text)
        self.assertIn("Test Aa | Reported", text)
        self.assertIn("This footnote contains an exception that must be retained.", text)
        self.assertIn("Missing information remains unknown.", text)
        self.assertEqual(snapshot["sha256"], hashlib.sha256(ARTICLE).hexdigest())
        self.assertEqual(snapshot["acquisition_method"], "public_https")
        self.assertTrue(snapshot["retrieved_at"].endswith("+00:00"))
        self.assertEqual((self.root / "run" / snapshot["raw_file"]).read_bytes(), ARTICLE)

    def test_table_outside_section_is_included_with_footnotes(self):
        external = ARTICLE.replace(b'<table-wrap id="t1">', b'<xref ref-type="table" rid="t1">Table 1</xref></sec><table-wrap id="t1">')
        external = external.replace(b'</table-wrap><sec><title>Additional context</title>', b'</table-wrap><sec><title>Additional context</title>')
        external = external.replace(b'</p></sec>\n</sec></body>', b'</p></sec>\n</body>')
        passages, _ = retrieval._parse_xml(external, sample_source())
        self.assertIn("This footnote contains an exception", passages[0]["text"])

    def test_subscription_wall_cannot_be_saved_as_a_reference(self):
        wall = b'<html><head><title>Subscription required</title></head><body><h1>Subscription required</h1><p>Sign in to access this article</p></body></html>'
        with self.fetch(wall, "text/html"):
            with self.assertRaisesRegex(retrieval.RetrievalError, "access wall"):
                retrieval.retrieve_sources(self.root / "wall")
        self.assertEqual(list((self.root / "wall" / "references").glob("*.snapshot.json")), [])

    def test_browser_challenge_is_rejected(self):
        challenge = b'<html><h1>Checking your browser</h1><p>reCAPTCHA</p></html>'
        with self.fetch(challenge, "text/html"):
            with self.assertRaisesRegex(retrieval.RetrievalError, "browser challenge"):
                retrieval.retrieve_sources(self.root / "challenge")

    def test_incorrect_original_article_is_rejected(self):
        for data in (ARTICLE.replace(b"10.1000/ac3-demo", b"10.1000/different"),
                     ARTICLE.replace(b"Example original article", b"A different article"),
                     ARTICLE.replace(b"PMC17", b"PMC99")):
            with self.subTest(data=data[:100]):
                with self.fetch(data):
                    with self.assertRaisesRegex(retrieval.RetrievalError, "does not match"):
                        retrieval.retrieve_sources(self.root / "incorrect")

    def test_redirect_to_unapproved_host_or_scheme_is_rejected(self):
        redirect = retrieval._AllowedRedirects(["public.example.org"])
        request = urllib.request.Request("https://public.example.org/article.xml")
        for target in ("https://unapproved.example/article.xml", "http://public.example.org/article.xml",
                       "https://user:password@public.example.org/article.xml",
                       "https://public.example.org:444/article.xml"):
            with self.subTest(target=target):
                with self.assertRaisesRegex(retrieval.RetrievalError, "approved HTTPS"):
                    redirect.redirect_request(request, None, 302, "Found", {}, target)
        with self.fetch(ARTICLE, final_url="https://unapproved.example/article.xml"):
            with self.assertRaisesRegex(retrieval.RetrievalError, "approved HTTPS"):
                retrieval.retrieve_sources(self.root / "redirect")

    def test_missing_required_section_fails_closed(self):
        missing = ARTICLE.replace(b"Selected complete section", b"Unrelated section")
        with self.fetch(missing):
            with self.assertRaisesRegex(retrieval.RetrievalError, "section not uniquely found"):
                retrieval.retrieve_sources(self.root / "missing-section")

    def test_missing_required_source_fails_without_snapshot(self):
        with patch.object(retrieval, "_fetch_url", side_effect=retrieval.RetrievalError("offline")):
            with self.assertRaisesRegex(retrieval.RetrievalError, "no model-memory fallback"):
                retrieval.retrieve_sources(self.root / "offline")

    def test_optional_risk_is_not_fetched_until_enabled_and_then_is_required(self):
        risk = sample_source()
        risk.update({"source_id": "ELN2022_AML_RISK", "default": False})
        self.manifest.write_text(json.dumps({"sources": [sample_source(), risk]}))
        with patch.object(retrieval, "_fetch_url", return_value=(ARTICLE, "application/xml", "https://public.example.org/article.xml")) as fetch:
            snapshots = retrieval.retrieve_sources(self.root / "default-only")
        self.assertEqual(len(snapshots), 1)
        self.assertEqual(fetch.call_count, 1)
        with patch.object(retrieval, "_fetch_url", side_effect=[
                (ARTICLE, "application/xml", "https://public.example.org/article.xml"),
                retrieval.RetrievalError("risk reference unavailable")]):
            with self.assertRaisesRegex(retrieval.RetrievalError, "ELN2022_AML_RISK unavailable"):
                retrieval.retrieve_sources(self.root / "risk-missing", include_risk=True)

    def test_local_original_retains_identity_and_does_not_fetch(self):
        path = self.root / "original.xml"
        path.write_bytes(ARTICLE)
        with patch.object(retrieval, "_fetch_url", side_effect=AssertionError("must not fetch")):
            snapshot = retrieval.retrieve_sources(self.root / "local", local_sources={"who": path})[0]
        self.assertEqual(snapshot["acquisition_method"], "local_import")
        self.assertIsNone(snapshot["retrieved_url"])
        self.assertEqual(snapshot["local_source_name"], "original.xml")

    def test_local_import_does_not_bypass_identity_checks(self):
        path = self.root / "wrong.xml"
        path.write_bytes(ARTICLE.replace(b"10.1000/ac3-demo", b"10.1000/different"))
        with self.assertRaisesRegex(retrieval.RetrievalError, "DOI does not match"):
            retrieval.retrieve_sources(self.root / "local-wrong", local_sources={"WHO": path})

    def test_missing_local_file_is_a_clean_retrieval_error(self):
        with self.assertRaisesRegex(retrieval.RetrievalError, "missing"):
            retrieval.retrieve_sources(self.root / "local-missing", local_sources={"WHO": self.root / "missing.xml"})

    def test_dtd_entity_expansion_is_rejected(self):
        data = ARTICLE.replace(b'<article>', b'<!DOCTYPE article [<!ENTITY bad "expanded">]><article>')
        with self.assertRaisesRegex(retrieval.RetrievalError, "entity declarations"):
            retrieval._parse_xml(data, sample_source())

    def test_oversized_transport_is_rejected_before_parsing(self):
        with self.fetch(ARTICLE), patch.object(retrieval, "MAX_BYTES", 32):
            with self.assertRaisesRegex(retrieval.RetrievalError, "size limit"):
                retrieval.retrieve_sources(self.root / "oversized")

    def test_html_preserves_complete_section_and_table_footnote(self):
        html = b'''<html><head><meta name="citation_title" content="Example original article">
        <meta name="citation_doi" content="10.1000/ac3-demo"></head><body>
        <nav>irrelevant navigation</nav><article><h1>Example original article</h1>
        <section><h2>Selected complete section</h2><p>A source statement retains its explicit qualification.</p>
        <section><h3>Table 1. Evidence table</h3><table><tr><th>Item</th><th>Result</th></tr>
        <tr><td>Test A</td><td>Reported</td></tr></table>
        <p>Footnote: this exception must remain available to the classifier.</p></section>
        </section></article></body></html>'''
        passages, _ = retrieval._parse_html(html, sample_source())
        self.assertIn("Test A | Reported", passages[0]["text"])
        self.assertIn("this exception must remain", passages[0]["text"])
        self.assertNotIn("irrelevant navigation", passages[0]["text"])


if __name__ == "__main__":
    unittest.main()
