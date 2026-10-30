# Start here: regular chat versus a saved reporting workflow

Use this kit directly in Claude or ChatGPT. **Skills files = saved procedure; reports = evidence; WHO = external reference.** The case is synthetic, and every output is a teaching draft requiring review.

**Preferred for this workshop: Claude Projects with individual Word uploads.** Follow [the Claude Project guide](claude_project/README.md), or open `claude_project/PARTICIPANT_GUIDE.docx` for the complete directions, Project instructions, and prompts in Word. Use the dedicated [Claude Project kit](https://raw.githubusercontent.com/srikarchamala/2026_AC3_IntegratedReporting_AI_Demo/main/manual_demo/Claude_Project_Demo_Kit.zip), or the `claude_project/` folder inside the complete kit.

Extract the downloaded kit on your computer. For the Project route, upload the individual files from `claude_project/SKILLS/` and `claude_project/PATHOLOGY_REPORTS/` (or use the Markdown copies in `claude_project/SKILLS_MARKDOWN/` instead of `SKILLS/`) after pasting the Project instructions. The separate inner `integrated-reporting-demo.zip` is used only for the optional native Skills route below.

## 1. Run regular chat first

Before installing or enabling the demo skill, open a **fresh ordinary chat outside Projects**. Use a conversation without the answer key or previous case conclusions. If the skill is already installed, disable it for this baseline.

Attach only the four pathology reports in `case/`:

- `Pathology_Report_1_bone_marrow_morphology.pdf`
- `Pathology_Report_2_flow_cytometry.pdf`
- `Pathology_Report_3_cytogenetics_fish.pdf`
- `Pathology_Report_4_molecular_ngs.pdf`

The same four files are in `claude_project/PATHOLOGY_REPORTS/`. In the GitHub repository, the originals are in the top-level `case/` folder as `01_` to `04_`.

Paste the contents of `01_BASELINE_PROMPT.txt` and send. Save the response. Keep the **same app and model** for the second demonstration. A regular chat may produce a good report; compare the actual results without assuming it must fail.

## 2. Choose one setup

### Claude Project with individual Skills files

Create a Project named **AC3 Integrated Reporting Demo**. Under **Set project instructions**, paste the contents of `claude_project/PROJECT_INSTRUCTIONS.txt` and save. Add all twelve documents to the Project's Files or knowledge area: the eight Skills files in `claude_project/SKILLS/` (`Skills_1` to `Skills_8`) and the four pathology reports in `claude_project/PATHOLOGY_REPORTS/` (`Pathology_Report_1` to `_4`). Markdown copies of the Skills files are in `SKILLS_MARKDOWN/`; use them instead of `SKILLS/`, not as well.

Start a conversation inside the Project. Send `claude_project/CHECK_SETUP_PROMPT.txt`, resolve any reported missing or partial content, then send `claude_project/RUN_DEMO_PROMPT.txt`. All copy-and-paste text is also in the Word participant guide. These documents guide the workflow without native Skill installation. See the [complete Project guide](claude_project/README.md) for the file list and source-access steps.

### Optional Claude route: upload the native Skill ZIP

1. In **Settings → Capabilities**, enable **Code execution and file creation**, called **Create and edit files** in the updated layout.
2. Open **Customize → Skills**.
3. Select **“+” → “+ Create skill” → “Upload a skill.”**
4. Upload `integrated-reporting-demo.zip` and toggle the skill on.
5. Start a fresh conversation, attach the same four case PDFs, and paste `02_AGENT_START_PROMPT.txt`.

Confirm in the activity display that Claude loaded the skill. If it did not, explicitly ask it to use **integrated-reporting-demo**. Workspace settings may restrict uploading. See [Claude's official Skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### ChatGPT: use Skills if available

If your account has the upload feature, open **Plugins → Skills → Create → Upload from your computer** and select `integrated-reporting-demo.zip`. Complete the app's scan, review, and installation steps. Then start a fresh conversation, attach the four PDFs, and paste `02_AGENT_START_PROMPT.txt`. Availability depends on your account and workspace; see [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

### ChatGPT fallback: Project instructions

Create a new Project. Open its **••• menu → Project settings**, and paste the **contents** of `03_PROJECT_INSTRUCTIONS.txt` into the instructions field. Upload only the four case PDFs. Start a new chat inside that Project and paste `02_AGENT_START_PROMPT.txt`.

`03_PROJECT_INSTRUCTIONS.txt` is self-contained: no extra supporting files or skill installation are required for this route. Label it a **Project-guided workflow**. See [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

## 3. Let the workflow use evidence

Enable web search for the workflow when your interface offers that control. The newer Claude interface may search without a toggle; explicitly ask it to open the approved reference. The workflow's stages are to extract each report, retrieve the approved reference, assess criteria, draft an integrated report, and review the evidence.

The default reference is the [public 2022 WHO fifth-edition myeloid author overview](https://doi.org/10.1038/s41375-022-01613-1). It is neither the complete Blue Book nor a claim of the latest guidance. An optional ELN reference addresses a separate risk framework; formal risk assessment requires that reference and its scope to be checked.

Show one extracted finding, its original quotation, one retrieved criterion, and the report statement supported by both. Check that different measurement methods remain distinct and that missing information has not become a negative result.

This is **one assistant following stages**. Uploading a skill does not guarantee four independently spawned agents. A review performed in the same chat is a review stage, not independent QA.

For an additional review, open another fresh chat and use `04_QA_PROMPT.txt` with the four original reports, generated draft, extraction results, and actually retrieved reference passages. Request concerns rather than a silently rewritten report.

## A five-to-six-minute presentation

| Time | Show |
|---|---|
| 0:00–1:00 | The four pathology reports and the regular-chat request |
| 1:00–2:00 | Its actual result, then Project instructions and the uploaded Skills files |
| 2:00–4:00 | The workflow's extraction, external reference, and draft |
| 4:00–5:00 | One sentence traced to findings and criteria; the review stage |
| 5:00–6:00 | Observed differences and remaining uncertainty |

Rehearse beforehand. If showing saved output, identify it as a rehearsal result. Keep answer keys and historical outputs outside generation.

## If something blocks the demo

- **WHO page cannot be read:** stop classification or attach the original public article, retaining its URL and edition. Do not substitute a search snippet, remembered rules, or a condensed answer key.
- **Native Skill unavailable:** use the Claude Project route with individual Word or Markdown Skills files. The separate ChatGPT Project alternative is self-contained and uses only report uploads.
- **Project file not read:** identify the missing or partial document, reattach it if needed, and repeat the setup check. Uploading does not guarantee full retrieval.
- **Skill not loading:** confirm it is enabled and name it explicitly.
- **Slow generation:** use your labeled rehearsal output and inspect its evidence.

The package structure has been checked. It has **not** been installed or executed in your signed-in Claude or ChatGPT account; confirm loading and output during rehearsal.
