"""Provider contract tests with fake credentials and no external API calls.

These checks cover source isolation and fail-closed response handling, not model
quality. Header/response contracts were reviewed against the official Messages
2026-10-21 and OpenAI Responses documentation.
"""
import io
import json
import os
import unittest
import urllib.error
import urllib.request
from unittest.mock import Mock, patch

from workflow.common import WorkflowError
from workflow.providers import ModelClient, _NoRedirect


FAKE_KEYS = {
    "ANTHROPIC_API_KEY": "not-a-real-anthropic-key-for-unit-tests",
    "OPENAI_API_KEY": "not-a-real-openai-key-for-unit-tests",
}


def completed(provider, text='{"findings": []}', response_id="response-one"):
    if provider == "anthropic":
        return {
            "id": response_id, "model": "test-returned-model",
            "type": "message", "role": "assistant", "stop_reason": "end_turn",
            "stop_details": None,
            "content": [{"type": "text", "text": text}],
            "usage": {"input_tokens": 31, "output_tokens": 12},
        }
    return {
        "id": response_id, "model": "test-returned-model", "status": "completed",
        "output": [{"type": "reasoning", "summary": []}, {
            "type": "message", "role": "assistant", "status": "completed",
            "content": [{"type": "output_text", "text": text, "annotations": []}],
        }],
        "usage": {"input_tokens": 31, "output_tokens": 12},
    }


def response_bytes(value):
    return io.BytesIO(json.dumps(value).encode("utf-8"))


