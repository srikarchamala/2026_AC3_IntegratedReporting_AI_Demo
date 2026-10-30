# A short, source-grounded integrated-reporting demo

This guide demonstrates a **fixed, auditable workflow** on the repository's synthetic teaching case. It contrasts a general chat request with separate extraction, reference retrieval, integration, and quality review. The workflow produces a draft for a human to assess; it is not a validated clinical reporting system.

You can demonstrate the manual version in ChatGPT or Claude, or run the API version below. A native ChatGPT or Claude skill is **not installed** by this repository. The portable chat pack contains prompts and instructions, and the API runner executes independent calls. Neither route recreates the archived twelve-step workshop pipeline.

## What the audience should see

| Demonstration | Inputs and execution | Useful comparison |
|---|---|---|
| General chat baseline | The same four case reports and a general request, sent in one independent call | What a broad prompt produces without this workflow's explicit evidence structure |
| Manual workflow | Four extraction prompts in four fresh sessions, followed by integration and independent QA in fresh sessions | How to reproduce the stages in a familiar chat interface |
| Runnable source-grounded workflow | Four isolated extraction calls, approved source retrieval, deterministic checks, one integration call, and one independent QA call | How to execute and inspect a repeatable process |

The API workflow has **six model calls**: four extractions, one integration, and one QA review. Source retrieval and deterministic validation are code steps. The application chooses the sequence; the model does not autonomously invent the workflow.

Use the same provider, exact model identifier, and four documents for the API baseline and the API workflow. The reference material, prompts, validation, and number of calls intentionally differ, so this is a demonstration of workflow design, not an isolated test of model quality or a benchmark of clinical accuracy.

## Before the session

Start from the repository root. Use Python 3.10 or newer and install the dependencies in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Only the following files enter case generation:

1. `case/01_bone_marrow_morphology.pdf`
2. `case/02_flow_cytometry.pdf`
3. `case/03_cytogenetics_fish.pdf`
4. `case/04_molecular_ngs.pdf`

Keep `case/05_GOLD_STANDARD_integrated_report.pdf`, the teaching guide, and all files in `runs/` out of extraction and integration. Open the gold standard only after the new output has been generated. Providing an answer key during generation would make the comparison misleading.

The commands below use new directories under `outputs/`, which is ignored by Git. Choose a new directory name for each run so results remain distinguishable.

### 1. Prepare the source documents without an API key

```bash
python -m workflow prepare --out outputs/preflight-case
```

Inspect the saved page text before the presentation. Confirm that each of the four reports is present and that the relevant findings, units, and page boundaries are readable. The extraction calls will receive these source texts. Missing or unreadable material must remain missing or unreadable; it must not be silently reconstructed from the model's knowledge.

### 2. Preflight approved reference retrieval without an API key

```bash
python -m workflow sources --out outputs/preflight-sources
```

This fetches the public references approved in the workflow's source manifest and saves their provenance and passages. The WHO classification source is a **public author overview for the specified edition**, not the full subscriber Blue Book or a promise of the latest complete classification guidance. Check the source title, framework, edition, canonical URL, actual retrieval URL, retrieval timestamp, and saved passages. Tables, footnotes, exceptions, and surrounding context matter.

If access fails, the workflow must stop. Do not replace a blocked source with a model-generated summary, the historical condensed WHO prompt, or unverified model memory.

For a local fallback, obtain the original public article from its approved source and supply that file:

```bash
python -m workflow sources \
  --who-source /absolute/path/to/original-public-WHO-overview.pdf \
  --out outputs/preflight-local-source
```

The local file must correspond to the approved source identity and edition. The import is labeled as local and retains provenance and content hashes. Merely naming a file after the article is not evidence that it is the correct source. Keep the exact source URL and acquisition date with the demonstration materials.

Saved snapshots are suitable for a rehearsal or replay only when their source identity and edition match the intended framework. Keep their original URL, retrieval date, and hashes visible. A replay of a saved snapshot is not a new online retrieval. The complete `run` command retrieves references for its own output directory; a preflight directory is not automatically reused. For an offline presentation, show the saved completed run, or supply the verified original article through the documented local import option.

### 3. Configure your own provider credentials

