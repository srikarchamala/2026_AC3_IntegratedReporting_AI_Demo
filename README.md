# Integrated Reporting with AI: Chatbot vs Agent

Demo materials for **"Bridging the AI Readiness Gap: A Five-Pillar Framework for Equitable Cancer Research"**, 9th Biennial African Caribbean Cancer Consortium (AC3) Conference, Bridgetown, Barbados, October 2026.

**Open the archived replay:** download [`index.html`](index.html) and open it in a browser. It displays the previously recorded workshop outputs offline. The executable workflow below generates new outputs.

> Everything here is a **synthetic teaching case**. No real patient data. Not for clinical use.

## Live source-grounded workflow

The new [`workflow/`](workflow/) implementation runs the same four component reports through **four independent report-specific extractors, one integrator, and one independent QA call**. It works with the OpenAI API or Anthropic API. Each call starts a fresh context.

| Stage | Implemented behavior |
|---|---|
| Extract | One shared extraction policy plus separate morphology, flow, cytogenetics, and molecular prompts and schemas. Preserve exact quotes, pages, missingness, methods, denominators, identifiers, and source-reported interpretations. |
| Retrieve guidance | Fetch approved public articles listed in [`workflow/sources.json`](workflow/sources.json), verify article identity and relevant sections, and save original bytes, passage text, source version, timestamp, and hashes. |
| Integrate | Match retrieved criteria to extracted findings, report unknown prerequisites, and attach finding and criterion IDs to report sentences. No case-answer rules or hand-written WHO medical thresholds are embedded in the new prompts. |
| Validate and review | Check schemas, quotations, source identity, reference IDs, and report structure; then run independent model QA. Render a reviewable HTML/Markdown draft with linked source evidence and visible QA flags. |

The default reference is the **public 2022 author overview of WHO fifth-edition myeloid classification**, with the complete relevant AML section and its tables. It is a bounded source, not a claim to access the full current WHO Blue Book. Optional ELN 2022 adult AML risk guidance is a separate reference enabled with `--include-risk`. Retrieval failures stop the workflow; there is no model-memory fallback. See the [source definitions](workflow/sources.json) and [architecture](docs/ARCHITECTURE.md).

### Run with an API

Requires Python 3.10+ and an API key for the chosen provider. A consumer chat subscription alone does not configure this runner.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

# These commands work without an API key:
python -m workflow prepare --out outputs/prepared-case
python -m workflow sources --out outputs/source-check
```

Set `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` in your local environment. Choose a model ID available to that API account and replace `YOUR_MODEL_ID` below. For an Anthropic key that is not scoped to a workspace, also set `ANTHROPIC_WORKSPACE_ID`.

```bash
# Claude / Anthropic
python -m workflow run --provider anthropic --model YOUR_MODEL_ID --out outputs/claude-agent