class ProviderTests(unittest.TestCase):
    def setUp(self):
        # Never read actual developer/user credentials during unit tests.
        self.env = patch.dict(os.environ, FAKE_KEYS, clear=True)
        self.env.start()

    def tearDown(self):
        self.env.stop()

    def client(self, provider):
        return ModelClient(provider, "explicit-test-model", max_output_tokens=1024, timeout=7)

    def test_each_complete_call_has_only_its_own_report_and_instructions(self):
        for provider in ("anthropic", "openai"):
            with self.subTest(provider=provider):
                client = self.client(provider)
                opener = Mock()
                opener.open.side_effect = [
                    response_bytes(completed(provider, '{"stage": "first"}', "first-result-id")),
                    response_bytes(completed(provider, '{"stage": "second"}', "second-result-id")),
                ]
                with patch("workflow.providers.urllib.request.build_opener", return_value=opener):
                    client.complete("Extract JSON from morphology ONLY", "MORPH-PRIVATE-MARKER")
                    client.complete("Extract JSON from flow ONLY", "FLOW-PRIVATE-MARKER")
                first, second = [json.loads(call.args[0].data) for call in opener.open.call_args_list]
                self.assertIn("MORPH-PRIVATE-MARKER", json.dumps(first))
                self.assertNotIn("MORPH-PRIVATE-MARKER", json.dumps(second))
                self.assertNotIn("morphology ONLY", json.dumps(second))
                self.assertNotIn("first-result-id", json.dumps(second))
                self.assertNotIn('"stage": "first"', json.dumps(second))
                self.assertNotIn("previous_response_id", second)
                self.assertNotIn("conversation", second)
                if provider == "anthropic":
                    self.assertEqual(second["messages"], [{"role": "user", "content": "FLOW-PRIVATE-MARKER"}])
                    self.assertEqual(second["system"], "Extract JSON from flow ONLY")
                else:
                    self.assertEqual(second["input"], "FLOW-PRIVATE-MARKER")
                    self.assertEqual(second["instructions"], "Extract JSON from flow ONLY")
                    self.assertFalse(second["store"])

    def test_current_anthropic_headers_and_workspace_selection(self):
        client = self.client("anthropic")
        url, headers, body = client.request_data("Return JSON", "Assigned report only")
        self.assertEqual(url, "https://api.anthropic.com/v1/messages")
        self.assertEqual(headers["Authorization"], "Bearer " + FAKE_KEYS["ANTHROPIC_API_KEY"])
        self.assertEqual(headers["anthropic-version"], "2026-10-21")
        self.assertNotIn("anthropic-workspace-id", headers)
        self.assertEqual(body["max_tokens"], 1024)
        for removed_sampling_parameter in ("temperature", "top_p", "top_k"):
            self.assertNotIn(removed_sampling_parameter, body)
        with patch.dict(os.environ, {"ANTHROPIC_WORKSPACE_ID": "wrkspc_fake_unit_test"}):
            _, headers, body = self.client("anthropic").request_data("Return JSON", "Assigned report only")
            self.assertEqual(headers["anthropic-workspace-id"], "wrkspc_fake_unit_test")
            self.assertNotIn("wrkspc_fake_unit_test", json.dumps(body))
            _, openai_headers, openai_body = self.client("openai").request_data("Return JSON", "Assigned report only")
            self.assertNotIn("anthropic-workspace-id", openai_headers)
            self.assertNotIn("wrkspc_fake_unit_test", json.dumps(openai_body))

    def test_openai_json_mode_and_plain_baseline_requests(self):
        client = self.client("openai")
        url, _, body = client.request_data("Return a JSON object", "Assigned report")
        self.assertEqual(url, "https://api.openai.com/v1/responses")
        self.assertEqual(body["text"]["format"]["type"], "json_object")
        self.assertEqual(body["max_output_tokens"], 1024)
        self.assertFalse(body["store"])
        _, _, plain = client.request_data("Write a report", "Assigned reports", json_output=False)
        self.assertNotIn("text", plain)

    def test_credentials_absent_or_blank_fail_before_network(self):
        for provider, env_name in (("anthropic", "ANTHROPIC_API_KEY"), ("openai", "OPENAI_API_KEY")):
            for value in (None, "", "  \t "):
                with self.subTest(provider=provider, value=value):
                    with patch.dict(os.environ, {} if value is None else {env_name: value}, clear=True):
                        with patch("workflow.providers.urllib.request.build_opener") as build:
                            with self.assertRaisesRegex(WorkflowError, env_name):
                                self.client(provider)
                            build.assert_not_called()

    def test_credentials_are_not_in_payloads_or_returned_metadata(self):
        for provider in ("anthropic", "openai"):
            with self.subTest(provider=provider):
                client = self.client(provider)
                _, _, body = client.request_data("Return JSON", "Assigned report")
                result = client.parse_response(completed(provider))
                public_data = json.dumps({"body": body, "metadata": result.metadata})
                for key in FAKE_KEYS.values():
                    self.assertNotIn(key, public_data)
                self.assertNotIn("Authorization", result.metadata)
                self.assertEqual(result.metadata["requested_model"], "explicit-test-model")
                self.assertEqual(result.metadata["returned_model"], "test-returned-model")

    def test_nullable_anthropic_stop_details_is_a_normal_success(self):
        client = self.client("anthropic")
        data = completed("anthropic")
        self.assertIsNone(data["stop_details"])
        self.assertEqual(client.parse_response(data).text, '{"findings": []}')
        del data["stop_details"]
        self.assertEqual(client.parse_response(data).text, '{"findings": []}')

    def test_anthropic_refusal_truncation_and_unfinished_turns_are_rejected(self):
        client = self.client("anthropic")
        for reason in ("refusal", "max_tokens", "model_context_window_exceeded", "pause_turn", "tool_use", None):
            with self.subTest(stop_reason=reason):
                data = completed("anthropic", '{"partial": true}')
                data["stop_reason"] = reason
                if reason == "refusal":
                    data["stop_details"] = {"type": "refusal", "category": None, "explanation": None}
                with self.assertRaisesRegex(WorkflowError, "No output was accepted"):
                    client.parse_response(data)
        # A structured refusal is rejected even if an inconsistent status is received.
        data = completed("anthropic")
        data["stop_details"] = {"type": "refusal", "category": None, "explanation": None}
        with self.assertRaises(WorkflowError):
            client.parse_response(data)

    def test_openai_incomplete_and_refused_responses_are_rejected(self):
        client = self.client("openai")
        for status in ("incomplete", "failed", "cancelled", "in_progress", "queued", None):
            with self.subTest(status=status):
                data = completed("openai", '{"partial": true}')
                data["status"] = status
                data["incomplete_details"] = {"reason": "max_output_tokens"}
                with self.assertRaisesRegex(WorkflowError, "No output was accepted"):
                    client.parse_response(data)
        data = completed("openai")
        data["output"][1]["content"].append({"type": "refusal", "refusal": "Declined"})
        with self.assertRaisesRegex(WorkflowError, "refused"):
            client.parse_response(data)

    def test_empty_or_whitespace_only_output_is_rejected(self):
        for provider in ("anthropic", "openai"):
            for empty in ("", " \n\t "):
                with self.subTest(provider=provider, text=empty):
                    with self.assertRaisesRegex(WorkflowError, "no usable text"):
                        self.client(provider).parse_response(completed(provider, empty))
            data = completed(provider)
            data["content" if provider == "anthropic" else "output"] = []
            with self.assertRaisesRegex(WorkflowError, "no usable text"):
                self.client(provider).parse_response(data)

    def test_http_errors_do_not_expose_provider_body_headers_or_credentials(self):
        sensitive = FAKE_KEYS["ANTHROPIC_API_KEY"] + " PRIVATE-REPORT-TEXT"
        for provider in ("anthropic", "openai"):
            with self.subTest(provider=provider):
                opener = Mock()
                opener.open.side_effect = urllib.error.HTTPError(
                    "https://api.example.invalid/private", 401, sensitive,
                    {"Authorization": sensitive}, io.BytesIO(sensitive.encode()))
                with patch("workflow.providers.urllib.request.build_opener", return_value=opener):
                    with self.assertRaises(WorkflowError) as error:
                        self.client(provider).complete("Return JSON", "Assigned report")
                message = str(error.exception)
                self.assertIn("HTTP 401", message)
                self.assertNotIn(sensitive, message)
                self.assertNotIn("PRIVATE-REPORT-TEXT", message)
                self.assertNotIn("api.example.invalid/private", message)
                opener.open.assert_called_once()

    def test_transport_failure_is_sanitized_and_not_automatically_repeated(self):
        opener = Mock()
        opener.open.side_effect = urllib.error.URLError(FAKE_KEYS["OPENAI_API_KEY"] + " PRIVATE-REPORT-TEXT")
        with patch("workflow.providers.urllib.request.build_opener", return_value=opener):
            with self.assertRaises(WorkflowError) as error:
                self.client("openai").complete("Return JSON", "Assigned report")
        self.assertNotIn(FAKE_KEYS["OPENAI_API_KEY"], str(error.exception))
        self.assertNotIn("PRIVATE-REPORT-TEXT", str(error.exception))
        self.assertIn("not automatically repeated", str(error.exception))
        opener.open.assert_called_once()

    def test_non_json_http_response_has_safe_error(self):
        opener = Mock()
        opener.open.return_value = io.BytesIO(b"<html>PRIVATE-REPORT-TEXT</html>")
        with patch("workflow.providers.urllib.request.build_opener", return_value=opener):
            with self.assertRaisesRegex(WorkflowError, "non-JSON") as error:
                self.client("openai").complete("Return JSON", "Assigned report")
        self.assertNotIn("PRIVATE-REPORT-TEXT", str(error.exception))

    def test_provider_redirect_is_stopped_before_authentication_can_be_forwarded(self):
        handler = _NoRedirect()
        request = urllib.request.Request("https://api.anthropic.com/v1/messages",
                                         headers={"Authorization": "Bearer " + FAKE_KEYS["ANTHROPIC_API_KEY"]})
        with self.assertRaisesRegex(WorkflowError, "redirect") as error:
            handler.redirect_request(request, None, 302, "Found", {}, "https://unapproved.example/collect")
        self.assertNotIn(FAKE_KEYS["ANTHROPIC_API_KEY"], str(error.exception))


if __name__ == "__main__":
    unittest.main()
