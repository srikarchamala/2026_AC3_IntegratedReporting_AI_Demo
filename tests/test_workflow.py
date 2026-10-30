"""Offline orchestration, provenance and failure-path tests."""

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from workflow.__main__ import make_chat_pack, parser, run_workflow, validate_saved
from workflow.common import INPUT_FILES, ROOT, WorkflowError, json_from_model, read_json, write_json
from workflow.render import render_reports
from workflow.validation import has_high, validate_extraction, validate_identity, validate_integration
from tests.fixtures import FakeClient, REFERENCE, document, extraction, integration


class ProvenanceTests(unittest.TestCase):
    def test_fabricated_quote_and_wrong_page_are_rejected(self):
        doc, data = document(), extraction(document())
        reported = next(f for f in data["findings"] if f["status"] == "reported")
        self.assertFalse(has_high(validate_extraction(data, doc)))
        reported["page"] = 2
        self.assertTrue(any(f["category"] == "quote_mismatch" for f in validate_extraction(data, doc)))
        reported.update(page=1, quote="Synthetic finding that was not actually written.")
        self.assertTrue(has_high(validate_extraction(data, doc)))

    def test_missing_value_cannot_be_relabelled_as_negative(self):
        data = extraction(document())
        data["findings"][0]["status"] = "negative"
        self.assertTrue(has_high(validate_extraction(data, document())))

    def test_unknown_page_for_unreadable_field_is_preserved(self):
        data = extraction(document())
        data["findings"][0]["status"] = "unreadable"
        self.assertFalse(has_high(validate_extraction(data, document())))
        data["findings"][0]["page"] = 99
        self.assertTrue(has_high(validate_extraction(data, document())))

    def test_conflicting_patient_identifiers_stop_integration(self):
        extracts = [extraction(document(sid)) for sid in INPUT_FILES]
        for index, data in enumerate(extracts):
            item = next(f for f in data["findings"] if f["field"] == "patient_identifier")
            item.update(value="TEST-A" if index < 3 else "TEST-B", status="reported")
        self.assertTrue(any(f["category"] == "identity_conflict" for f in validate_identity(extracts)))

    def test_invented_criterion_and_dangling_evidence_are_rejected(self):
        extracts, refs = [extraction(document())], [deepcopy(REFERENCE)]
        data = integration(extracts, refs)
        data["criteria_assessment"][0]["quote"] = "Guidance that was never retrieved."
        data["sections"][0]["sentences"][0]["finding_ids"] = ["MORPH-999"]
        categories = {f["category"] for f in validate_integration(data, extracts, refs)}
        self.assertIn("guideline_quote", categories)
        self.assertIn("sentence_reference", categories)

    def test_missing_criterion_evidence_cannot_be_marked_met(self):
        extracts = [extraction(document())]
        data = integration(extracts)
        data["criteria_assessment"][0]["assessment"] = "met"
        self.assertTrue(any(f["category"] == "criterion_evidence"
                            for f in validate_integration(data, extracts, [REFERENCE])))

    def test_insufficient_or_out_of_scope_can_cite_evidence_gap(self):
        extracts = [extraction(document())]
        for status in ("insufficient_evidence", "out_of_scope"):
            with self.subTest(status=status):
                data = integration(extracts)
                data["classification_status"] = status
                data["criteria_assessment"] = []
                for section in data["sections"]:
                    section["sentences"][0]["criterion_ids"] = []
                self.assertFalse(has_high(validate_integration(data, extracts, [REFERENCE])))

    def test_optional_risk_uncertainty_does_not_block_supported_who_classification(self):
        extracts = [extraction(document())]
        reported_id = next(f["id"] for f in extracts[0]["findings"] if f["status"] == "reported")
        data = integration(extracts)
        data["classification_status"] = "supported"
        data["criteria_assessment"][0].update(assessment="met", finding_ids=[reported_id])
        risk = deepcopy(REFERENCE)
        risk.update(source_id="ELN2022_AML_RISK", framework="ELN 2022 adult AML genetic risk")
        criterion = deepcopy(data["criteria_assessment"][0])
        criterion.update(id="R1", source_id=risk["source_id"], assessment="unknown", finding_ids=[])
        data["criteria_assessment"].append(criterion)
        self.assertFalse(has_high(validate_integration(data, extracts, [REFERENCE, risk])))
        data["criteria_assessment"][0]["assessment"] = "unknown"
        self.assertTrue(has_high(validate_integration(data, extracts, [REFERENCE, risk])))

    def test_no_hidden_json_salvage(self):
        for text in ('Here is JSON: {"x": 1}', '{"x":', '[]', '{"x":1}\n{"y":2}'):
            with self.subTest(text=text), self.assertRaises(WorkflowError):
                json_from_model(text)
        self.assertEqual(json_from_model('```json\n{"x": 1}\n```'), {"x": 1})

    def test_html_escapes_model_text_and_labels_local_imports(self):
        data, refs = integration(), [deepcopy(REFERENCE)]
        data["sections"][0]["sentences"][0]["text"] = '<script>alert("injected")</script>'
        refs[0]["acquisition_method"] = "local_import"
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            render_reports(out, data, [extraction(document())], refs, [])
            html = (out / "report.html").read_text()
            self.assertNotIn("<script>", html)
            self.assertIn("&lt;script&gt;", html)
            self.assertIn("local_import", html)
            self.assertIn("Local original article import", html)
            self.assertIn('id="WHO5E_MYEOID_2022--TEST-P1"', html)


