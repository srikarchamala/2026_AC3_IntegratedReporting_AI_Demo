# Integrated Reporting with AI: Regular Chat vs a Guided Workflow

Demo materials for **"Bridging the AI Readiness Gap: A Five-Pillar Framework for Equitable Cancer Research"**, 9th Biennial African Caribbean Cancer Consortium (AC3) Conference, Bridgetown, Barbados, October 2026.

You give the same four pathology reports to Claude twice:

1. **Regular chat:** attach the reports and ask once.
2. **Claude Project:** the same model, plus written instructions and a reference to the WHO classification. It extracts each report with quotes, reads the guideline, checks criteria, drafts the report, and reviews it.

Then you compare what you can *check* in each answer. No coding, no API key, no software to install.

> **Synthetic teaching case only.** The patient and all reports are fictional. Never put real patient information into a consumer AI tool. Outputs are teaching drafts, not clinical reports.

---

## What you need

- A Claude account that can create **Projects** ([claude.ai/projects](https://claude.ai/projects)).
- About **20 minutes** the first time.
- The demo kit: **[Claude_Project_Demo_Kit.zip](manual_demo/Claude_Project_Demo_Kit.zip)** (on that page, click the download button).

## Step 1: Download and unzip the kit

Unzip `Claude_Project_Demo_Kit.zip`. Inside you will find:

| File or folder | What it is | Upload it? |
|---|---|---|
| `upload_word/` | 8 Word workflow documents + 4 PDF reports (12 files) | **Yes**, into the Project (step 3) |
| `upload_files/` | The same 8 workflow documents as Markdown, plus the same 4 PDFs | Only if you prefer Markdown. Use **one** set, never both |
| `PROJECT_INSTRUCTIONS.txt` | Text you paste into the Project's instructions | Paste, don't upload |
| `BASELINE_PROMPT.txt` | Prompt for the regular chat (step 2) | Paste |
| `CHECK_SETUP_PROMPT.txt` | Prompt that checks Claude can read every file (step 4) | Paste |
| `RUN_DEMO_PROMPT.txt` | Prompt that runs the workflow (step 5) | Paste |
| `PARTICIPANT_GUIDE.docx` | All of the above in one Word document | Keep for yourself; **don't upload** |

Every upload file is named for its job: `Skills_1` to `Skills_8` are the instructions, in the order Claude uses them, and `CASE_01` to `CASE_04` are the four reports. Both folders hold the same four reports.

## Step 2: Run the regular chat first

Do this **before** you create the Project, so nothing from the Project influences it.

1. Open a **new chat** at [claude.ai](https://claude.ai), **outside** any Project.
2. If your chat has a Memory option in the **+** menu, turn it off for this chat.
3. Attach the **four `CASE_` PDFs** from `upload_word/` (paperclip or **+** → upload). Attach nothing else.
4. Paste the contents of `BASELINE_PROMPT.txt` and send.
5. Save the answer (copy it into a document, or leave the tab open).

Note the model you used (shown near the message box). Use the same model in step 5.

## Step 3: Create the Project

1. Go to [claude.ai/projects](https://claude.ai/projects) and click **+ New Project**.
2. Name it `AC3 Integrated Reporting Demo`. Keep it private.
3. Click **Set project instructions**. Paste the **entire** contents of `PROJECT_INSTRUCTIONS.txt` and click **Save instructions**.
   Put it in the instructions box, not in the Project description.
4. In the Project's **Files** (project knowledge) area, click **+** and upload all **12 files** from `upload_word/`. You can select them together.
5. Check that the Project lists 12 files: 8 starting `Skills_` and 4 starting `CASE_`.

### What the 12 files are

They fall into four groups. Together they work like a written procedure handed to a new colleague, plus the case to work on.

**The procedure (1 file)**

| File | What it does |
|---|---|
| `Skills_1_procedure.docx` | The master procedure. Lists the six stages (inventory, extraction, guideline, criteria, draft, review), the evidence rules, and which other file to use at each stage |

**How to read each report (5 files)**

| File | What it does |
|---|---|
| `Skills_2_extraction_rules_all_reports.docx` | Rules for every report: quote the exact words, record where they came from, keep units and methods, and treat "not reported" as unknown, never as negative |
| `Skills_3_checklist_morphology.docx` | Checklist for the bone marrow morphology report: cellularity, blast and monocyte counts kept separate, lineage wording, cytochemistry |
| `Skills_4_checklist_flow_cytometry.docx` | Checklist for the flow cytometry report: each cell population and its percentage, gating, markers, lineage wording |
| `Skills_5_checklist_cytogenetics_FISH.docx` | Checklist for the cytogenetics and FISH report: exact karyotype, each FISH probe and result, and the limits of a targeted panel |
| `Skills_6_checklist_molecular.docx` | Checklist for the molecular (NGS) report: each variant with its transcript, allele fraction and tier, what was tested, and assay limits |

**Where the rules come from and how to write it up (2 files)**

| File | What it does |
|---|---|
| `Skills_7_guideline_sources.docx` | Points to the WHO 5th edition myeloid article (and optional ELN 2022 risk guidance) that Claude must open and read. It holds addresses and scope only, not the rules themselves, and no answer |
| `Skills_8_report_template.docx` | The output format: extraction tables, criteria table, the 11-section report, and the review table |

**The case (4 files)**

| File | What it is |
|---|---|
| `CASE_01_bone_marrow_morphology.pdf` | Synthetic morphology report (MORPH) |
| `CASE_02_flow_cytometry.pdf` | Synthetic flow cytometry report (FLOW) |
| `CASE_03_cytogenetics_fish.pdf` | Synthetic karyotype and FISH report (CYTO) |
| `CASE_04_molecular_ngs.pdf` | Synthetic molecular NGS report from a separate reference lab (MOLEC) |

The 8 workflow files contain no diagnosis or expected answer, and none of them are the guideline itself; Claude reads the WHO article separately in step 5. The `upload_files/` folder has the same 8 workflow files as Markdown (`.md`) if you prefer them.

Do **not** upload the answer key (`case/05_GOLD_STANDARD_integrated_report.pdf`), this README, the participant guide, or anything from `runs/`. They contain the expected answer and would make the comparison unfair.

## Step 4: Check that Claude can read every file

1. Start a **new chat inside the Project**.
2. Paste the contents of `CHECK_SETUP_PROMPT.txt` and send.
3. Claude returns a table with one row per file and a status: **READ**, **PARTIAL**, **MISSING** or **UNREADABLE**.
4. It should end with **"File setup ready for the workflow."**

If it says **"File setup incomplete"**, re-upload the files it names and run the check again. This check does not diagnose anything; it only confirms the files are readable.

## Step 5: Run the workflow

1. In the same Project chat, turn on **Web search** if your **+** menu offers it. (Some newer layouts search automatically and have no switch.)
2. Paste the contents of `RUN_DEMO_PROMPT.txt` and send.
3. Wait. The full run usually takes **several minutes** and produces a long answer.

Claude works through six labelled stages:

| Stage | What you should see |
|---|---|
| 1. Inventory | The four reports matched to MORPH, FLOW, CYTO, MOLEC, with accessions and an identity check |
| 2. Extraction | Four tables. Each finding has an ID (e.g. `MOLEC-003`) and an exact quote from its report |
| 3. Guideline | A **source card** for the WHO 5th edition article it actually opened, with what it read |
| 4. Criteria | A table of WHO criteria marked met / not met / unknown, each citing finding IDs |
| 5. Draft | An 11-section integrated report. Statements cite findings, e.g. `[MOLEC-003; C2]` |
| 6. Review | A table of concerns by severity. Open issues stay visible |

**If Claude says it could not open the WHO article:** download the open-access PDF from [PubMed Central (PMC9252913)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9252913/), attach it to the chat, and ask Claude to continue using the uploaded article. It will label it as an uploaded source.

## Step 6: Compare the two answers

Put the regular-chat answer (step 2) next to the Project answer (step 5) and check:

| Question | Where to look |
|---|---|
| Does the diagnosis name the defining mutation (NPM1)? | Diagnosis line in both |
| Is **DNMT3A** in the diagnosis line? It shouldn't be: it is prognostic, not classifying | Diagnosis line in both |
| Are both blast counts (18% morphology, 22% flow) named and reconciled? | Interpretation in both |
| Can you tell which report each statement came from? | Regular chat: usually no. Project: finding IDs and quotes |
| Which classification source was used, and which part of it? | Project: source card and criteria table |
| What is still uncertain? | Project: review table |

The regular chat may produce a good answer. The point is not that it is wrong, but that you can't easily check it.

**Only after both runs**, open the pathologist-written answer key, [`case/05_GOLD_STANDARD_integrated_report.pdf`](case/05_GOLD_STANDARD_integrated_report.pdf), and compare the diagnosis lines. Run the regular chat again in a fresh chat and see what changes between runs.

## Troubleshooting

| Problem | What to do |
|---|---|
| Setup check shows PARTIAL or MISSING | Re-upload that file. Project search sometimes reads only parts of a document; run the check again |
| Claude asks you to run code or give an API key | You don't need to. Reply: "Continue using only the uploaded files and the web, no code." |
| Classification paused, WHO article not read | Attach the PMC PDF (link in step 5) and ask Claude to continue |
| Answer is too long to present | Ask: "Show only the opening summary, one extraction row with its quote, the source card, and the review table." |
| Claude mentions the answer key or earlier results | You uploaded extra files. Remove them, start a new Project chat, and rerun |
| Results differ between runs | Expected. AI output varies; that is part of what the demo shows |

## What this does and doesn't show

- It is **one assistant following written stages**, not several independent agents. The review stage is the same assistant checking its own work, not independent quality control.
- The WHO source is the public **2022 author overview** of the WHO 5th edition myeloid classification (Khoury et al., [doi:10.1038/s41375-022-01613-1](https://doi.org/10.1038/s41375-022-01613-1)), not the full WHO Blue Book.
- A real deployment would bring the model to the data: an approved model inside the institution, fed by the laboratory information system rather than PDFs, producing a draft a pathologist reviews and signs, validated and governed like any other clinical tool. See Part 3 of [`case/00_DEMO_GUIDE.pdf`](case/00_DEMO_GUIDE.pdf).

---

## About the case

> **Spoiler:** this section contains the expected answer. Don't upload it to Claude.

One fictional 58-year-old patient, one bone marrow specimen, four reports from different laboratories ([`case/`](case/)):

| Report | What only it shows |
|---|---|
| `01_bone_marrow_morphology.pdf` | Blasts 18% by manual count; monocytic lineage only "probable" |
| `02_flow_cytometry.pdf` | Blasts 22% by gated count; confirms monocytic lineage |
| `03_cytogenetics_fish.pdf` | Normal karyotype 46,XY[20]; AML FISH panel negative |
| `04_molecular_ngs.pdf` | NPM1 (disease-defining), FLT3-ITD, DNMT3A R882H (not classifying) |

No single report is enough. The pathologist-authored answer is **acute myeloid leukemia with mutated NPM1, with monocytic differentiation; FLT3-ITD present; normal karyotype** ([`case/05_GOLD_STANDARD_integrated_report.pdf`](case/05_GOLD_STANDARD_integrated_report.pdf)). The built-in trap: DNMT3A is real and prognostically relevant but belongs in the prognostic notes, not the diagnosis line.

## Other ways to run it

| Route | When to use it | Files |
|---|---|---|
| **Claude native Skill** | Your account allows uploading Skills (Settings → Capabilities → code execution/file creation on) | Upload [`manual_demo/integrated-reporting-demo.zip`](manual_demo/integrated-reporting-demo.zip) as a Skill; see [`START_HERE.md`](manual_demo/START_HERE.md) |
| **ChatGPT Project** | You use ChatGPT | Paste [`manual_demo/03_PROJECT_INSTRUCTIONS.txt`](manual_demo/03_PROJECT_INSTRUCTIONS.txt) into Project instructions; upload the four PDFs; use [`02_AGENT_START_PROMPT.txt`](manual_demo/02_AGENT_START_PROMPT.txt) |
| **Two prompts by hand** | Any chat tool, simplest version | Step 1: attach the four PDFs and paste [`prompt_extractor.txt`](prompts/two_prompt_by_hand/prompt_extractor.txt) + [`schema_extractor_output.json`](prompts/two_prompt_by_hand/schema_extractor_output.json). Step 2: paste [`prompt_integrator.txt`](prompts/two_prompt_by_hand/prompt_integrator.txt) + the JSON from step 1 |

## Example runs (for reference)

[`index.html`](index.html) is an offline, click-through page (download it and open it in a browser) showing example outputs on this case: three regular-chat runs, the 12-step agent pipeline from the API Summit workshop, and the two-prompt version, scored against the answer key. These are **rehearsal runs made with Claude on 29–30 October 2026 using the workshop's prompts**, not outputs from the original workshop. Raw outputs are in [`runs/`](runs/) and the prompts in [`prompts/`](prompts/).

| Check | Regular chat (3 runs) | Agent pipeline | Two prompts |
|---|---|---|---|
| Diagnosis names NPM1 | 3 of 3 | Yes | Yes |
| DNMT3A kept out of the diagnosis | 0 of 3 | Yes | Yes |
| Diagnosis lines match the answer key | 0 of 3 | Close (FLT3-ITD sent to prognostic notes) | Yes |
| Every sentence traced to a source report | No trace | 19 of 19 | 27 of 27 |
| Extracted quotes found in the source text | n/a | 61 of 61 | 33 of 33 |
| Lab names and accessions carried through | Yes | No (not in its extraction schema) | Yes |

`prompts/agent_pipeline/who5e_instructions.md` is the workshop's condensed rule summary, kept only to explain those runs. The Project workflow reads the original WHO article instead.

## Credits

The synthetic case, answer key, two-prompt pipeline and agent pipeline come from the **Agentic Pathology Workshop**, API Summit 2026: [github.com/hesamhakim/agentic-pathology-workshop](https://github.com/hesamhakim/agentic-pathology-workshop)

- Hesam H. Javadi, PhD (Medical College of Wisconsin, Children's Wisconsin): workshop infrastructure, LangFlow components
- Srikar Chamala, PhD (Children's Hospital Los Angeles, USC Keck School of Medicine)
- Omar Baba, MD (Henry Ford Health): AML case design, answer key, two-stage prompts

Workshop materials are used under the MIT License; see [`LICENSE-workshop-materials`](LICENSE-workshop-materials). The WHO and ELN articles belong to their authors and publishers and are linked, not redistributed.

Contact: Srikar Chamala, schamala@chla.usc.edu
