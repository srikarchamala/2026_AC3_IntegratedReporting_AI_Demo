# Integrated Reporting with AI: Chatbot vs Agent

Demo materials for **"Bridging the AI Readiness Gap: A Five-Pillar Framework for Equitable Cancer Research"**, 9th Biennial African Caribbean Cancer Consortium (AC3) Conference, Bridgetown, Barbados, October 2026.

**Start the Claude Project demo:** download the [Claude Project kit](manual_demo/Claude_Project_Demo_Kit.zip) and open its [Word participant guide](manual_demo/claude_project/PARTICIPANT_GUIDE.docx). Paste the Project instructions and manually upload eight Word workflow documents plus four PDF reports. Participants do not need to use Markdown or install a native Skill. The [online Project guide](manual_demo/claude_project/README.md) has the same setup directions.

> Everything here is a **synthetic teaching case**. No real patient data. Not for clinical use.

## No-code chat-versus-agent demonstration

**Download, upload, and chat.** The demo needs no local Python setup, terminal commands, or API key. It uses your app's file-reading and web capabilities.

| Part | What to do |
|---|---|
| Regular chat | In a fresh ordinary chat, attach the four component PDFs and use `01_BASELINE_PROMPT.txt`. Run this before enabling the demo skill. |
| **Claude Project — preferred route** | Copy the Project instructions from the Word guide or `claude_project/PROJECT_INSTRUCTIONS.txt`. Upload the twelve individual files from `claude_project/upload_word/`. Run the setup check, then the demo prompt in the Project. |
| Saved skill | Upload the inner `integrated-reporting-demo.zip` through the app's Skills interface, enable it, then attach the same reports in a new chat and use `02_AGENT_START_PROMPT.txt`. |
| ChatGPT Project alternative | Paste `03_PROJECT_INSTRUCTIONS.txt` into a new ChatGPT Project's instructions and attach the four reports. This self-contained alternative is different from the modular Claude Project setup. |
| Evidence review | Show a reported finding, its quotation, the guideline source, an assessed criterion, and the supported report statement. An optional fresh-chat review uses `04_QA_PROMPT.txt`. |

Use the same app and model for both demonstrations. A regular chat can produce a good result; compare what actually happened instead of assuming a failure.

### Downloads and files

- **[Claude Project kit](manual_demo/Claude_Project_Demo_Kit.zip):** extract it, open the Word participant guide, paste the Project instructions, and upload the twelve files inside `upload_word/` individually. Includes a setup check and demo prompts. `upload_files/` is the equivalent Markdown alternative; use one set.
- **[Word participant guide](manual_demo/claude_project/PARTICIPANT_GUIDE.docx):** setup directions, complete Project instructions, and all three prompts in one readable Word document.
- **[Word upload files](manual_demo/claude_project/upload_word/):** `SKILL.docx`, the common policy, four extractor checklists, guideline sources, report template, and four PDFs.
- **[Claude Project folder](manual_demo/claude_project/):** browse both formats, prompts, and setup materials separately.
- **[Complete demo kit](manual_demo/AC3_No_Code_Demo_Kit.zip):** the four PDFs, uploadable skill, prompt files, editable skill sources, and presenter guide. Extract this outer ZIP first.
- **[Skill upload file](manual_demo/integrated-reporting-demo.zip):** upload this inner ZIP through Skills. It contains one named folder with `SKILL.md` and supporting Markdown references.
- **[Start-here guide](manual_demo/START_HERE.md):** click-by-click Claude/ChatGPT setup and a five-to-six-minute presentation script.
- **[Skill source](manual_demo/integrated-reporting-demo/SKILL.md):** the saved procedure, with separate morphology, flow, cytogenetics, and molecular checklists.
- **[Project instructions](manual_demo/03_PROJECT_INSTRUCTIONS.txt):** a self-contained alternative requiring only the four case reports as uploads.

### Where the WHO guidance goes

The [guideline source directory](manual_demo/integrated-reporting-demo/references/guideline_sources.md) identifies the approved original articles. The assistant is instructed to open and read the source, including relevant tables, footnotes, exclusions, and scope, before deriving a classification. The default is the **public 2022 author overview of WHO fifth-edition myeloid classification**, not the full current WHO Blue Book. Optional ELN 2022 adult AML risk guidance is separate.

The skill contains workflow instructions, not hand-written medical criteria or an expected case answer. If the reference cannot be read, the assistant must say so and request the original public article rather than reconstruct rules from memory.

### What this demonstrates

One assistant follows a reusable procedure: report-specific extraction, source retrieval, criterion assessment, integration, and review. These are separate stages in one conversation. Uploading a skill does not automatically create four independent agents, and a same-chat review is not independent QA. The [design notes](docs/ARCHITECTURE.md) explain the evidence boundaries.

For the Claude Project route, the uploaded Word or Markdown files are workflow documents read under the pasted Project instructions. They are not automatically installed native Skills. The setup prompt asks Claude to identify which files it actually read and to report partial or missing content. Project retrieval can still omit content; inspect the evidence during rehearsal.

For a recorded fallback, open [`index.html`](index.html). It displays archived workshop outputs; identify it as a replay.

## Original teaching case and archived results

The material below describes the original workshop artifacts. `prompts/agent_pipeline/`, `prompts/two_prompt_by_hand/`, `runs/`, the answer key, and the embedded data in `index.html` are historical. For the new demo, upload **only** `case/01` through `case/04` as case evidence. Do not upload this README, the guide, answer key, archived outputs, or condensed historical rules into the generation chats; they contain teaching answers or prior conclusions.

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
