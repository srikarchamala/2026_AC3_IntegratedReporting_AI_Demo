# Start here: regular chat versus a saved reporting workflow

Use this kit directly in Claude or ChatGPT. **Skill = saved procedure; reports = evidence; WHO = external reference.** The case is synthetic, and every output is a teaching draft requiring review.

Extract `AC3_No_Code_Demo_Kit.zip` on your computer. Keep the inner **`integrated-reporting-demo.zip`** intact: that is the file to upload through the app's Skills interface. Attaching it to an ordinary conversation does not establish that the skill is installed.

## 1. Run regular chat first

Before installing or enabling the demo skill, open a **fresh ordinary chat outside Projects**. Use a conversation without the answer key or previous case conclusions. If the skill is already installed, disable it for this baseline.

Attach only the four PDFs in `case/`:

- `01_bone_marrow_morphology.pdf`
- `02_flow_cytometry.pdf`
- `03_cytogenetics_fish.pdf`
- `04_molecular_ngs.pdf`

Paste the contents of `01_BASELINE_PROMPT.txt` and send. Save the response. Keep the **same app and model** for the second demonstration. A regular chat may produce a good report; compare the actual results without assuming it must fail.

## 2. Choose one setup

### Claude: upload the Skill ZIP

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

Enable web search for the workflow when available. Its stages are to extract each report, retrieve the approved reference, assess criteria, draft an integrated report, and review the evidence.

The default reference is the [public 2022 WHO fifth-edition myeloid author overview](https://doi.org/10.1038/s41375-022-01613-1). It is neither the complete Blue Book nor a claim of the latest guidance. An optional ELN reference addresses a separate risk framework; formal risk assessment requires that reference and its scope to be checked.

Show one extracted finding, its original quotation, one retrieved criterion, and the report statement supported by both. Check that different measurement methods remain distinct and that missing information has not become a negative result.

This is **one assistant following stages**. Uploading a skill does not guarantee four independently spawned agents. A review performed in the same chat is a review stage, not independent QA.

For an additional review, open another fresh chat and use `04_QA_PROMPT.txt` with the four original reports, generated draft, extraction results, and actually retrieved reference passages. Request concerns rather than a silently rewritten report.

## A five-to-six-minute presentation

| Time | Show |
|---|---|
| 0:00–1:00 | The four source reports and the regular-chat request |
| 1:00–2:00 | Its actual result, then the installed skill or Project instructions |
| 2:00–4:00 | The workflow's extraction, external reference, and draft |
| 4:00–5:00 | One sentence traced to findings and criteria; the review stage |
| 5:00–6:00 | Observed differences and remaining uncertainty |

Rehearse beforehand. If showing saved output, identify it as a rehearsal result. Keep answer keys and historical outputs outside generation.

## If something blocks the demo

- **WHO page cannot be read:** stop classification or attach the original public article, retaining its URL and edition. Do not substitute a search snippet, remembered rules, or a condensed answer key.
- **Skill unavailable:** use the Project route if permitted. Its instructions need no additional support-file uploads.
- **Skill not loading:** confirm it is enabled and name it explicitly.
- **Slow generation:** use your labeled rehearsal output and inspect its evidence.

The package structure has been checked. It has **not** been installed or executed in your signed-in Claude or ChatGPT account; confirm loading and output during rehearsal.