# Or OpenAI
python -m workflow run --provider openai --model YOUR_MODEL_ID --out outputs/openai-agent
```

Open `report.html` inside the selected output directory. It contains the draft, criterion assessments, linked findings, original quotations, retrieved guideline passages, and QA flags. The structured report is `integration.json`. Input text, prompts, responses, source snapshots, and model metadata are saved alongside it for inspection.

For the regular-chat comparison, run a fresh baseline with the **same provider and model**:

```bash
python -m workflow baseline --provider anthropic --model YOUR_MODEL_ID --out outputs/claude-baseline
python -m workflow validate --run-dir outputs/claude-agent
```

Use a new output directory each time. The `run` command retrieves its own sources; it does not silently reuse a prior preflight. Exit code `2` means high-severity review flags remain. Deterministic evidence failures stop before report rendering; model QA flags remain visible on the rendered draft. None of these checks establishes clinical correctness.

### Use regular ChatGPT or Claude chat

```bash
python -m workflow chat-pack --out outputs/chat-demo
```

Follow `outputs/chat-demo/START_HERE.md`. It packages exactly the four input PDFs and the new prompts. Use four fresh conversations for the four extraction steps, then fresh integration and QA conversations. This is manual orchestration; copying prompts into chat does not execute the Python checks or install a native skill.

For a short presentation, follow the [six-minute demo guide](docs/SOURCE_GROUNDED_DEMO.md). Prepare a successful run in advance, then show the baseline, one extraction, the retrieved source, the criteria table, and the final QA view. A prerecorded run should be identified as a replay.

### Development checks

```bash
python -m unittest discover -s tests -v
```

The tests use artificial model responses to check orchestration and failure handling. They do not measure model accuracy or clinical validity. Actual model execution requires your provider credentials.

## Original teaching case and archived results

The material below describes the original workshop artifacts. `prompts/agent_pipeline/`, `prompts/two_prompt_by_hand/`, `runs/`, the answer key, and the embedded data in `index.html` are historical. The new runner reads **only** `case/01` through `case/04` as case inputs and uses its own resources under `workflow/`; it never loads the guide, answer key, archived outputs, or condensed historical WHO rules.

### The case

One fictional patient, one bone marrow specimen, four separately issued reports (in [`case/`](case/)):

| Report | What only it shows |
|---|---|
| `01_bone_marrow_morphology.pdf` | Blasts 18% by manual count; monocytic lineage only "probable" |
| `02_flow_cytometry.pdf` | Blasts 22% by gated count; proves monocytic lineage |
| `03_cytogenetics_fish.pdf` | Normal karyotype 46,XY[20]; AML FISH panel negative |
| `04_molecular_ngs.pdf` | NPM1 (defining), FLT3-ITD, DNMT3A R882H (not classifying) |

No single report is enough. The diagnosis is **acute myeloid leukemia with mutated NPM1, with monocytic differentiation**. The built-in trap: DNMT3A is real and prognostic but belongs in the prognostic notes, not the diagnosis line. The pathologist-authored answer key is `case/05_GOLD_STANDARD_integrated_report.pdf`.

### Three archived approaches

| Approach | What it is | Prompts | Outputs |
|---|---|---|---|
| **Chatbot** | Attach the four reports, ask once | [`prompts/agent_pipeline/chatbot__DEFAULT_SYSTEM_PROMPT.txt`](prompts/agent_pipeline/) | [`runs/chatbot/`](runs/chatbot/) (3 runs) |
| **Two prompts by hand** | Extract with quotes, then integrate with a trace, in any chat tool | [`prompts/two_prompt_by_hand/`](prompts/two_prompt_by_hand/) | [`runs/two_prompt_by_hand/`](runs/two_prompt_by_hand/) |
| **Agent pipeline** | 12 steps: per-report extraction, cross-report analysis, parsers, WHO classifier, QA | [`prompts/agent_pipeline/`](prompts/agent_pipeline/) | [`runs/agent_pipeline/`](runs/agent_pipeline/) |

### Historical two-prompt exercise (no code)

You need any AI chat tool. Use only the synthetic files here, never patient data in a public tool.

1. Open a new chat. Attach the four PDFs from `case/`.
2. Paste the contents of `prompts/two_prompt_by_hand/prompt_extractor.txt`, then the contents of `schema_extractor_output.json`. Send.
3. You get one block of structured data (JSON). Every finding is tagged with its report and a quote.
4. Paste the contents of `prompt_integrator.txt`, then the JSON from step 3. Send.
5. You get the 11-section integrated report and an evidence trace: every sentence of the interpretation and diagnosis mapped to its source.
6. Compare with `case/05_GOLD_STANDARD_integrated_report.pdf`. Check the diagnosis line, both blast counts, and where DNMT3A landed. Run it again and see what changes.

### What happened in the recorded workshop runs

| Check | Chatbot (3 runs) | Agent pipeline | Two prompts |
|---|---|---|---|
| Diagnosis names NPM1 | 3 of 3 | Yes | Yes |
| DNMT3A kept out of the diagnosis | 0 of 3 | Yes | Yes |
| Diagnosis lines match the gold standard | 0 of 3 | Close (FLT3-ITD sent to prognostic notes) | Yes |
| Every sentence traced to a source report | No trace | 19 of 19 | 27 of 27 |
| Extracted quotes found in the source text | n/a | 61 of 61 | 33 of 33 |
| Lab names and accessions carried through | Yes | No (not in its extraction schema) | Yes |

The chatbot was usually close. The difference is that the structured versions can be checked.

**How these runs were made:** all three approaches used Claude with the prompts in this repo, one fresh call per step. The live workshop below ran on a different model, so wording differs.

## From demo to practice

A real deployment brings the model to the data: an on-premises or contractually walled-off model, fed by the lab information system rather than PDFs, producing a draft a pathologist reviews and signs, validated and governed like any other clinical tool. See Part 3 of `case/00_DEMO_GUIDE.pdf`.

## Credits

The synthetic case, the two-prompt pipeline, the gold standard and the agent pipeline come from the **Agentic Pathology Workshop**, API Summit 2026: [github.com/hesamhakim/agentic-pathology-workshop](https://github.com/hesamhakim/agentic-pathology-workshop)

- Hesam H. Javadi, PhD (Medical College of Wisconsin, Children's Wisconsin): workshop infrastructure, LangFlow components
- Srikar Chamala, PhD (Children's Hospital Los Angeles, USC Keck School of Medicine)
- Omar Baba, MD (Henry Ford Health): AML case design, gold standard, two-stage prompts

Workshop materials are used under the MIT License; see [`LICENSE-workshop-materials`](LICENSE-workshop-materials).

Contact: Srikar Chamala, schamala@chla.usc.edu
