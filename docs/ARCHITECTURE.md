# Design of the no-code reporting demonstration

## Three kinds of input

| Input | Role | Location |
|---|---|---|
| Skill | A reusable procedure for reading reports, consulting guidance, drafting, and reviewing | `manual_demo/integrated-reporting-demo/SKILL.md` and its references |
| Case reports | The evidence about this synthetic case | Only the four component PDFs, uploaded at run time |
| Guideline | The external authority for an applied classification criterion | The original public article opened by the assistant, or an identified uploaded original |

The assistant uses its built-in document and web tools. The kit contains no scripts, API calls, software dependencies, or encoded expected diagnosis. Users install the skill through their app's upload interface, or paste the self-contained Project instructions into a Project.

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

Run the baseline before enabling the skill, outside any Project containing the case answer. Keep the same app and model for the second conversation. Keep the answer key, original README's teaching answers, archived outputs, and prior conclusions out of generation. Show what happened, including failures and uncertainty. Do not assume the baseline must give a wrong diagnosis.

The full kit contains only the four input PDFs, skill package/source files, prompts, presenter guide, and workshop attribution/license. The existing `index.html` and `runs/` remain historical replays.

Setup and presentation instructions are in [START_HERE](../manual_demo/START_HERE.md). Platform menu labels and availability are checked against the official documentation linked there; actual installation and a rehearsal in the presenter's account are still required.
