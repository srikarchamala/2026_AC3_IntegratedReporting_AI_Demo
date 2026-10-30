# CYTO: cytogenetics and FISH extraction pass

Use `WORKFLOW_2_extraction_rules_all_reports.md` and the **CYTO** source ID. Inspect only the assigned cytogenetics/FISH report. Return the common findings table, starting at `CYTO-001`.

| Field / population | What to capture |
|---|---|
| Karyotype | The exact reported notation, punctuation, clone counts, and qualifications. |
| Analysis details | Metaphase counts, banding resolution, preparation, and specimen adequacy when reported. |
| FISH targets and results | Each named target/probe and its corresponding result, cell count, percentage, or cutoff as stated. |
| Other reported assays | Any explicitly included microarray or other cytogenetic result, with its own method and scope. |
| Assay scope | Tested targets, stated coverage, detection limitations, and unsuccessful or pending analyses. |
| Interpretation | The source author's interpretation, clearly attributed and quoted. |

Use a consistent test group label to link a FISH target with its result and measurement rows. Preserve an aggregate panel result as an aggregate when individual probe results are not supplied. Do not generate per-probe results or add targets from knowledge of a customary panel.

Restrict a negative result to the assessment or tested scope described in its source. Do not expand a reported normal or negative finding into an exclusion of untested abnormalities. Keep those source limitations visible for integration.

Include the shared identity, specimen, accession, laboratory, and date fields. Mark missing checklist information **Not reported** and explicitly unperformed studies **Not performed**. Retain exact quotations and locations for every supported result. Do not derive a disease category or classification rule during this pass.
