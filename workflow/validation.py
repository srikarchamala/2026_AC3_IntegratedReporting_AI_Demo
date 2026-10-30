"""Deterministic provenance checks; these are not a clinical validation engine."""

from __future__ import annotations

from .common import SECTION_IDS, normalize, schema


def flag(category: str, concern: str, reference: str = "general", severity: str = "high") -> dict:
    return {"severity": severity, "category": category, "concern": concern, "reference": reference}


def schema_flags(data: dict, filename: str) -> list:
    from jsonschema import Draft202012Validator
    validator = Draft202012Validator(schema(filename))
    return [flag("schema", error.message, "/".join(map(str, error.absolute_path)) or "root")
            for error in sorted(validator.iter_errors(data), key=lambda e: str(e.absolute_path))][:20]


def validate_extraction(data: dict, document: dict) -> list:
    source_id = document["source_id"]
    flags = schema_flags(data, f"extractor_{source_id}.schema.json")
    if flags:
        return flags
    if data["source_id"] != source_id or data["document_name"] != document["document_name"]:
        flags.append(flag("source_identity", "Extraction names a different input source or document.", source_id))
    pages = {p["page"]: p["text"] for p in document["pages"]}
    seen = set()
    for finding in data["findings"]:
        fid, status = finding["id"], finding["status"]
        if fid in seen or not fid.startswith(source_id + "-"):
            flags.append(flag("finding_id", "Finding ID is duplicated or belongs to another source.", fid))
        seen.add(fid)
        quote, page = normalize(finding["quote"]), finding["page"]
        if status == "not_reported":
            if finding["value"] is not None or quote or page is not None:
                flags.append(flag("missingness", "Not-reported finding must have null value/page and no invented quote.", fid))
        elif status == "unreadable" and not quote:
            if (page is not None and page not in pages) or finding["value"] is not None:
                flags.append(flag("unreadable", "Unreadable finding must retain a null value; any cited page must exist.", fid))
        elif not quote or page not in pages or quote not in normalize(pages.get(page, "")):
            flags.append(flag("quote_mismatch", "Finding quote does not occur on its cited input page.", fid))
    return flags


def validate_identity(extractions: list[dict]) -> list:
    flags = []
    # Accession numbers can legitimately differ by laboratory; do not equate
    # accessions with patient or specimen identity.
    for field in ("patient_identifier", "date_of_birth"):
        values, missing = {}, []
        for extraction in extractions:
            matches = [f for f in extraction["findings"] if f["field"] == field
                       and f["status"] == "reported" and f["value"] is not None]
            if not matches:
                missing.append(extraction["source_id"])
            for match in matches:
                values.setdefault(normalize(match["value"]).casefold(), []).append(match["id"])
        if len(values) > 1:
            flags.append(flag("identity_conflict", f"Different reported {field} values require review before combining reports.", field))
        if missing:
            flags.append(flag("identity_incomplete", f"{field} not established in: {', '.join(missing)}.", field, "medium"))
    return flags


def validate_integration(data: dict, extractions: list[dict], references: list[dict]) -> list:
    flags = schema_flags(data, "integration.schema.json")
    if flags:
        return flags
    findings = {f["id"]: f for e in extractions for f in e["findings"]}
    finding_ids = set(findings)
    sources = {r["source_id"]: r for r in references}
    who_source_ids = {sid for sid in sources if sid.startswith("WHO")}
    if not who_source_ids:
        flags.append(flag("missing_reference", "No approved WHO reference snapshot was supplied."))
    criteria = {}
    for criterion in data["criteria_assessment"]:
        cid = criterion["id"]
        if cid in criteria:
            flags.append(flag("criterion_id", "Duplicate criterion ID.", cid))
        criteria[cid] = criterion
        source = sources.get(criterion["source_id"])
        passage = next((p for p in (source or {}).get("passages", [])
                        if p["id"] == criterion["passage_id"]), None)
        if not passage or not normalize(criterion["quote"]) or normalize(criterion["quote"]) not in normalize(passage["text"]):
            flags.append(flag("guideline_quote", "Criterion is not backed by a quote from the cited retrieved passage.", cid))
        if set(criterion["finding_ids"]) - finding_ids:
            flags.append(flag("finding_reference", "Criterion cites a finding that does not exist.", cid))
        if criterion["assessment"] in {"met", "not_met"} and not criterion["finding_ids"]:
            flags.append(flag("criterion_evidence", "A met/not-met criterion requires case evidence.", cid))
        elif criterion["assessment"] in {"met", "not_met"} and not any(
                findings.get(fid, {}).get("status") in {"reported", "negative", "equivocal"}
                for fid in criterion["finding_ids"]):
            flags.append(flag("criterion_evidence", "Missing, pending or unreadable findings cannot establish a met/not-met criterion.", cid))
    if [s["id"] for s in data["sections"]] != SECTION_IDS:
        flags.append(flag("report_sections", "Report must contain the eleven required sections once, in order."))
    seen_sentences = set()
    for section in data["sections"]:
        for sentence in section["sentences"]:
            sid = sentence["id"]
            if sid in seen_sentences:
                flags.append(flag("sentence_id", "Duplicate sentence ID.", sid))
            seen_sentences.add(sid)
            if set(sentence["finding_ids"]) - finding_ids or set(sentence["criterion_ids"]) - criteria.keys():
                flags.append(flag("sentence_reference", "Sentence cites a nonexistent finding or criterion.", sid))
            if not sentence["finding_ids"] and not sentence["criterion_ids"]:
                flags.append(flag("unsupported_sentence", "Sentence has no finding or guideline support.", sid))
    if data["classification_status"] == "supported":
        who_criteria = {cid: c for cid, c in criteria.items() if c["source_id"] in who_source_ids}
        if not any(c["assessment"] == "met" for c in who_criteria.values()):
            flags.append(flag("classification_support", "Supported classification requires assessed and met WHO criteria."))
        # Unknown eligibility/exclusion criteria cannot be turned into a positive
        # classification. Optional risk uncertainty does not change WHO status.
        if any(c["assessment"] == "unknown" for c in who_criteria.values()):
            flags.append(flag("unresolved_criterion", "Supported classification has an unresolved relevant criterion."))
        diagnosis = next(s for s in data["sections"] if s["id"] == "diagnosis")
        if not any(set(s["criterion_ids"]) & who_criteria.keys() for s in diagnosis["sentences"]):
            flags.append(flag("diagnosis_reference", "A supported integrated diagnosis must cite the applied WHO criteria."))
    if sources and data["framework"] not in {r["framework"] for r in references if "WHO" in r["source_id"]}:
        flags.append(flag("framework_mismatch", "Classification framework differs from the approved WHO reference."))
    return flags


def has_high(flags: list[dict]) -> bool:
    return any(f.get("severity") == "high" for f in flags)
