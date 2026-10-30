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
| `SKILLS/` | The 8 Skills files (Word): the workflow instructions | **Yes**, into the Project (step 3) |
| `PATHOLOGY_REPORTS/` | The 4 pathology reports (PDF): the case | **Yes**, into the Project (step 3); also attached in the regular chat (step 2) |
| `SKILLS_MARKDOWN/` | The same 8 Skills files as Markdown (`.md`) | Only if you prefer Markdown, **instead of** `SKILLS/`. Never upload both |
| `PROJECT_INSTRUCTIONS.txt` | Text you paste into the Project's instructions | Paste, don't upload |
| `BASELINE_PROMPT.txt` | Prompt for the regular chat (step 2) | Paste |
| `CHECK_SETUP_PROMPT.txt` | Prompt that checks Claude can read every file (step 4) | Paste |
| `RUN_DEMO_PROMPT.txt` | Prompt that runs the workflow (step 5) | Paste |
| `GUIDELINES/` | The original WHO 2022 classification article and the optional ELN 2022 AML guidelines (PDF) | **Attach** the WHO article in the chat in step 5; don't upload to the Project |
| `PARTICIPANT_GUIDE.docx` | All of the above in one Word document | Keep for yourself; **don't upload** |

Every upload file is named for its job: `Skills_1` to `Skills_8` are the instructions, in the order Claude uses them, and `Pathology_Report_1` to `Pathology_Report_4` are the four pathology reports. Both folders hold the same four reports.

## Step 2: Run the regular chat first

Do this **before** you create the Project, so nothing from the Project influences it.

