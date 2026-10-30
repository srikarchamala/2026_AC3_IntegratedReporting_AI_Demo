# No-upload route: copy and paste from GitHub

Use this route if you cannot upload files to Claude (for example, office IT blocks uploads). Everything is copied as **text** from GitHub and pasted into Claude. No files leave your computer.

The workflow is the same as the upload route, with the same Skills, the same four reports and the same WHO article. Only the delivery changes.

## How to copy a file from GitHub

1. Click the file name in this folder.
2. Click the **Copy raw file** button (the two-squares icon at the top right of the file view). This copies the whole file as plain text.
3. Paste it into Claude (Ctrl+V or Cmd+V).

## Files in this folder

| File | What it is | Where it goes |
|---|---|---|
| `PROJECT_INSTRUCTIONS_PASTE.txt` | Project instructions for this route | Paste into the Project's **instructions** |
| `1_SKILLS_ALL.md` | All 8 Skills files in one text (`Skills_1` to `Skills_8`) | Paste into Project knowledge as text content titled **SKILLS_ALL** |
| `2_PATHOLOGY_REPORTS_ALL.md` | The 4 pathology reports as text, with PDF page markers | Paste into Project knowledge titled **PATHOLOGY_REPORTS_ALL**; also used in the regular chat |
| `3_WHO_2022_article_text.md` | Text of the WHO 2022 article (CC BY 4.0), with journal page markers | Paste into Project knowledge titled **WHO_2022_article_text** |
| `CHECK_SETUP_PROMPT_PASTE.txt` | Prompt that checks Claude can read everything | Send in the Project chat (step 3) |
| `RUN_DEMO_PROMPT_PASTE.txt` | Prompt that runs the workflow | Send in the Project chat (step 4) |
| `BASELINE_PROMPT_PASTE.txt` | Prompt for the regular chat | Send in a regular chat with the reports pasted underneath (step 1) |

## Step 1: Regular chat (baseline)

1. Open a **new chat outside any Project**.
2. Copy the first paragraph of `BASELINE_PROMPT_PASTE.txt` into the message box.
3. Below it, paste the full contents of `2_PATHOLOGY_REPORTS_ALL.md`. Claude may show the long paste as a pasted-text block; that's fine.
4. Send.

## Step 2: Set up the Project

1. Create a Project, for example **AC3 Integrated Reporting Demo**.
2. Open **Set project instructions**, paste the contents of `PROJECT_INSTRUCTIONS_PASTE.txt`, and save.
3. In the Project knowledge area, click **+** and choose **Add text content**. Paste `1_SKILLS_ALL.md` and title it `SKILLS_ALL`. Save.
4. Repeat for `2_PATHOLOGY_REPORTS_ALL.md` (title `PATHOLOGY_REPORTS_ALL`) and `3_WHO_2022_article_text.md` (title `WHO_2022_article_text`).

That's three text items in total. Don't add anything else.

## Step 3: Check the setup

Start a new chat in the Project and send the contents of `CHECK_SETUP_PROMPT_PASTE.txt`. You should get a table of 13 rows (8 Skills, 4 reports, 1 WHO article) ending with **"Setup ready for the workflow"**. If anything shows PARTIAL or MISSING, re-paste that item.

## Step 4: Run the demo

In the same Project chat, send the contents of `RUN_DEMO_PROMPT_PASTE.txt`. Nothing needs to be attached. Expect it to take several minutes. The response starts with a short summary, then the eleven-section draft, then the full evidence tables.

## Notes

- The report and WHO texts were extracted unchanged from the PDFs in `../PATHOLOGY_REPORTS/` and `../GUIDELINES/`. Line breaks and table layout may differ from the PDFs.
- WHO article: Khoury JD, et al. *Leukemia* 2022;36:1703–1719, [doi:10.1038/s41375-022-01613-1](https://doi.org/10.1038/s41375-022-01613-1), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- All case material is synthetic. Every output is a teaching draft for human review.
