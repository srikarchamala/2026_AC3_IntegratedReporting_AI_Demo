# MORPH: morphology extraction pass

Use `extractor_common.md` and the **MORPH** source ID. Inspect only the assigned morphology report. Return the common findings table, starting at `MORPH-001`.

| Field / population | What to capture |
|---|---|
| Specimen and adequacy | Preparation, specimen type, adequacy, quality, and stated sampling limitations. |
| Cellularity and architecture | The report's descriptive findings, ranges, and qualifications. |
| Blast measurements | Each stated percentage or count, its preparation, counting method, units, and denominator. |
| Other differential populations | Separately reported promonocytes, monocytes, and other differential entries, retaining their source labels. |
| Morphology and lineage | Cytologic features and the source's lineage assessment, including hedges or deferred conclusions. |
| Immunohistochemistry | Named markers, reported results, intensity or distribution, and limitations. |
| Interpretation and limitations | Clearly attributed source-reported interpretation, uncertainty, pending studies, and limitations. |

Use distinct rows for measurements from different preparations or methods. Keep each reported population separate even when adding numbers would produce an appealing summary. Do not create a combined count, substitute another report's percentage, or infer a denominator from customary practice.

Preserve words such as “possible,” “probable,” and “pending” where the source uses them. A source statement that awaits another study remains unresolved within this extraction pass.

Include the shared identity, accession, laboratory, and date fields. Mark absent checklist information **Not reported**. Record a stated diagnosis as **Source-reported interpretation**, with its exact quotation and location. Apply no disease thresholds, classification rules, or external interpretations during this pass.