class WorkflowTests(unittest.TestCase):
    def args(self, output):
        return parser().parse_args(["run", "--provider", "openai", "--model", "TEST-MODEL",
                                   "--out", str(output), "--case-dir", str(ROOT / "case")])

    def run_fake(self, output, client):
        with patch("workflow.retrieval.retrieve_sources", return_value=[deepcopy(REFERENCE)]), redirect_stdout(io.StringIO()):
            return run_workflow(self.args(output), client=client)

    def test_six_independent_calls_and_answer_key_isolation(self):
        with tempfile.TemporaryDirectory() as directory:
            out, client = Path(directory) / "run", FakeClient()
            self.assertEqual(self.run_fake(out, client), 0)
            self.assertEqual(len(client.calls), 6)
            extracts = [c for c in client.calls if "source_id" in c["payload"]]
            self.assertEqual({c["payload"]["source_id"] for c in extracts}, set(INPUT_FILES))
            for call in extracts:
                self.assertEqual(set(call["payload"]), {"source_id", "document_name", "sha256", "pages"})
                self.assertNotIn("Artificial test reference", json.dumps(call))
            for call in client.calls:
                payload_text = json.dumps(call["payload"])
                self.assertNotIn("05_GOLD_STANDARD", payload_text)
                self.assertNotIn("00_DEMO_GUIDE", payload_text)
            self.assertTrue((out / "report.html").is_file())
            self.assertEqual(read_json(out / "manifest.json")["clinical_validation"], False)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(validate_saved(out), 0)

    def test_bad_extraction_stops_before_integration(self):
        with tempfile.TemporaryDirectory() as directory:
            out, client = Path(directory) / "run", FakeClient(bad_quote=True)
            with self.assertRaisesRegex(WorkflowError, "integration was stopped"):
                self.run_fake(out, client)
            self.assertEqual(len(client.calls), 4)
            self.assertFalse((out / "integration.json").exists())
            self.assertEqual(read_json(out / "manifest.json")["status"], "failed")

    def test_bad_guideline_quote_prevents_render_and_qa(self):
        with tempfile.TemporaryDirectory() as directory:
            out, client = Path(directory) / "run", FakeClient(bad_criterion=True)
            with self.assertRaisesRegex(WorkflowError, "no final report was rendered"):
                self.run_fake(out, client)
            self.assertEqual(len(client.calls), 5)
            self.assertFalse((out / "report.html").exists())

    def test_high_qa_is_visible_and_survives_revalidation(self):
        qa = [{"severity": "high", "category": "semantic_test", "concern": "Artificial semantic QA failure", "reference": "S1"}]
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "run"
            self.assertEqual(self.run_fake(out, FakeClient(qa_flags=qa)), 2)
            self.assertIn("Artificial semantic QA failure", (out / "report.html").read_text())
            with redirect_stdout(io.StringIO()):
                self.assertEqual(validate_saved(out), 2)

    def test_changed_input_or_reference_snapshot_is_detected(self):
        for kind in ("input", "reference"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as directory:
                out = Path(directory) / "run"
                self.run_fake(out, FakeClient())
                path = out / "inputs" / "MORPH.json" if kind == "input" else out / "references.json"
                data = read_json(path)
                if kind == "input":
                    data["pages"][0]["text"] += " Tampered after the run."
                else:
                    data[0]["passages"][0]["text"] += " Tampered after the run."
                write_json(path, data)
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(validate_saved(out), 2)
                self.assertTrue(any("integrity" in f["category"] for f in read_json(out / "revalidation.json")))

    def test_chat_pack_only_contains_four_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "pack"
            args = parser().parse_args(["chat-pack", "--out", str(out)])
            with redirect_stdout(io.StringIO()):
                self.assertEqual(make_chat_pack(args), 0)
            self.assertEqual({p.name for p in (out / "case").iterdir()}, set(INPUT_FILES.values()))
            self.assertFalse(any("GOLD_STANDARD" in p.name for p in out.rglob("*")))
            self.assertIn("manual orchestration", (out / "START_HERE.md").read_text())


if __name__ == "__main__":
    unittest.main()
