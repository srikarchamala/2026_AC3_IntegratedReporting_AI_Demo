# Claude Project workflow: test runs (30 October 2026)

Rehearsal runs of the current kit on the synthetic AML case, made with Claude. Each step was a fresh context: the regular chat had only the four reports and `BASELINE_PROMPT.txt`; the Project runs had `PROJECT_INSTRUCTIONS.txt`, the 12 upload files (Markdown set) and the setup or run prompt. Wording will differ from run to run.

| File | What it is | Result |
|---|---|---|
| `1_regular_chat_run_A.md`, `_B.md` | Regular chat, two runs | Diagnosis right both times (AML with mutated NPM1, monocytic differentiation, FLT3-ITD, normal karyotype), but DNMT3A placed in the diagnosis both times and no sources given |
| `2_project_setup_check.md` | `CHECK_SETUP_PROMPT.txt` | All 12 files read; "File setup ready for the workflow" |
| `3_project_run_no_guideline_access.md` | `RUN_DEMO_PROMPT.txt` with the WHO article unreachable online | Extraction complete; diagnosis correctly paused ("insufficient evidence") and the article requested |
| `4_project_run_with_WHO_pdf_attached.md` | `RUN_DEMO_PROMPT.txt` with `GUIDELINES/WHO_2022_Khoury_myeloid_5th_edition.pdf` attached | "AML with NPM1 mutation (WHO 5th edition)", supported by 12 criteria cited to the article; DNMT3A and FLT3-ITD kept in prognostic notes |

Checked against the sources: in run 4, all 11 WHO quotations appear word for word in the article and 189 of 195 report quotations match exactly (the other 6 are table cells split across lines or quoting-format slips, not invented text).

Compared with the answer key (`case/05_GOLD_STANDARD_integrated_report.pdf`): run 4 matches the defining diagnosis but is more conservative. It does not add "with monocytic differentiation" to the name (it treats that as the flow report's descriptor, because the WHO overview types by differentiation only when no defining abnormality is present) and lists FLT3-ITD under prognostic notes rather than as a diagnosis line. These are reporting-convention choices a pathologist can discuss and edit.
