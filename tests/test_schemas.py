"""Structural and evidence-boundary tests using a wholly fictional case.

These fixtures exercise the serialization contract, not medical classification.
The source text is defined independently of the extracted findings so that a
schema-valid fabrication can also be checked against the actual source boundary.
"""

import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

from workflow.validation import validate_extraction


SCHEMA_DIR = Path(__file__).resolve().parents[1] / "workflow" / "schemas"
SOURCES = ("MORPH", "FLOW", "CYTO", "MOLEC")
SCHEMA_NAMES = tuple(f"extractor_{source}.schema.json" for source in SOURCES) + (
    "integration.schema.json", "qa.schema.json",
)
SECTION_IDS = (
    "patient_specimen", "component_studies", "clinical_context", "morphology",
    "flow", "cytogenetics", "molecular", "interpretation", "diagnosis",
    "prognostic_predictive", "limitations",
)

COMMON_TEXT = """Patient identifier: DEMO-001.
Patient name: Example, Fictional.
Date of birth: 2000-01-01.
Specimen identifier: SPEC-001.
Specimen description: Bone marrow aspirate.
Collection date: 2026-01-02.
Report date: 2026-01-03.
Report status: Final.
Interpretation: Findings require integrated review.
Limitations: Assessment is limited to this report.
"""

MODALITY_TEXT = {
    "MORPH": """Cellularity: variable.
Manual differential: blasts 7% of 100 counted cells.
Morphology: cellular aspirate.
Lineage assessment: uncertain.
Immunohistochemistry: not performed.
Specimen adequacy: sufficient.
""",
    "FLOW": """Gated blasts: 9% of acquired nucleated events.
Population: gated blast population.
Immunophenotype: marker A positive; marker B equivocal.
Gating strategy: viable singlet events.
Lineage assessment: indeterminate.
Specimen adequacy: sufficient.
""",
    "CYTO": """Karyotype: 46,XY[10].
Metaphases evaluated: 10.
FISH target: example target A.
FISH result for example target A: negative.
Assay coverage: example target A only.
Specimen adequacy: sufficient.
""",
    "MOLEC": """Assay: Example panel.
Assay scope: Example locus only.
Method: targeted sequencing.
Result: one synthetic variant is listed.
Coverage/sensitivity: sensitivity is unspecified in this teaching source.
Gene: EXAMPLE1.
Variant: example-variant.
Variant allele fraction: 0.12.
""",
}


def load_schema(name):
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


