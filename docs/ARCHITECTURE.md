# Design of the no-code reporting demonstration

## Three kinds of input

| Input | Role | Location |
|---|---|---|
| Workflow files | A reusable procedure for reading reports, consulting guidance, drafting, and reviewing | `manual_demo/claude_project/upload_word/`: `SKILL.docx` and seven supporting Word files; equivalent Markdown copies are in `upload_files/` |
| Case reports | The evidence about this synthetic case | The four component PDFs selected for the run, uploaded to the Project or attached to the chat |
| Guideline | The external authority for an applied classification criterion | The original public article opened by the assistant, or an identified uploaded original |

The assistant uses its built-in document and web tools. The kit contains no scripts, API calls, software dependencies, or encoded expected diagnosis. The preferred Claude route uses twelve individually uploaded Project files and a short controller pasted into Project instructions. Native Skills installation and the self-contained ChatGPT Project instructions remain optional alternatives.

## Claude Project loading

`PROJECT_INSTRUCTIONS.txt` names the eight workflow files and four reports, tells Claude to read them, and defines what to do when content is missing or only partly retrieved. It recognizes Word and Markdown equivalents and selects one version per module. It is pasted into the Project instructions field; merely uploading this controller or putting it in the Project description does not configure the instructions. The Word participant guide includes the same controller and prompts for copy and paste.

The Project copies of `SKILL.docx` and `SKILL.md` use flat filenames because manually uploaded documents do not preserve a native skill directory. The Word documents retain the operative checklist/template content, with readable headings and tables; header-only table templates list their columns in order. Their internal references use Word filenames. The Markdown sources retain the canonical checklist content. The four PDF copies in each set are byte-identical to the originals in `case/`.

`CHECK_SETUP_PROMPT.txt` requests a file inventory and a short content-based indication of what was read. This is an inspection aid, not a completeness guarantee: Claude Project retrieval can select only relevant passages. If a required file is unavailable or partial, the assistant asks for the full file before the affected stage. `RUN_DEMO_PROMPT.txt` then starts the reporting workflow.

An uploaded Word or Markdown workflow document in Project knowledge is not evidence of native Skill installation. The Project controller explicitly selects it as an instruction source; report and website contents remain evidence, not instructions. Participants upload either the Word set or the Markdown set. If both are present, the controller requires duplicate-version handling before conflicting instructions are used.

## One assistant, visible stages

The saved workflow organizes one assistant's work into six stages:

1. Inventory the four reports and check the available identity information.
2. Extract each report with the shared policy and its report-specific checklist.
3. Open and read the approved guidance, preserving source identity and scope.
4. Assess the relevant criteria against the extracted findings.
5. Draft the integrated report with evidence references.
6. Revisit the evidence and display review concerns.

Separate extraction passes in one chat share context. The instructions require report-specific evidence, but do not establish isolated processing. A skill upload does not itself spawn independent agents. A review in the same conversation is a self-review stage; a fresh review chat can provide an additional pass when given the full evidence bundle.

These distinctions should be stated during the demo. The demonstration shows a reusable workflow with tools and inspectable evidence. It is not an isolated benchmark of model intelligence or clinical accuracy, because instructions, reference use, and output structure differ from the baseline.

## Extraction and interpretation

The common policy preserves source identity, accession numbers, laboratories, dates, quotations, locations, methods, units, denominators, and explicit missingness. Four checklists cover morphology, flow, cytogenetics/FISH, and molecular results.

A table records what its assigned report actually says. A source-authored diagnosis or prognostic statement remains attributed to that source. Missing text is not a tested negative result. Distinct measurements, populations, and variants remain separate. Derived classification belongs in the later criterion assessment.

## The online reference is not a rule summary

The source directory identifies the public 2022 WHO fifth-edition myeloid author overview by title, DOI, and public locations. It does not reproduce a medical decision tree. The assistant must read the actual relevant context, including tables, footnotes, exceptions, prerequisites, and scope.

That overview has a defined scope; it is not the full current WHO Blue Book. Optional ELN 2022 adult AML risk guidance is a separate framework and requires its own applicability checks. If the text is unavailable, the instructions require a visible pause or an upload of the original public article. Search snippets and remembered criteria are insufficient.

A source card records what was actually accessed. No computed checksum, retrieval success, timestamp, or page number should be claimed unless observed. An uploaded original remains labeled an upload.

## Evidence trail and limits

Each extracted finding has an ID and an original quote/location. Each applied criterion has a source citation, finding references, an assessment, and a concise explanation. Reported facts cite findings; derived interpretation and diagnosis cite findings and applicable criteria. Unknown necessary evidence remains unknown.

The review stage checks support, omissions, identity, missingness, measurement context, variant grouping, criterion applicability, and overstatement. Those checks are model behavior requested by instructions, not enforced programmatic guarantees. They can fail. Human inspection of the original passages remains part of the teaching exercise.

The eleven report sections cover patient/specimen, component studies, clinical context, four modalities, integrated interpretation, diagnostic assessment, prognostic/predictive observations, and limitations.

## Demonstration boundaries

Run the baseline outside the reporting Project and before enabling any native demo skill. Keep the same app and model for both conversations. Where available, turn off Memory before the first message in each comparison chat. Keep the answer key, original README's teaching answers, archived outputs, and prior conclusions out of generation. Show what happened, including failures and uncertainty. Do not assume the baseline must give a wrong diagnosis.

The Claude Project kit offers two sets of twelve upload files: eight workflow modules plus four PDFs in each set. Participants choose one set. It also includes a Word participant guide, the pasted controller, three prompts, the online guide, and workshop attribution/license. The full multi-route kit additionally contains the native skill package and ChatGPT alternative; some files repeat across the self-contained route folders. Neither kit includes the answer key or archived outputs. The existing `index.html` and `runs/` remain historical replays.

Setup and presentation instructions are in the [Claude Project guide](../manual_demo/claude_project/README.md) and [START_HERE](../manual_demo/START_HERE.md). Platform menu labels and availability are checked against the official documentation linked there; actual upload and a rehearsal in the presenter's account are still required.
