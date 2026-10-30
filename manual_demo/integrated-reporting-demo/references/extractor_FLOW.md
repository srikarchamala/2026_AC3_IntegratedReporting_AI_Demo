# FLOW: flow cytometry extraction pass

Use `extractor_common.md` and the **FLOW** source ID. Inspect only the assigned flow cytometry report. Return the common findings table, starting at `FLOW-001`.

| Field / population | What to capture |
|---|---|
| Specimen and adequacy | Specimen type, viability, adequacy, and source-stated quality limitations. |
| Population descriptions | Each population's exact label and any reported relationship to another gate. |
| Population measurements | Each percentage or count with its stated gate, units, and denominator. |
| Immunophenotype | Marker names, positive/negative results, intensity, subset qualifiers, and aberrant patterns as reported. |
| Gating and method | The source's gating strategy, methodological descriptions, and limitations. |
| Lineage and interpretation | The report's own assessment and certainty, labeled as source-reported interpretation where appropriate. |

Repeat a population group label across its descriptive, measurement, and marker rows. Keep a reported blast population separate from other populations. If promonocytes or monocytic populations are described, retain their exact source labels and measurements. Do not assume that populations overlap, are disjoint, or use the same denominator unless the report establishes that relationship.

Preserve an explicitly negative marker result, but do not treat an unmentioned marker as negative. Record an unstated denominator or gating detail as **Not stated**. Include **Not reported** rows for missing checklist information.

Carry through the shared identity, accession, laboratory, date, and limitation fields. Do not use this pass to decide whether flow resolves another report's uncertainty. Cross-report comparison belongs to integration; this table preserves what the flow source itself supports.
