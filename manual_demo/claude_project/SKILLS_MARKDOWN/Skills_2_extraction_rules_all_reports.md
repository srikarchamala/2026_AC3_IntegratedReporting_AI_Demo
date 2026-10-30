# Shared extraction instructions

Perform one extraction pass for each assigned report, using source IDs **MORPH**, **FLOW**, **CYTO**, and **MOLEC**. In a single chat, these passes share conversation context. Restrict each pass's evidence to its assigned report; another report cannot fill a missing field. Apply the matching modality instructions after these shared instructions.

## Output

Label the output with its source ID and exact uploaded filename. Return a findings table with these columns:

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|

Assign unique sequential IDs within each source, beginning with `MORPH-001`, `FLOW-001`, `CYTO-001`, or `MOLEC-001`. Keep these IDs unchanged when the findings are used later. Use a separate row for each distinct result. Repeat a group label in **Field / population** when rows describe the same population, test, or molecular variant.

## Shared checklist

| Information | Preserve from the assigned report |
|---|---|
| Patient identity | Patient identifier, name, date of birth, and any reported identifying qualifications. |
| Specimen and study identity | Specimen identifier and description, accession numbers, performing laboratories, and collection/report dates. |
| Report context | Report status, amendments, clinical history, pending studies, and stated limitations. |
| Reported interpretation | The source author's interpretation, explicitly labeled **Source-reported interpretation**. |

Do not assume that an accession number is a patient or specimen identifier. Preserve identifiers and laboratory names exactly.

## Status and evidence

| Status | Meaning |
|---|---|
| Reported | The source explicitly states the finding or value. |
| Negative | The source explicitly reports a negative or absent finding within a stated assessment or tested scope. |
| Not reported | An expected checklist field is absent from the accessible report. |
| Not performed | The source explicitly says the assessment was not performed. |
| Pending | The source explicitly says the result is pending. |
| Equivocal | The source explicitly describes the result as equivocal or indeterminate. |
| Unreadable | Relevant content is present but cannot be read reliably. |

For supported findings, copy an exact, contiguous quotation and provide its actual page and section. If page numbering is unavailable, give a visible heading or other identifiable location. Do not invent a page, paraphrase a quote, or combine fragments. The evidence must support the value and any method, units, or denominator supplied.

If printed page labels conflict with the PDF's actual page order, cite the physical PDF page and note the discrepancy.

For **Not reported**, enter no inferred value or quotation and write “No supporting statement located.” For **Unreadable**, identify the affected location if possible. Mark unstated measurement context as “Not stated.” Preserve ranges, qualifiers, uncertainty, and separate populations; do not calculate new values.

Keep extraction descriptive. Derived classification, risk assessment, treatment implications, and cross-report reconciliation belong to the later integration pass with its supporting references. If the assigned file is inaccessible, mark that extraction pass unavailable instead of presenting invented findings.
