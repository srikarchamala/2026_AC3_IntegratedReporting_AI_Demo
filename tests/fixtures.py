"""Clearly artificial outputs for testing orchestration, not diagnostic accuracy."""

import json
from copy import deepcopy
from threading import Lock

from workflow.common import INPUT_FILES, SECTION_IDS, schema
from workflow.providers import ModelResult


REFERENCE = {
    "source_id": "WHO5E_MYEOID_2022",
    "title": "Artificial test reference; not clinical guidance",
    "framework": "WHO fifth edition (2022 myeloid overview)",
    "edition": "TEST FIXTURE",
    "canonical_url": "https://example.invalid/test-reference",
    "retrieved_url": None,
    "retrieved_at": "2026-01-01T00:00:00+00:00",
    "sha256": "0" * 64,
    "acquisition_method": "test_fixture",
    "scope": "Orchestration testing only, not clinical guidance.",
    "passages": [{"id": "TEST-P1", "section": "Artificial test section",
                  "text": "This artificial criterion requires evidence not supplied in the fixture."}],
}


def document(source_id="MORPH"):
    return {"source_id": source_id, "document_name": INPUT_FILES[source_id],
            "sha256": "1" * 64,
            "pages": [{"page": 1, "text": "Synthetic finding. Patient TEST-A. No result supplied."},
                      {"page": 2, "text": "A separate page."}]}


def extraction(doc):
    sid = doc["source_id"]
    checks = schema(f"extractor_{sid}.schema.json")["properties"]["findings"]["allOf"]
    fields = [check["contains"]["properties"]["field"]["const"] for check in checks]
    findings = [{"id": f"{sid}-{i:03}", "field": field, "group_id": None,
                 "value": None, "status": "not_reported", "units": None,
                 "method": None, "denominator": None, "quote": "", "page": None}
                for i, field in enumerate(fields, 1)]
    # One real source quotation establishes a reported statement. All other
    # fields intentionally remain missing; this is not a case extraction.
    item = next(f for f in findings if f["field"] == "reported_interpretation")
    item.update(value="Synthetic test quotation", status="reported",
                quote=doc["pages"][0]["text"].splitlines()[0], page=1)
    return {"source_id": sid, "document_name": doc["document_name"], "findings": findings}


def integration(extractions=None, references=None):
    extractions = extractions or [extraction(document())]
    references = references or [deepcopy(REFERENCE)]
    fid = extractions[0]["findings"][0]["id"]
    source = references[0]
    passage = source["passages"][0]
    return {
        "framework": source["framework"], "classification_status": "insufficient_evidence",
        "criteria_assessment": [{"id": "C1", "criterion": "Artificial missing prerequisite",
            "source_id": source["source_id"], "passage_id": passage["id"],
            "quote": passage["text"], "finding_ids": [fid], "assessment": "unknown",
            "explanation": "Synthetic test data do not establish the prerequisite."}],
        "sections": [{"id": sid, "title": sid.replace("_", " ").title(),
            "sentences": [{"id": f"S{i}", "text": "Artificial test draft: evidence is incomplete.",
                           "finding_ids": [fid], "criterion_ids": ["C1"] if sid == "diagnosis" else []}]}
            for i, sid in enumerate(SECTION_IDS, 1)],
        "unresolved_issues": ["Artificial fixture; no clinical interpretation performed."],
    }


class FakeClient:
    """Return visible fixtures and record all inputs for isolation assertions."""

    def __init__(self, bad_quote=False, bad_criterion=False, qa_flags=None):
        self.calls, self.lock = [], Lock()
        self.bad_quote, self.bad_criterion = bad_quote, bad_criterion
        self.qa_flags = qa_flags or []

    def complete(self, system, user, json_output=True):
        payload = json.loads(user.split("\n", 1)[1])
        with self.lock:
            self.calls.append({"system": system, "payload": deepcopy(payload)})
        if "source_id" in payload:
            result = extraction(payload)
            if self.bad_quote and payload["source_id"] == "MORPH":
                next(f for f in result["findings"] if f["status"] == "reported")["quote"] = "FABRICATED QUOTE NOT IN ANY PDF"
        elif "formal_risk_assessment_enabled" in payload:
            result = integration(payload["extractions"], payload["references"])
            if self.bad_criterion:
                result["criteria_assessment"][0]["quote"] = "INVENTED GUIDELINE STATEMENT"
        else:
            result = {"flags": deepcopy(self.qa_flags)}
        return ModelResult(json.dumps(result), {"provider": "test_fixture", "usage": {}, "clinical_validation": False})
