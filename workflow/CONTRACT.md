# Source-grounded workflow contracts

This is a synthetic teaching workflow. It adds a runnable, fixed sequence of model calls; it does not claim to be an autonomous clinical system or recreate the archived twelve-node workshop run.

## Extraction

One independent call receives only its assigned document. `extract_<SOURCE>.json` has `source_id` (MORPH, FLOW, CYTO, MOLEC), `document_name`, and `findings`.

Each finding has `id` (for example MORPH-001), `field`, `group_id` (string or null; associate molecular variant fields), `value` (string, number, or null), `status` (reported, negative, not_reported, not_performed, pending, equivocal, unreadable), `units`, `method`, `denominator` (each string or null), `quote` (string), and `page` (positive integer or null). Non-reported values must not masquerade as negative. `not_reported` has null value/page and empty quote; other statuses need source support unless unreadable, which can identify a page and retain an empty quote. Quotes must occur on the identified PDF page after whitespace/Unicode normalization. Field-specific instructions and field enums differ by modality. Common fields include patient_identifier, patient_name, date_of_birth, specimen_identifier, specimen_description, accession_number, performing_lab, collection_date, report_date, report_status, reported_interpretation, and limitations. The output schemas require exactly these top-level keys and all finding keys. No inferred classifying boolean.

## Retrieved reference

`sources.json` is an approved source manifest. It carries framework, edition/year, scope, canonical URL, retrieval URLs, and section selectors; it contains no diagnostic rules or expected case answers. Fetch only public approved sources; do not automate WHO subscriber access. Reference snapshots contain `source_id`, `title`, `framework`, `edition`, `canonical_url`, `retrieved_url`, `retrieved_at`, `sha256`, `passages` (list of `id`, `section`, `text`). Include table footnotes, exceptions and context. Distinguish a public author overview from the full current Blue Book. If required source content cannot be retrieved and verified, stop; no model-memory fallback. Locally supplied original public article files must retain source identity and hashes and be labeled local imports.

## Integration

An integration call receives all extraction JSONs, reference snapshots and deterministic validation findings. It returns `framework` (string), `classification_status` (supported, insufficient_evidence, out_of_scope), `criteria_assessment`, `sections`, `unresolved_issues` (array of strings).

Each criterion is `{id, criterion, source_id, passage_id, quote, finding_ids, assessment, explanation}`. assessment is met, not_met, unknown or not_applicable. Each criterion quote must match its cited retrieved passage; criterion IDs are unique. Scope, hierarchy, exclusions, and missing prerequisites are evaluated before classification.

Each report section is `{id, title, sentences}`; each sentence is `{id, text, finding_ids, criterion_ids}`. The eleven section IDs, in order: patient_specimen, component_studies, clinical_context, morphology, flow, cytogenetics, molecular, interpretation, diagnosis, prognostic_predictive, limitations. Every sentence has at least one real finding or criterion reference. Interpretation/diagnosis statements applying classification require criterion references. Do not issue a definitive diagnosis when prerequisites remain unknown; describe uncertainty and missing evidence. Reported interpretation remains attributed separately from derived interpretation. No new scientific interpretation without retrieved source support. Without an explicitly retrieved risk reference, record source-reported prognostic statements as reported, but do not generate a formal risk category. QA checks semantic support as well as reference existence.

## QA

Independent QA receives original page text, structured findings, reference snapshots, integration output, and deterministic flags. Return `flags` array only. Each flag: `{severity: low|medium|high, category: string, concern: string, reference: string}`. Do not rewrite the draft. Unknown/unavailable guidance is a real limitation; a matching quote alone does not establish correct reasoning. A successful schema or deterministic check is not clinical validation. All outputs remain drafts for review.

## Files and command interface

`python -m workflow prepare --out <new-directory>` extracts only case/01 through 04 PDFs, saves page text and run metadata. `sources --out <directory> [--include-risk]` retrieves source snapshots. `run --provider anthropic|openai --model <explicit-model-id> --out <new-directory> [--include-risk]` executes preparation, source retrieval, four extractions, validation, integration and QA. `baseline` uses the same four documents and a general request in one independent call. `validate --run-dir <directory>` rechecks saved evidence. `chat-pack --out <new-directory>` writes platform-neutral prompts for manual use. Outputs, credentials and downloaded references are ignored by Git. API keys are read only from provider environment variables and never printed or persisted.
