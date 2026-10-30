"""Small stateless HTTP adapters. Provider credentials never enter prompts/files."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass

from .common import WorkflowError


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise WorkflowError("Unexpected provider redirect; request was stopped.")


@dataclass
class ModelResult:
    text: str
    metadata: dict


class ModelClient:
    """Each call starts a fresh context; no previous response/session is reused."""

    def __init__(self, provider: str, model: str, max_output_tokens: int = 16000,
                 timeout: int = 180):
        if provider not in {"anthropic", "openai"}:
            raise WorkflowError("Provider must be anthropic or openai.")
        if not model or max_output_tokens < 1 or timeout < 1:
            raise WorkflowError("Model ID, positive output-token limit, and positive timeout are required.")
        self.provider, self.model = provider, model
        self.max_output_tokens, self.timeout = max_output_tokens, timeout
        env_name = "ANTHROPIC_API_KEY" if provider == "anthropic" else "OPENAI_API_KEY"
        self._key = os.environ.get(env_name, "").strip()
        self._workspace_id = os.environ.get("ANTHROPIC_WORKSPACE_ID", "").strip() if provider == "anthropic" else ""
        if not self._key:
            raise WorkflowError(f"Set {env_name} in your local environment before running model calls. Do not paste it into chat.")

    def request_data(self, system: str, user: str, json_output: bool = True) -> tuple:
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self._key}"}
        if self.provider == "anthropic":
            headers["anthropic-version"] = "2026-10-21"
            if self._workspace_id:
                headers["anthropic-workspace-id"] = self._workspace_id
            body = {"model": self.model, "max_tokens": self.max_output_tokens,
                    "system": system, "messages": [{"role": "user", "content": user}],
                    "stream": False}
            return "https://api.anthropic.com/v1/messages", headers, body
        body = {"model": self.model, "instructions": system, "input": user,
                "max_output_tokens": self.max_output_tokens, "store": False}
        if json_output:
            # Our full local schemas use keywords outside provider strict-output
            # subsets. JSON mode plus local validation keeps the entire contract.
            body["text"] = {"format": {"type": "json_object"}}
        return "https://api.openai.com/v1/responses", headers, body

    def complete(self, system: str, user: str, json_output: bool = True) -> ModelResult:
        url, headers, body = self.request_data(system, user, json_output)
        request = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
        opener = urllib.request.build_opener(_NoRedirect())
        for attempt in range(3):
            try:
                with opener.open(request, timeout=self.timeout) as response:
                    raw = response.read(16 * 1024 * 1024 + 1)
                if len(raw) > 16 * 1024 * 1024:
                    raise WorkflowError("Provider response exceeded the response-size limit.")
                return self.parse_response(json.loads(raw))
            except urllib.error.HTTPError as exc:
                if exc.code in {429, 500, 502, 503, 504} and attempt < 2:
                    time.sleep(2 ** (attempt + 1))
                    continue
                # Do not echo provider bodies or headers: they can contain input
                # content, request details, or credentials.
                workspace_hint = " Set ANTHROPIC_WORKSPACE_ID if your key is not workspace-scoped." if self.provider == "anthropic" else ""
                raise WorkflowError(f"{self.provider} returned HTTP {exc.code}. Check model access, API version, quota and credentials." + workspace_hint) from exc
            except (urllib.error.URLError, TimeoutError) as exc:
                raise WorkflowError(f"{self.provider} request failed or timed out. The request was not automatically repeated.") from exc
            except json.JSONDecodeError as exc:
                raise WorkflowError("Provider returned a non-JSON HTTP response.") from exc
        raise WorkflowError("Provider retries exhausted.")

    def parse_response(self, data: dict) -> ModelResult:
        if self.provider == "anthropic":
            if data.get("stop_reason") != "end_turn" or (data.get("stop_details") or {}).get("type") == "refusal":
                raise WorkflowError("Claude did not finish a normal response (possibly refused or truncated). No output was accepted.")
            parts = [x["text"] for x in data.get("content", []) if x.get("type") == "text"]
            api_version = "2026-10-21"
        else:
            if data.get("status") != "completed":
                raise WorkflowError("OpenAI did not complete the response (possibly truncated). No output was accepted.")
            blocks = [block for item in data.get("output", []) if item.get("type") == "message"
                      for block in item.get("content", [])]
            if any(block.get("type") == "refusal" for block in blocks):
                raise WorkflowError("OpenAI refused the request. No output was accepted.")
            parts = [block["text"] for block in blocks if block.get("type") == "output_text"]
            api_version = "responses-v1"
        text = "\n".join(parts).strip()
        if not text:
            raise WorkflowError("Provider returned no usable text.")
        return ModelResult(text, {"provider": self.provider, "requested_model": self.model,
                                  "returned_model": data.get("model"), "response_id": data.get("id"),
                                  "api_version": api_version, "usage": data.get("usage", {})})