1. Open a **new chat** at [claude.ai](https://claude.ai), **outside** any Project.
2. If your chat has a Memory option in the **+** menu, turn it off for this chat.
3. Attach the **four `Pathology_Report_` PDFs** from `PATHOLOGY_REPORTS/` (paperclip or **+** → upload). Attach nothing else.
4. Paste the contents of `BASELINE_PROMPT.txt` and send.
5. Save the answer (copy it into a document, or leave the tab open).

Note the model you used (shown near the message box). Use the same model in step 5.

## Step 3: Create the Project

1. Go to [claude.ai/projects](https://claude.ai/projects) and click **+ New Project**.
2. Name it `AC3 Integrated Reporting Demo`. Keep it private.
3. Click **Set project instructions**. Paste the **entire** contents of `PROJECT_INSTRUCTIONS.txt` and click **Save instructions**.
   Put it in the instructions box, not in the Project description.
4. In the Project's **Files** (project knowledge) area, click **+** and upload all **12 files**: the 8 in `SKILLS/` and the 4 in `PATHOLOGY_REPORTS/`. You can select them together.
5. Check that the Project lists 12 files: 8 starting `Skills_` and 4 starting `Pathology_Report_`.

### What the 12 files are

They fall into four groups. Together they work like a written procedure handed to a new colleague, plus the case to work on.

**The procedure (1 file)**

| File | What it does |
|---|---|
| `Skills_1_master_procedure.docx` | The master procedure. Lists the six stages (inventory, extraction, guideline, criteria, draft, review), the evidence rules, and which other file to use at each stage |

**How to read each report (5 files)**

| File | What it does |
|---|---|
| `Skills_2_extraction_rules_all_reports.docx` | Rules for every report: quote the exact words, record where they came from, keep units and methods, and treat "not reported" as unknown, never as negative |
| `Skills_3_extraction_rules_morphology.docx` | Extraction rules for the bone marrow morphology report: cellularity, blast and monocyte counts kept separate, lineage wording, cytochemistry |
| `Skills_4_extraction_rules_flow_cytometry.docx` | Extraction rules for the flow cytometry report: each cell population and its percentage, gating, markers, lineage wording |
| `Skills_5_extraction_rules_cytogenetics_FISH.docx` | Extraction rules for the cytogenetics and FISH report: exact karyotype, each FISH probe and result, and the limits of a targeted panel |
| `Skills_6_extraction_rules_molecular.docx` | Extraction rules for the molecular (NGS) report: each variant with its transcript, allele fraction and tier, what was tested, and assay limits |

**Where the rules come from and how to write it up (2 files)**

| File | What it does |
|---|---|
| `Skills_7_guideline_sources.docx` | Points to the WHO 5th edition myeloid article (and optional ELN 2022 risk guidance) that Claude must open and read. It holds addresses and scope only, not the rules themselves, and no answer |
| `Skills_8_integrated_report_template.docx` | The output format: extraction tables, criteria table, the 11-section report, and the review table |

**The case (4 files)**

| File | What it is |
|---|---|
| `Pathology_Report_1_bone_marrow_morphology.pdf` | Synthetic morphology report (MORPH) |
| `Pathology_Report_2_flow_cytometry.pdf` | Synthetic flow cytometry report (FLOW) |
| `Pathology_Report_3_cytogenetics_fish.pdf` | Synthetic karyotype and FISH report (CYTO) |
| `Pathology_Report_4_molecular_ngs.pdf` | Synthetic molecular NGS report from a separate reference lab (MOLEC) |

The 8 Skills files contain no diagnosis or expected answer, and none of them are the guideline itself; Claude reads the WHO article separately in step 5. The `SKILLS_MARKDOWN/` folder has the same 8 Skills files as Markdown (`.md`) if you prefer them; upload it in place of `SKILLS/`, not as well.

Do **not** upload the answer key (`case/05_GOLD_STANDARD_integrated_report.pdf`), this README, the participant guide, or anything from `runs/`. They contain the expected answer and would make the comparison unfair.

## Step 4: Check that Claude can read every file

1. Start a **new chat inside the Project**.
2. Paste the contents of `CHECK_SETUP_PROMPT.txt` and send.
3. Claude returns a table with one row per file and a status: **READ**, **PARTIAL**, **MISSING** or **UNREADABLE**.
4. It should end with **"File setup ready for the workflow."**

If it says **"File setup incomplete"**, re-upload the files it names and run the check again. This check does not diagnose anything; it only confirms the files are readable.

## Step 5: Run the workflow

1. In the same Project chat, **attach `GUIDELINES/WHO_2022_Khoury_myeloid_5th_edition.pdf`** (paperclip or **+** → upload). Claude reads the original WHO article from it, so the run does not depend on web access or conference Wi-Fi. Leave the ELN article out unless you want a formal risk category.
2. Paste the contents of `RUN_DEMO_PROMPT.txt` and send. (Without the attachment, turn on **Web search** if your **+** menu offers it; Claude will then try to open the article online.)
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

**If Claude says it could not open the WHO article:** attach `GUIDELINES/WHO_2022_Khoury_myeloid_5th_edition.pdf` and ask Claude to continue using the uploaded article. It will label it as an uploaded source. Without the article, Claude is instructed to pause the diagnosis rather than classify from memory.

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
| Classification paused, WHO article not read | Attach `GUIDELINES/WHO_2022_Khoury_myeloid_5th_edition.pdf` and ask Claude to continue |
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

[`runs/claude_project_test/`](runs/claude_project_test/) has test runs of the current Claude Project kit (regular chat, setup check, and the workflow with and without the WHO article), with a comparison to the answer key.

`prompts/agent_pipeline/who5e_instructions.md` is the workshop's condensed rule summary, kept only to explain those runs. The Project workflow reads the original WHO article instead.

## Credits

The synthetic case, answer key, two-prompt pipeline and agent pipeline come from the **Agentic Pathology Workshop**, API Summit 2026: [github.com/hesamhakim/agentic-pathology-workshop](https://github.com/hesamhakim/agentic-pathology-workshop)

- Hesam H. Javadi, PhD (Medical College of Wisconsin, Children's Wisconsin): workshop infrastructure, LangFlow components
- Srikar Chamala, PhD (Children's Hospital Los Angeles, USC Keck School of Medicine)
- Omar Baba, MD (Henry Ford Health): AML case design, answer key, two-stage prompts

Workshop materials are used under the MIT License; see [`LICENSE-workshop-materials`](LICENSE-workshop-materials). The WHO article (Khoury et al., *Leukemia* 2022) is included under CC BY 4.0 and the ELN recommendations (Döhner et al., *Blood* 2022) as an unmodified copy under CC BY-NC-ND 4.0; copyright remains with their authors and publishers. See [`manual_demo/claude_project/GUIDELINES/README.md`](manual_demo/claude_project/GUIDELINES/README.md).

Contact: Srikar Chamala, schamala@chla.usc.edu