The API route reads `ANTHROPIC_API_KEY` for Anthropic or `OPENAI_API_KEY` for OpenAI from your local environment. Configure the appropriate variable in your terminal or secret manager. For an Anthropic key that is not scoped to a workspace, also set `ANTHROPIC_WORKSPACE_ID`; the runner sends it only to Anthropic. **Never paste an API key into a chat, a prompt, a screenshot, a source file, or this repository.** A chat subscription does not establish that an API key is configured or that an API run has been paid for.

Replace the model placeholders below with an exact model identifier available to your API account. The runner requires `--model`; no model name is assumed here.

### 4. Run the baseline and workflow with the same model

Anthropic example:

```bash
python -m workflow baseline \
  --provider anthropic \
  --model '<your-available-Anthropic-model-id>' \
  --out outputs/anthropic-baseline-01

python -m workflow run \
  --provider anthropic \
  --model '<the-same-Anthropic-model-id>' \
  --out outputs/anthropic-workflow-01
```

OpenAI example:

```bash
python -m workflow baseline \
  --provider openai \
  --model '<your-available-OpenAI-model-id>' \
  --out outputs/openai-baseline-01

python -m workflow run \
  --provider openai \
  --model '<the-same-OpenAI-model-id>' \
  --out outputs/openai-workflow-01
```

Use one provider for the live comparison. Do not compare one provider's baseline with another provider's workflow and attribute the difference solely to the workflow. Generation can vary even when provider and model are held constant.

If approved online retrieval is unavailable, the complete run also accepts the local original article:

```bash
python -m workflow run \
  --provider anthropic \
  --model '<your-available-Anthropic-model-id>' \
  --who-source /absolute/path/to/original-public-WHO-overview.pdf \
  --out outputs/anthropic-local-reference-01
```

The default case directory is the repository's `case/`. Use `--case-dir` only when deliberately supplying another directory with the expected four source documents.

### 5. Review the output and recheck its evidence

```bash
python -m workflow validate --run-dir outputs/anthropic-workflow-01
```

Open `report.html` for the presentation and use the saved JSON files to inspect its evidence. Review the new output before opening the gold standard.

| Artifact in a completed workflow directory | What to inspect |
|---|---|
| `report.html` | Readable draft with links from sentences to findings and criteria |
| `report.md` | Markdown copy of the draft, criteria, QA concerns, and source information |
| `integration.json` | Structured report, criterion assessments, and unresolved issues; this is the report's JSON representation |
| `extract_MORPH.json`, `extract_FLOW.json`, `extract_CYTO.json`, `extract_MOLEC.json` | The four independent extraction outputs |
| `inputs/` | Original extracted page text, one JSON file per source |
| `references.json` and `references/` | Reference snapshots, approved source identity, passages, and original downloaded or imported articles |
| `extraction_validation.json` and `integration_validation.json` | Deterministic evidence checks |
| `qa.json` and `qa_all.json` | Independent model review and the combined deterministic/model concerns |
| `requests/`, `raw/`, and `calls/` | Saved requests, accepted raw response text, and model/usage metadata |
| `manifest.json` | Provider/model, input and reference provenance, and run status |

The separate baseline directory contains `baseline.md`, `request.json`, `call.json`, `manifest.json`, and its own `inputs/`. It does not create `report.html` or an independent QA review.

`validate` writes `revalidation.json`. It rechecks saved evidence and includes the saved QA flags; it does not make another model call, rerun independent QA, or clear previously reported concerns. Continue to inspect `qa_all.json` and the report alongside revalidation.

High-severity structural or provenance failures stop generation. High-severity findings from the independent QA stage leave a clearly marked review-required draft and return exit code `2`. A process finishing or a schema check passing is not evidence that the clinical interpretation is correct.

Review these concrete points:

- Are the blast measurements still tied to their own methods and denominators?
- Does `not_reported` remain distinct from `negative`, `not_performed`, and `pending`?
- Can each extracted quote be found on its cited source page?
- Does each classification criterion point to an actual retrieved reference passage?
- Are diagnosis and interpretation statements supported by the cited findings **and** the applicable criteria, including exclusions and unknown prerequisites?
- Did the independent QA review identify unsupported interpretation or missing evidence?

