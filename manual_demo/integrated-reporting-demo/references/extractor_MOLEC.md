# MOLEC: molecular report extraction pass

Use `extractor_common.md` and the **MOLEC** source ID. Inspect only the assigned molecular report. Return the common findings table, starting at `MOLEC-001`.

| Field / population | What to capture |
|---|---|
| Assay and scope | Assay name, tested scope, method, overall result, and stated coverage or sensitivity limitations. |
| Variant identity | Gene, variant description, transcript, and variant type exactly as provided. |
| Variant measurements | Allele fraction, ratio, copy number, or other measurement, preserving its stated units and method. |
| Source annotations | Reported tier, significance, and other annotations with their exact supporting wording. |
| Reported implications | Explicit diagnostic, prognostic, or predictive comments labeled **Source-reported interpretation**. |
| Limitations and status | Pending results, unperformed components, technical limitations, and uncertain findings. |

Give each actual reported variant or gene-level result a group label, such as “Variant group 1,” and repeat that label across its rows. Keep findings from different variants separate. Preserve exact gene symbols and variant/transcript strings; do not reconstruct a missing expression or infer clonality, inheritance, or biological significance.

For an actual reported variant, an absent attribute may be marked **Not reported** within its group. Do not create fictional variants or gene-specific negative results to populate the table. An unmentioned gene provides no evidence of a negative test.

Preserve ratios and allele fractions as reported rather than converting between them. Extract classification, risk, or treatment-related wording only when this source states it, with clear attribution. Any independently derived implication requires later integration with supporting reference material. Include the shared patient/specimen identity, accessions, performing laboratory, dates, and limitations.
