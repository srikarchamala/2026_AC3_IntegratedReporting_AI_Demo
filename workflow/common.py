"""File handling and exact source preservation, independent of any model."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parent
INPUT_FILES = {
    "MORPH": "01_bone_marrow_morphology.pdf",
    "FLOW": "02_flow_cytometry.pdf",
    "CYTO": "03_cytogenetics_fish.pdf",
    "MOLEC": "04_molecular_ngs.pdf",
}
SECTION_IDS = [
    "patient_specimen", "component_studies", "clinical_context", "morphology",
    "flow", "cytogenetics", "molecular", "interpretation", "diagnosis",
    "prognostic_predictive", "limitations",
]


class WorkflowError(Exception):
    """An actionable failure which must not be silently repaired by a model."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize(text: object) -> str:
    """Whitespace and Unicode normalization only; do not erase negation or units."""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(text))).strip()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def new_directory(path: Path) -> Path:
    path = path.resolve()
    if path.exists():
        raise WorkflowError(f"Output directory already exists: {path}. Choose a new directory.")
    path.mkdir(parents=True)
    return path


def extract_documents(case_dir: Path, out_dir: Path) -> dict:
    """Read only the four explicit component files, never the guide or answer key."""
    from pypdf import PdfReader

    documents = {}
    for source_id, name in INPUT_FILES.items():
        path = case_dir / name
        if not path.is_file():
            raise WorkflowError(f"Missing component report: {path}")
        raw = path.read_bytes()
        if len(raw) > 20 * 1024 * 1024:
            raise WorkflowError(f"Component report exceeds the 20 MiB demo limit: {name}")
        try:
            reader = PdfReader(path)
            if reader.is_encrypted:
                raise WorkflowError(f"Encrypted PDF cannot be read: {name}")
            pages = [{"page": i + 1, "text": page.extract_text() or ""}
                     for i, page in enumerate(reader.pages)]
        except WorkflowError:
            raise
        except Exception as exc:
            raise WorkflowError(f"Cannot extract PDF text from {name}: {type(exc).__name__}") from exc
        if not pages or any(not normalize(page["text"]) for page in pages):
            raise WorkflowError(f"Unreadable/empty page in {name}. Supply a text-readable PDF; no OCR is assumed.")
        document = {"source_id": source_id, "document_name": name,
                    "sha256": digest(raw), "pages": pages}
        documents[source_id] = document
        write_json(out_dir / "inputs" / f"{source_id}.json", document)
    return documents


def prompt(name: str) -> str:
    return (PACKAGE / "prompts" / name).read_text(encoding="utf-8")


def schema(name: str) -> dict:
    return read_json(PACKAGE / "schemas" / name)


def json_from_model(text: str) -> dict:
    text = text.strip()
    # Accept a single, otherwise well-formed fenced JSON object; never fish an
    # arbitrary object out of a narrative or silently repair truncated output.
    if text.startswith("```") and text.endswith("```"):
        lines = text.splitlines()
        if lines[0].strip().lower() not in {"```json", "```"}:
            raise WorkflowError("Model returned an unexpected fenced format.")
        text = "\n".join(lines[1:-1])
    try:
        result = json.loads(text)
    except json.JSONDecodeError as exc:
        raise WorkflowError("Model output is not complete valid JSON; inspect the saved raw response.") from exc
    if not isinstance(result, dict):
        raise WorkflowError("Model output must be a JSON object.")
    return result