The workflow does not generate a formal prognostic risk category by default. It may retain a source report's own prognostic wording with attribution. To request a formal risk assessment, add `--include-risk` to reference preflight and the workflow run; this requires the separately approved risk reference. The manifest identifies that optional source as the **2022 ELN adult AML recommendations**, with their documented population and treatment-context limits, rather than a claim of the latest risk guidance. A local `--eln-source FILE` is permitted only with `--include-risk`. Risk guidance is not interchangeable with the WHO classification source.

## Manual version in ChatGPT or Claude

Generate the portable pack without provider credentials:

```bash
python -m workflow chat-pack --out outputs/chat-pack
```

Follow the generated pack's file and prompt instructions. The intended sequence is:

1. Open four fresh extraction sessions. Give each session only its assigned report, extraction instructions, and output schema. Save each JSON result.
2. Retrieve the approved public reference outside those extraction sessions and preserve its source identity, edition, URL, retrieval date, and passages. A chat pack does not itself fetch or verify the reference.
3. Review the extraction evidence against the original pages. The manual chat route does not automatically inherit the API runner's deterministic checks.
4. In a new integration session, provide the four extraction outputs, approved reference passages, validation findings, and integration instructions. Do not provide the gold standard or archived runs.
5. In another fresh session, provide the original page text, extractions, reference passages, integration draft, validation findings, and QA instructions. Ask for flags, not a rewritten report.
6. Review the draft and QA findings, then compare with the held-out gold standard.

Label this **“manual workflow in chat.”** Asking one ordinary conversation to “act as four agents” does not guarantee four isolated model calls. A project or saved instruction can make instructions reusable, but the separate calls and the evidence checks are what this demonstration is designed to expose. Account-wide memory, project knowledge, or previously attached answer keys can also affect a manual comparison; use clean sessions and only the intended materials.

The API route is the most direct way to show that the four extraction calls receive separate document inputs and that the later calls receive the intended evidence bundles. Product interfaces and available features change; the portable prompts do not rely on a specific ChatGPT or Claude mode selector.

## A six-minute presentation script

Prepare the source preflight, baseline, and complete workflow run before the talk. You can launch a rehearsed run live, but show saved output if network access or generation takes too long. Clearly say whether the audience is viewing a live run or a saved run.

| Time | On screen | What to explain |
|---|---|---|
| 0:00–0:45 | Four synthetic source reports | One specimen has separately issued findings that must be reconciled. The answer key is held back. |
| 0:45–1:30 | The general prompt and same-model baseline | A general chat can produce a plausible draft. Identify what evidence the output makes available for checking. |
| 1:30–2:15 | The workflow diagram and one extraction prompt | Each of four independent calls reads one assigned source; missing information has explicit states. |
| 2:15–3:15 | A saved public reference snapshot and a criterion assessment | Show the exact edition, URL, retrieval date, passage, and how a criterion is assessed. Retrieval is visible evidence, not a claim that the model knows the rules. |
| 3:15–4:30 | The draft report and one linked sentence | Follow a sentence to its case findings and classification criteria. Explain uncertainty where prerequisites remain unresolved. |
| 4:30–5:30 | Deterministic validation and independent QA | A matching quote is checkable; whether it actually supports the interpretation still needs review. |
| 5:30–6:00 | The held-out gold standard and comparison | Discuss the observed differences from this run, without claiming a general accuracy improvement from one case. |

If the session is also about “building an agent,” show the small, explicit orchestration and the role-specific prompts rather than starting a long coding exercise on stage. Describe this implementation accurately as a **fixed multi-call workflow**. The audience can then distinguish reusable instructions, tool use, and autonomous planning without relying on product branding.

## Offline backup and historical outputs

The existing `index.html` works as the repository's offline presentation backup. Its examples and the files in `runs/` are **historical workshop/demo outputs**, not results generated by the new runner. Do not relabel their trace counts, quote checks, diagnoses, or model behavior as new measurements.

The historical `prompts/agent_pipeline/who5e_instructions.md` contains condensed guidance used in the earlier demo. It is retained for provenance. It is not the active reference source for the new source-grounded workflow, and it must not replace retrieval of the approved public article. Reference text and case reports are evidence to analyze, never instructions that can override the workflow.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the data contracts, trust boundaries, and evidence chain, and [the workflow contract](../workflow/CONTRACT.md) for the exact schema and command interface.