def extraction_fixture(source):
    """A complete small report, with absent and explicitly unavailable fields."""
    findings = []

    def add(field, value=None, quote="", status="reported", **context):
        finding = {
            "id": f"{source}-{len(findings) + 1:03d}",
            "field": field, "group_id": None, "value": value,
            "status": status, "units": None, "method": None,
            "denominator": None, "quote": quote,
            "page": 1 if quote else None,
        }
        finding.update(context)
        findings.append(finding)

    add("patient_identifier", "DEMO-001", "Patient identifier: DEMO-001.")
    add("patient_name", "Example, Fictional", "Patient name: Example, Fictional.")
    add("date_of_birth", "2000-01-01", "Date of birth: 2000-01-01.")
    add("specimen_identifier", "SPEC-001", "Specimen identifier: SPEC-001.")
    add("specimen_description", "Bone marrow aspirate", "Specimen description: Bone marrow aspirate.")
    add("accession_number", f"{source}-A001", f"Accession: {source}-A001.")
    add("performing_lab", f"Fictional {source} Laboratory", f"Laboratory: Fictional {source} Laboratory.")
    add("collection_date", "2026-01-02", "Collection date: 2026-01-02.")
    add("report_date", "2026-01-03", "Report date: 2026-01-03.")
    add("report_status", "Final", "Report status: Final.")
    add("clinical_history", status="not_reported")
    add("reported_interpretation", "Findings require integrated review", "Interpretation: Findings require integrated review.")
    add("limitations", "Assessment is limited to this report", "Limitations: Assessment is limited to this report.")

    if source == "MORPH":
        add("cellularity", "variable", "Cellularity: variable.")
        add("blast_percentage", 7, "Manual differential: blasts 7% of 100 counted cells.",
            units="%", method="manual differential", denominator="100 counted cells")
        add("promonocyte_percentage", status="not_reported")
        add("morphology_findings", "cellular aspirate", "Morphology: cellular aspirate.")
        add("lineage_assessment", "uncertain", "Lineage assessment: uncertain.")
        add("immunohistochemistry", quote="Immunohistochemistry: not performed.", status="not_performed")
        add("specimen_adequacy", "sufficient", "Specimen adequacy: sufficient.")
    elif source == "FLOW":
        add("blast_percentage", 9, "Gated blasts: 9% of acquired nucleated events.",
            units="%", method="gated", denominator="acquired nucleated events", group_id="FLOW-P001")
        add("promonocyte_percentage", status="not_reported")
        add("population_description", "gated blast population", "Population: gated blast population.", group_id="FLOW-P001")
        add("immunophenotype", "marker A positive; marker B equivocal", "Immunophenotype: marker A positive; marker B equivocal.", group_id="FLOW-P001")
        add("gating_strategy", "viable singlet events", "Gating strategy: viable singlet events.")
        add("lineage_assessment", "indeterminate", "Lineage assessment: indeterminate.", status="equivocal")
        add("specimen_adequacy", "sufficient", "Specimen adequacy: sufficient.")
    elif source == "CYTO":
        add("karyotype", "46,XY[10]", "Karyotype: 46,XY[10].")
        add("metaphase_count", 10, "Metaphases evaluated: 10.")
        add("banding_resolution", status="not_reported")
        add("fish_target", "example target A", "FISH target: example target A.", group_id="CYTO-T001")
        add("fish_result", "negative", "FISH result for example target A: negative.", status="negative", group_id="CYTO-T001")
        add("assay_coverage", "example target A only", "Assay coverage: example target A only.")
        add("specimen_adequacy", "sufficient", "Specimen adequacy: sufficient.")
    elif source == "MOLEC":
        add("assay_name", "Example panel", "Assay: Example panel.")
        add("assay_scope", "Example locus only", "Assay scope: Example locus only.")
        add("assay_method", "targeted sequencing", "Method: targeted sequencing.")
        add("result_summary", "one synthetic variant is listed", "Result: one synthetic variant is listed.")
        add("coverage_or_sensitivity", "sensitivity is unspecified in this teaching source", "Coverage/sensitivity: sensitivity is unspecified in this teaching source.")
        add("gene", "EXAMPLE1", "Gene: EXAMPLE1.", group_id="MOLEC-G001")
        add("variant", "example-variant", "Variant: example-variant.", group_id="MOLEC-G001")
        add("variant_allele_fraction", 0.12, "Variant allele fraction: 0.12.", group_id="MOLEC-G001")
        add("reported_variant_tier", status="not_reported", group_id="MOLEC-G001")
    else:
        raise ValueError(source)

    document_name = f"synthetic_{source.lower()}.pdf"
    document = {
        "source_id": source, "document_name": document_name,
        "pages": [{"page": 1, "text": (
            COMMON_TEXT + f"Accession: {source}-A001.\n"
            + f"Laboratory: Fictional {source} Laboratory.\n" + MODALITY_TEXT[source]
        )}],
    }
    return {"source_id": source, "document_name": document_name, "findings": findings}, document


def by_field(extraction, field):
    return next(finding for finding in extraction["findings"] if finding["field"] == field)


def integration_fixture(status="insufficient_evidence"):
    """An evidence-limited draft without a real medical decision rule."""
    return {
        "framework": "Fictional format-checking framework",
        "classification_status": status,
        "criteria_assessment": [{
            "id": "CRIT-001",
            "criterion": "The fictional assessment requires supplied clinical history.",
            "source_id": "EXAMPLE_REFERENCE", "passage_id": "EXAMPLE-P1",
            "quote": "This fictional assessment requires supplied clinical history.",
            "finding_ids": ["MORPH-011"],
            "assessment": "unknown", "explanation": "Clinical history is not reported.",
        }],
        "sections": [
            {
                "id": section_id, "title": section_id.replace("_", " ").title(),
                "sentences": [{
                    "id": f"S{index:03d}",
                    "text": "The component report states that its findings require integrated review.",
                    "finding_ids": ["MORPH-012"], "criterion_ids": [],
                }],
            }
            for index, section_id in enumerate(SECTION_IDS, 1)
        ],
        "unresolved_issues": ["The fictional assessment lacks its required clinical history."],
    }


class SchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schemas = {name: load_schema(name) for name in SCHEMA_NAMES}
        cls.validators = {name: Draft202012Validator(schema) for name, schema in cls.schemas.items()}

    def assert_valid(self, instance, name):
        errors = list(self.validators[name].iter_errors(instance))
        self.assertEqual(errors, [], "\n".join(error.message for error in errors))

    def assert_invalid(self, instance, name):
        self.assertTrue(list(self.validators[name].iter_errors(instance)), "Invalid contract was accepted")

    def test_schemas_are_draft_2020_12_and_resolve_without_external_refs(self):
        def walk(node):
            if isinstance(node, dict):
                for key, value in node.items():
                    if key == "$ref":
                        self.assertTrue(value.startswith("#"), f"External schema reference: {value}")
                    yield from walk(value)
            elif isinstance(node, list):
                for value in node:
                    yield from walk(value)
            yield None

        for name, schema in self.schemas.items():
            with self.subTest(schema=name):
                self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
                Draft202012Validator.check_schema(schema)
                list(walk(schema))

    def test_complete_independent_reports_validate_against_schema_and_source_pages(self):
        for source in SOURCES:
            with self.subTest(source=source):
                extraction, document = extraction_fixture(source)
                self.assert_valid(extraction, f"extractor_{source}.schema.json")
                self.assertEqual(validate_extraction(extraction, document), [])

    def test_absent_not_performed_equivocal_and_negative_are_distinct_valid_states(self):
        morph, _ = extraction_fixture("MORPH")
        flow, _ = extraction_fixture("FLOW")
        cyto, _ = extraction_fixture("CYTO")
        self.assertEqual(by_field(morph, "promonocyte_percentage")["status"], "not_reported")
        self.assertEqual(by_field(morph, "immunohistochemistry")["status"], "not_performed")
        self.assertEqual(by_field(flow, "lineage_assessment")["status"], "equivocal")
        self.assertEqual(by_field(cyto, "fish_result")["status"], "negative")
        for source, extraction in (("MORPH", morph), ("FLOW", flow), ("CYTO", cyto)):
            self.assert_valid(extraction, f"extractor_{source}.schema.json")

    def test_missing_checklist_fields_cannot_disappear_silently(self):
        core = {"MORPH": "blast_percentage", "FLOW": "gating_strategy",
                "CYTO": "fish_result", "MOLEC": "result_summary"}
        for source in SOURCES:
            for field in ("patient_identifier", core[source]):
                with self.subTest(source=source, field=field):
                    extraction, _ = extraction_fixture(source)
                    extraction["findings"] = [f for f in extraction["findings"] if f["field"] != field]
                    self.assert_invalid(extraction, f"extractor_{source}.schema.json")

    def test_not_reported_rejects_invented_values_or_evidence(self):
        contradictions = (
            {"value": "negative"}, {"value": 0}, {"quote": "not present"},
            {"page": 1}, {"units": "%"}, {"method": "assumed method"},
            {"denominator": "assumed population"},
        )
        for changes in contradictions:
            with self.subTest(changes=changes):
                extraction, _ = extraction_fixture("MORPH")
                by_field(extraction, "clinical_history").update(changes)
                self.assert_invalid(extraction, "extractor_MORPH.schema.json")

    def test_source_supported_statuses_require_quote_page_and_appropriate_value(self):
        for status in ("reported", "negative", "equivocal", "pending", "not_performed"):
            for changes in ({"quote": ""}, {"page": None}, {"page": 0}):
                with self.subTest(status=status, changes=changes):
                    extraction, _ = extraction_fixture("CYTO")
                    finding = by_field(extraction, "fish_result")
                    finding["status"] = status
                    finding.update(changes)
                    self.assert_invalid(extraction, "extractor_CYTO.schema.json")
        for status in ("reported", "negative", "equivocal"):
            for value in (None, True, ""):
                with self.subTest(status=status, value=value):
                    extraction, _ = extraction_fixture("CYTO")
                    by_field(extraction, "fish_result").update(status=status, value=value)
                    self.assert_invalid(extraction, "extractor_CYTO.schema.json")

    def test_pending_and_unreadable_can_remain_unknown_without_fabricated_value(self):
        extraction, document = extraction_fixture("MOLEC")
        pending = by_field(extraction, "result_summary")
        pending.update(status="pending", value=None, quote="Result: pending.")
        document["pages"][0]["text"] += "\nResult: pending.\n"
        self.assert_valid(extraction, "extractor_MOLEC.schema.json")
        self.assertEqual(validate_extraction(extraction, document), [])
        for page in (None, 1):
            with self.subTest(page=page):
                unreadable = copy.deepcopy(extraction)
                by_field(unreadable, "result_summary").update(status="unreadable", value=None, quote="", page=page)
                self.assert_valid(unreadable, "extractor_MOLEC.schema.json")
                by_field(unreadable, "result_summary")["value"] = "guessed result"
                self.assert_invalid(unreadable, "extractor_MOLEC.schema.json")

    def test_wrong_modality_fields_and_inferred_classification_are_rejected(self):
        extraction, _ = extraction_fixture("MORPH")
        extra = copy.deepcopy(extraction["findings"][0])
        extra.update(id="MORPH-999", field="karyotype")
        extraction["findings"].append(extra)
        self.assert_invalid(extraction, "extractor_MORPH.schema.json")
        extraction, _ = extraction_fixture("MOLEC")
        by_field(extraction, "variant")["classifying"] = True
        self.assert_invalid(extraction, "extractor_MOLEC.schema.json")
        extraction, _ = extraction_fixture("MOLEC")
        extraction["derived_diagnosis"] = "An inferred category"
        self.assert_invalid(extraction, "extractor_MOLEC.schema.json")

    def test_schema_valid_quote_does_not_substitute_for_source_verification(self):
        extraction, document = extraction_fixture("FLOW")
        by_field(extraction, "blast_percentage")["quote"] = "This sentence is absent from the original page."
        self.assert_valid(extraction, "extractor_FLOW.schema.json")
        flags = validate_extraction(extraction, document)
        self.assertIn("quote_mismatch", {flag["category"] for flag in flags})

    def test_evidence_limited_and_out_of_scope_drafts_are_representable(self):
        for status in ("insufficient_evidence", "out_of_scope"):
            with self.subTest(status=status):
                draft = integration_fixture(status)
                self.assert_valid(draft, "integration.schema.json")
                draft["criteria_assessment"] = []
                self.assert_valid(draft, "integration.schema.json")

    def test_supported_classification_requires_some_assessed_reference_criteria(self):
        draft = integration_fixture("supported")
        draft["criteria_assessment"][0].update(
            criterion="This fictional reporting label requires a documented specimen identifier.",
            quote="A documented specimen identifier is required for this fictional reporting label.",
            finding_ids=["MORPH-004"], assessment="met",
            explanation="The source explicitly reports specimen identifier SPEC-001.",
        )
        draft["sections"][8]["sentences"][0].update(
            text="The fictional reporting label's specimen-identifier prerequisite is documented.",
            finding_ids=["MORPH-004"], criterion_ids=["CRIT-001"],
        )
        draft["unresolved_issues"] = []
        self.assert_valid(draft, "integration.schema.json")
        draft["criteria_assessment"] = []
        self.assert_invalid(draft, "integration.schema.json")

    def test_exact_eleven_sections_in_contract_order_are_required(self):
        mutations = []
        swapped = integration_fixture(); swapped["sections"][0], swapped["sections"][1] = swapped["sections"][1], swapped["sections"][0]; mutations.append(swapped)
        omitted = integration_fixture(); omitted["sections"].pop(); mutations.append(omitted)
        extra = integration_fixture(); extra["sections"].append(copy.deepcopy(extra["sections"][0])); mutations.append(extra)
        duplicate = integration_fixture(); duplicate["sections"][1] = copy.deepcopy(duplicate["sections"][0]); mutations.append(duplicate)
        for draft in mutations:
            with self.subTest(section_ids=[section["id"] for section in draft["sections"]]):
                self.assert_invalid(draft, "integration.schema.json")

    def test_every_sentence_needs_at_least_one_kind_of_provenance(self):
        for section_index in range(len(SECTION_IDS)):
            with self.subTest(section=SECTION_IDS[section_index]):
                draft = integration_fixture()
                sentence = draft["sections"][section_index]["sentences"][0]
                sentence.update(finding_ids=[], criterion_ids=[])
                self.assert_invalid(draft, "integration.schema.json")
                sentence["criterion_ids"] = ["CRIT-001"]
                self.assert_valid(draft, "integration.schema.json")
                sentence["finding_ids"] = ["MORPH-011"]
                self.assert_valid(draft, "integration.schema.json")

    def test_qa_accepts_no_flags_or_a_concrete_flag_but_not_a_rewritten_report(self):
        self.assert_valid({"flags": []}, "qa.schema.json")
        flags = {"flags": [{"severity": "high", "category": "missingness_error",
                            "concern": "A missing field was presented as a negative result.",
                            "reference": "MORPH-011"}]}
        self.assert_valid(flags, "qa.schema.json")
        invalid = copy.deepcopy(flags); invalid["flags"][0]["severity"] = "acceptable"
        self.assert_invalid(invalid, "qa.schema.json")
        invalid = copy.deepcopy(flags); invalid["corrected_report"] = "Replacement draft"
        self.assert_invalid(invalid, "qa.schema.json")


if __name__ == "__main__":
    unittest.main()
