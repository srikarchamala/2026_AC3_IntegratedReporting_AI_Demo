# Claude Project demonstration guide

Build a reusable reporting workflow by uploading familiar documents to a Claude Project. Participants can use the **Word files**; an equivalent Markdown set is included for those who prefer plain text. The four case reports remain PDFs. No programming or native Skill installation is required.

Use `PARTICIPANT_GUIDE.docx` for these directions, the Project instructions, and all three prompts in Word. Keep this guide on your computer; upload only the files in the set you choose below.

## 1 Download the files

Download and extract the [Claude Project demo kit](https://raw.githubusercontent.com/srikarchamala/2026_AC3_IntegratedReporting_AI_Demo/main/manual_demo/Claude_Project_Demo_Kit.zip). The ZIP is a download container. Upload its individual documents to the Project.

For the workshop, use **`upload_word/`**. It contains eight Word workflow files and four PDF reports, twelve files in total. The alternative **`upload_files/`** folder contains the same eight workflow modules as Markdown plus the same four PDFs. Choose one complete set. Uploading both sets creates duplicate instructions.

## 2 Run regular chat first

Open a fresh ordinary Claude chat outside the reporting Project. Attach only the four report PDFs and paste `BASELINE_PROMPT.txt`, also reproduced in the Word guide. Save the actual response for comparison.

Use the same Claude model for both demonstrations. Disable any previously installed native demo skill. Where the controls are available, turn off **Memory** in the chat's **+** menu before sending its first message; do this for the Project comparison chat too. Keep answer keys, archived outputs, and previous case conclusions outside both chats. The baseline may produce a good result; compare what happened.

## 3 Create the Project

Open [Claude Projects](https://claude.ai/projects), select **+ New Project**, and name it **AC3 Integrated Reporting Demo**. If visibility is offered, keep it private for your rehearsal.

Select **Set project instructions**. Paste the complete contents of `PROJECT_INSTRUCTIONS.txt` and select **Save instructions**. You can copy the same text from the Project instructions section of the Word guide. Put it in the instructions field, not only in the Project description or an uploaded document.

In the Project's **Files** or **project knowledge** area, use **+** to upload each of the twelve documents from `upload_word/`. You may select them together while keeping them as individual files. Some accounts have a newer Project layout; use its corresponding files and instructions controls.

### Eight workflow documents

| Word file | What it tells Claude to do |
|---|---|
| `Skills_1_master_procedure.docx` | Follow the complete reporting workflow |
| `Skills_2_extraction_rules_all_reports.docx` | Preserve quotations, evidence locations, measurements, and missing information |
| `Skills_3_extraction_rules_morphology.docx` | Extract morphology findings |
| `Skills_4_extraction_rules_flow_cytometry.docx` | Extract flow cytometry findings |
| `Skills_5_extraction_rules_cytogenetics_FISH.docx` | Extract cytogenetics and FISH findings |
| `Skills_6_extraction_rules_molecular.docx` | Extract molecular findings |
| `Skills_7_guideline_sources.docx` | Locate and read the approved original WHO reference; use optional ELN guidance only when requested |
| `Skills_8_integrated_report_template.docx` | Format the report, criteria table, and evidence review |

### Four source reports

- `CASE_01_bone_marrow_morphology.pdf`
- `CASE_02_flow_cytometry.pdf`
- `CASE_03_cytogenetics_fish.pdf`
- `CASE_04_molecular_ngs.pdf`

The Markdown alternative uses the same workflow filenames ending in `.md`. Project instructions recognize either format. Word files contain the workflow as real document text, with headings and readable tables; they are not screenshots of the instructions.

## 4 Check what Claude can read

Start a new conversation inside the Project. Send `CHECK_SETUP_PROMPT.txt`, also reproduced in the Word guide. Claude should identify the twelve files, state which contents it actually read, and give a brief content-based indication for each. This first check does not ask for a diagnosis or a guideline lookup.

Resolve any missing, partial, duplicate, or unreadable document before the affected stage. A filename list alone is not proof of reading. Project retrieval may select passages rather than the whole document; the check improves visibility but does not guarantee complete retrieval.

## 5 Run the workflow

In that Project conversation, send `RUN_DEMO_PROMPT.txt`, also reproduced in the Word guide. It asks Claude to extract the four reports, open the approved WHO source, assess criteria, draft the integrated report, and review support.

If your interface has a **Web search** option in the chat's **+** menu, enable it. The newer Claude interface searches when useful and may have no toggle. The run prompt explicitly requests opening and reading the source. Workspace settings can affect access.

Show one reported finding, its original quotation, the guideline section actually read, and the report statement supported by that evidence. A file named `Skills_7_guideline_sources` supplies the source address and scope; it is not itself the guideline. The default is the public 2022 WHO fifth-edition myeloid overview, rather than a claim to have consulted the full current Blue Book. If Claude cannot read the necessary article text, it should pause derived classification and request the original article as an upload.

## A short presentation sequence

| Time | Show |
|---|---|
| First minute | Four PDFs and the regular-chat result |
| Second minute | Project instructions and the eight uploaded Word workflow documents |
| Next two minutes | Report extraction, actual reference access, and integrated draft |
| Final one or two minutes | One evidence trail, review concerns, and observed differences |

Describe this as a **Project-guided reporting workflow**. The uploaded documents organize one assistant's stages; their presence does not establish independently running agents or independent review. The task remains a synthetic teaching exercise requiring human review.

Rehearse in your Claude account before presenting. If using saved rehearsal output, identify it as such. The kit's structure and documents have been checked; account-specific loading and the live online lookup still need your rehearsal.

## Official setup references

Menu labels and file support were checked on 30 October 2026.

- [Create and manage Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude)
- [Project document retrieval](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)
- [Web search and direct URL access](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)
- [Claude file formats including Markdown](https://claude.com/product/overview)

The separate native Skills option is documented in [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Uploading a Word or Markdown workflow document to Project knowledge does not itself install a native Skill.
