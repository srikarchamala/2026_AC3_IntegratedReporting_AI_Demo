# Synthetic teaching draft — human review required

*Synthetic, fictional teaching case. This was produced in stages within one Project conversation. It is not a native Skill installation, not four independent agents, not independent QA, and not clinically validated.*

## Opening summary

| Item | Status |
|---|---|
| **Classification status** | **Insufficient evidence. Derived WHO classification is PAUSED** because the approved WHO source could not be read (see Stage 3). |
| **Source/framework actually consulted** | **None.** I tried to open WHO5E_MYEOID_2022 (Khoury et al., 2022, DOI 10.1038/s41375-022-01613-1) at every approved URL. None returned article text, so no WHO criteria were applied. I did not substitute search snippets or remembered rules. |
| **Key findings (reported)** | One patient (DOE, JONATHAN R.; MRN-4471902; DOB 1967-09-14) appears in all four reports [MORPH-001–003; FLOW-001–003; CYTO-001–003; MOLEC-001–003]. Aspirate blasts are 18% by 500-cell manual differential [MORPH-020]. Flow myeloid blasts are 22% of total nucleated cells [FLOW-022]. Core cellularity is about 90–95%, with sheets of immature cells [MORPH-041, MORPH-042]. Karyotype is 46,XY[20] and the 8-probe AML FISH panel is negative [CYTO-017, CYTO-022–029]. NPM1 c.860_863dup at VAF 39% (Tier I), FLT3-ITD at VAF 31% with ITD/WT ratio 0.62 (Tier I), and DNMT3A p.(Arg882His) at VAF 44% (Tier II) [MOLEC-024–037]. |
| **Source-reported diagnoses (attributed, not derived)** | MORPH: "ACUTE MYELOID LEUKEMIA" [MORPH-050]. FLOW: "acute myeloid leukemia with monocytic differentiation" [FLOW-055]. MOLEC: "acute myeloid leukemia with mutated NPM1" [MOLEC-041]. |
| **Material unresolved issues** | (1) The WHO source has not been read, so classification is paused. (2) Blast percentages differ by method and denominator: 18% manual aspirate, 22% flow TNC, and 41% peripheral smear with method not stated. (3) Promonocyte enumeration differs (4% manual vs 11% flow TNC). (4) The reports' own WHO/ICC statements have not been checked against the source. (5) The full 54-gene list and coverage appendix are not in the MOLEC report. (6) The FISH cutoff values are not stated. |
| **Needed from you** | Please upload the original public article (the PMC9252913 full text or the Nature open-access PDF of DOI 10.1038/s41375-022-01613-1). I will label it as an **uploaded source** and then complete Stages 4–6 for classification. |

---

## Stage status (one Project conversation)

| # | Stage | Status |
|---|---|---|
| 0 | Instruction access and module selection | **Complete.** Only the **Markdown set** is present: eight `Skills_*.md` files plus four PDFs, 12 uploads in total. There are no `.docx` versions, so there are no duplicate module versions to reconcile. I read all eight .md modules in full. They are uploaded workflow documents, not installed native Skills. |
| 1 | Report inventory and identity check | **Complete.** I read all four PDFs in full. Name, MRN and DOB match in all four. Collection date is 2026-04-22 in all four. Accessions differ by laboratory, and MOLEC lists the morphology accession as its client accession. There is no identity conflict. |
| 2 | MORPH, FLOW, CYTO, MOLEC extraction passes | **Complete.** These were four separate passes in this same conversation, each restricted to its own report. MORPH has 59 findings, FLOW 63, CYTO 37 and MOLEC 45. |
| 3 | Actual online WHO source access | **FAILED (access).** No approved URL returned article content. Details are in the source card. |
| 4 | Source-grounded criteria assessment | **Paused.** No criteria could be selected from a retrieved source. |
| 5 | Integrated teaching draft | **Complete for reported/descriptive content.** Sections 8–9 contain no derived WHO classification. |
| 6 | Same-conversation evidence review | **Complete** (same conversation, not independent). Concerns are listed below. |

### Stage 1: Report inventory

| Source ID | Filename | Patient / MRN / DOB | Accession(s) | Performing laboratory | Collected / Reported | Status | Readable locations |
|---|---|---|---|---|---|---|---|
| MORPH | Pathology_Report_1_bone_marrow_morphology.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 | S26-BM-01187 | Riverbend Regional Medical Center, Dept. of Pathology & Laboratory Medicine (CLIA 14D9999999) | 2026-04-22 / 2026-04-24 | FINAL (morphology component) | Physical PDF pp. 1–2. The printed footer says "Page 1 of 1" on physical p. 2, which is a discrepancy. |
| FLOW | Pathology_Report_2_flow_cytometry.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 | FC-26-003942 | Riverbend Regional Medical Center, Flow Cytometry Laboratory (CLIA 14D9999999) | 2026-04-22 / resulted 2026-04-23 | FINAL | Physical PDF pp. 1–2. The printed footer says "Page 1 of 1" on physical p. 2, which is a discrepancy. |
| CYTO | Pathology_Report_3_cytogenetics_fish.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 | CG-26-00871 | Riverbend Regional Medical Center, Cytogenetics Laboratory (CLIA 14D9999999) | 2026-04-22 / 2026-04-29 | FINAL | Physical PDF p. 1 |
| MOLEC | Pathology_Report_4_molecular_ngs.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 | Reference MMD-26-NGS-22150; Client S26-BM-01187 | Meridian Molecular Diagnostics (CLIA 14D8888888) | 2026-04-22 / 2026-05-04 | FINAL | Physical PDF p. 1 |

### Stage 3: WHO source card

| Item | Record |
|---|---|
| Source ID, title, DOI | WHO5E_MYEOID_2022. *The 5th edition of the World Health Organization Classification of Haematolymphoid Tumours: Myeloid and Histiocytic/Dendritic Neoplasms*. Khoury et al. DOI 10.1038/s41375-022-01613-1. **The title and DOI were not checked against an opened document, because no document opened.** |
| Framework and edition/year | WHO 5th edition, public 2022 author overview. This is not the full or latest Blue Book. |
| Access method | **Unavailable** |
| URLs attempted (actual results) | 1. `https://pmc.ncbi.nlm.nih.gov/articles/PMC9252913/`: the web tool refused it as not on the session allowlist. 2. `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9252913/` (from a search result): HTTP 302 redirect to `https://pmc.ncbi.nlm.nih.gov/articles/PMC9252913`, which the tool then refused as not on the allowlist. 3. `https://pmc.ncbi.nlm.nih.gov/articles/9252913/` (from a search result): this returned only a Google reCAPTCHA "Checking your browser" interstitial, with no title, DOI or article text. 4. `https://www.nature.com/articles/s41375-022-01613-1`: refused as not on the allowlist. 5. `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9252913/fullTextXML`: refused as not on the allowlist. |
| Access date | 2026-10-30 |
| Sections/tables read | **None.** I read none of the Introduction, the Acute myeloid leukaemia section, its tables or footnotes, or the secondary myeloid neoplasm context. |
| Limitations | No guideline text is available. Web search result listings showed only titles and links, and they are not retrieved evidence. Some search results pointed to institutional repository copies. They are not approved sources in Skills_7_guideline_sources.md, so I did not use them. I did not attempt to bypass the CAPTCHA or the access restrictions. |

**Request:** Please upload the original public article (the PMC9252913 full text or the Nature open-access PDF). When it is uploaded, I will record it as an *uploaded original*, not as newly retrieved online. I will then read the Introduction, the full AML section with its tables and footnotes, and the relevant secondary myeloid neoplasm context before assessing criteria.

---

## Evidence tables

### MORPH: Pathology_Report_1_bone_marrow_morphology.pdf

*Locations use physical PDF pages. The printed footer reads "Page 1 of 1" but the file has 2 physical pages.*

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| MORPH-001 | Patient identity: name | Reported: DOE, JONATHAN R. | Not applicable | "Patient: DOE, JONATHAN R." (p. 1, header) |
| MORPH-002 | Patient identity: MRN | Reported: MRN-4471902 | Not applicable | "MRN: MRN-4471902" (p. 1, header) |
| MORPH-003 | Patient identity: DOB/age/sex | Reported: 1967-09-14 / 58 y / Male | Not applicable | "DOB / Age / Sex: 1967-09-14 / 58 y / Male" (p. 1, header) |
| MORPH-004 | Study identity: accession | Reported: S26-BM-01187 | Not applicable | "Accession: S26-BM-01187" (p. 1, header) |
| MORPH-005 | Performing laboratory | Reported: Riverbend Regional Medical Center | Not applicable | "Riverbend Regional Medical Center" (p. 1, letterhead) |
| MORPH-006 | Performing laboratory: address/CLIA | Reported: Lakeshore, IL; CLIA 14D9999999 | Not applicable | "1200 Halsted Avenue, Lakeshore, IL 60000 • CLIA 14D9999999" (p. 1, letterhead) |
| MORPH-007 | Dates: collection | Reported: 2026-04-22 | Not applicable | "Collected: 2026-04-22" (p. 1, header) |
| MORPH-008 | Dates: report | Reported: 2026-04-24 | Not applicable | "Reported: 2026-04-24" (p. 1, header) |
| MORPH-009 | Ordering provider | Reported: Patel, Anjali R., MD | Not applicable | "Ordering provider: Patel, Anjali R., MD (Hematology/Oncology)" (p. 1, header) |
| MORPH-010 | Patient location | Reported: Inpatient, 6 West Hematology | Not applicable | "Location: Inpatient — 6 West Hematology" (p. 1, header) |
| MORPH-011 | Report status | Reported: FINAL (morphology component) | Not applicable | "Report status: FINAL (morphology component)." (p. 2, signature block) |
| MORPH-012 | Specimen | Reported: bone marrow, left posterior iliac crest, aspirate and core | Not applicable | "Bone marrow, left posterior iliac crest (aspirate and core biopsy)." (p. 1, Specimen) |
| MORPH-013 | Specimen: preparations | Reported: Wright-Giemsa smears, clot section, decalcified H&E core | Not applicable | "Aspirate smears (Wright-Giemsa), clot section, and decalcified core biopsy (H&E) received." (p. 1, Specimen) |
| MORPH-014 | Specimen: ancillary studies | Reported: submitted under separate accession | Not applicable | "Aspirate also submitted for flow cytometry, cytogenetics, and molecular studies under separate accession." (p. 1, Specimen) |
| MORPH-015 | Clinical history: presentation | Reported | Not applicable | "58-year-old man with three weeks of progressive fatigue, dyspnea on exertion, gingival bleeding, and scattered lower-extremity ecchymoses." (p. 1, Clinical History) |
| MORPH-016 | Clinical history: CBC | Reported: WBC 38.4 x10^9/L; Hb 7.9 g/dL; platelets 31 x10^9/L | Units as stated; CBC on admission | "CBC on admission: WBC 38.4 x10^9/L, hemoglobin 7.9 g/dL, platelets 31 x10^9/L." (p. 1, Clinical History) |
| MORPH-017 | Clinical history: peripheral blood blasts | Reported: 41% circulating blasts | Peripheral smear; count method and denominator not stated | "Peripheral smear with 41% circulating blasts, some with folded nuclei and abundant cytoplasm." (p. 1, Clinical History) |
| MORPH-018 | Clinical history: prior therapy | Reported: no prior hematologic history, chemotherapy, or radiation | Not applicable | "No prior hematologic history, no prior chemotherapy or radiation." (p. 1, Clinical History) |
| MORPH-019 | Specimen adequacy: aspirate | Reported: adequately cellular and spicular | Not applicable | "Smears are adequately cellular and spicular." (p. 1, Microscopic Description) |
| MORPH-020 | Blast measurement: aspirate | Reported: 18% | Manual aspirate differential; 500 cells | "Aspirate blast count 18% by 500-cell manual differential" (p. 1, Diagnosis) |
| MORPH-021 | Other differential populations: promonocytes | Reported: 4% | Aspirate differential, 500-cell count; enumerated separately | "Promonocytes* 4" (p. 1, Aspirate Differential table row; whitespace normalized) |
| MORPH-022 | Other differential populations: promonocytes (footnote) | Reported: enumerated separately; assignment subjective | Not applicable | "* Promonocytes were enumerated separately; their assignment is morphologically subjective and is discussed below." (p. 1, footnote to differential) |
| MORPH-023 | Other differential populations: monocytes (mature) | Reported: 6% | Aspirate differential, 500-cell count | "Monocytes (mature) 6" (p. 1, differential table row; whitespace normalized) |
| MORPH-024 | Other differential populations: promyelocytes | Reported: 3% | Aspirate differential, 500-cell count | "Promyelocytes 3" (p. 1, differential table row; whitespace normalized) |
| MORPH-025 | Other differential populations: myelocytes/metamyelocytes | Reported: 8% | Aspirate differential, 500-cell count | "Myelocytes / metamyelocytes 8" (p. 1, differential table row; whitespace normalized) |
| MORPH-026 | Other differential populations: neutrophils/bands | Reported: 21% | Aspirate differential, 500-cell count | "Neutrophils / bands 21" (p. 1, differential table row; whitespace normalized) |
| MORPH-027 | Other differential populations: eosinophils | Reported: 2% | Aspirate differential, 500-cell count | "Eosinophils 2" (p. 1, differential table row; whitespace normalized) |
| MORPH-028 | Other differential populations: basophils | Reported: 1% | Aspirate differential, 500-cell count | "Basophils 1" (p. 1, differential table row; whitespace normalized) |
| MORPH-029 | Other differential populations: lymphocytes | Reported: 9% | Aspirate differential, 500-cell count | "Lymphocytes 9" (p. 1, differential table row; whitespace normalized) |
| MORPH-030 | Other differential populations: plasma cells | Reported: 1% | Aspirate differential, 500-cell count | "Plasma cells 1" (p. 1, differential table row; whitespace normalized) |
| MORPH-031 | Other differential populations: erythroid precursors | Reported: 14% | Aspirate differential, 500-cell count | "Erythroid precursors 14" (p. 1, differential table row; whitespace normalized) |
| MORPH-032 | Other differential populations: M:E ratio | Reported: ~4.4:1 | Ratio, approximate | "M:E ratio ~4.4:1" (p. 1, differential table row; whitespace normalized) |
| MORPH-033 | Morphology: blasts | Reported: medium-to-large blasts, high N:C, fine chromatin, 1–3 nucleoli | Aspirate smear | "There is a population of medium-to-large blasts with high nuclear-to-cytoplasmic ratio, fine chromatin, and one to three nucleoli." (p. 1, Microscopic Description) |
| MORPH-034 | Morphology: blast subset | Reported: folded/indented nuclei, grayish cytoplasm, fine azurophilic granulation | Aspirate smear | "A subset of blasts shows slightly folded or indented nuclei with moderate amounts of grayish cytoplasm and occasional fine azurophilic granulation" (p. 1, Microscopic Description) |
| MORPH-035 | Morphology: vacuoles | Reported: rare cells with delicate vacuoles | Aspirate smear | "rare cells contain delicate cytoplasmic vacuoles." (p. 1, Microscopic Description) |
| MORPH-036 | Morphology and lineage: monocytoid cells (hedged) | Reported: occasional monocytoid cells; promonocytes difficult to distinguish | Aspirate smear | "Occasional cells with monocytoid features are noted, but unequivocal promonocytes are difficult to distinguish from immature myeloid forms on morphology alone." (p. 1, Microscopic Description) |
| MORPH-037 | Morphology: Auer rods | Negative: no definite Auer rods | Multiple smears reviewed | "No definite Auer rods are identified after review of multiple smears." (p. 1, Microscopic Description) |
| MORPH-038 | Morphology: erythropoiesis | Reported: left-shifted, mild megaloblastoid change | Aspirate | "Erythropoiesis is left-shifted with mild megaloblastoid change." (p. 1, Microscopic Description) |
| MORPH-039 | Morphology: megakaryocytes (aspirate) | Reported: reduced | Aspirate | "Megakaryocytes are reduced." (p. 1, Microscopic Description, Aspirate) |
| MORPH-040 | Cellularity and architecture: core | Reported: markedly hypercellular | Core biopsy | "The core is markedly hypercellular" (p. 1, Microscopic Description, Core biopsy and clot) |
| MORPH-041 | Cellularity and architecture: cellularity estimate | Reported: approximately 90–95% | Core biopsy; percent cellularity (range) | "cellularity approximately 90-95%" (p. 1, Core biopsy and clot) |
| MORPH-042 | Cellularity and architecture: infiltrate | Reported: extensive replacement by immature mononuclear cells in sheets | Core biopsy; no numeric percentage stated | "extensive replacement by immature mononuclear cells arranged in sheets." (p. 1, Core biopsy and clot) |
| MORPH-043 | Cellularity and architecture: distribution | Reported: interstitial and paratrabecular | Core biopsy | "Interstitial and paratrabecular distribution is noted." (p. 1, Core biopsy and clot) |
| MORPH-044 | Cellularity and architecture: residual hematopoiesis | Reported: markedly decreased | Core biopsy | "Residual maturing granulopoiesis and erythropoiesis are present but markedly decreased." (p. 1, Core biopsy and clot) |
| MORPH-045 | Cellularity and architecture: megakaryocytes (core) | Reported: markedly reduced | Core biopsy | "Megakaryocytes are markedly reduced." (p. 1, Core biopsy and clot) |
| MORPH-046 | Special stains: reticulin | Reported: no significant fibrosis (MF-1) | Reticulin stain; MF grade | "Reticulin stain shows no significant fibrosis (MF-1)." (p. 1, Core biopsy and clot) |
| MORPH-047 | Special stains: iron | Reported: storage iron present; no ring sideroblasts | Iron stain on aspirate | "Iron stain (aspirate): storage iron present; no ring sideroblasts." (p. 1, Core biopsy and clot) |
| MORPH-048 | Cytochemistry: MPO | Reported: positive in approximately 5–10% of blasts | MPO cytochemistry; denominator = blasts (approximate range) | "Myeloperoxidase (MPO): positive in a minor subset of blasts (approximately 5-10%)." (p. 1, Cytochemistry) |
| MORPH-049 | Cytochemistry: NSE | Reported: positive in a subset, partial fluoride inhibition | NSE (alpha-naphthyl butyrate); proportion not stated | "Non-specific esterase (NSE, alpha-naphthyl butyrate): positive in a subset of cells with partial fluoride inhibition, supporting a monocytic component." (p. 1, Cytochemistry) |
| MORPH-050 | Source-reported interpretation: diagnosis | Source-reported interpretation: AML | Not applicable | "HYPERCELLULAR MARROW WITH ACUTE MYELOID LEUKEMIA (see comment)." (p. 1, Diagnosis) |
| MORPH-051 | Source-reported interpretation: core | Source-reported interpretation: extensive blast-equivalent infiltration | Core biopsy; no numeric value | "core biopsy with extensive blast-equivalent infiltration." (p. 1, Diagnosis) |
| MORPH-052 | Source-reported interpretation: lineage (hedged/pending) | Source-reported interpretation: probable monocytic differentiation, to be confirmed by flow | Morphology and cytochemistry | "Probable monocytic differentiation by morphology and cytochemistry; to be confirmed by flow cytometry." (p. 2, Diagnosis continued) |
| MORPH-053 | Source-reported interpretation: cytochemistry pattern | Source-reported interpretation: myeloid process with probable monocytic differentiation | Not applicable | "The combined pattern is consistent with a myeloid process with probable monocytic differentiation; correlation with flow cytometry is recommended." (p. 1, Cytochemistry) |
| MORPH-054 | Source-reported interpretation: blast threshold comment | Source-reported interpretation: 18% below historical 20% threshold; core infiltration exceeds it; PB 41% | Not applicable | "The manual aspirate blast percentage (18%) is below the historical 20% threshold; however, the core biopsy demonstrates extensive infiltration by immature cells well in excess of that proportion, and the peripheral blood blast count is 41%." (p. 2, Comment) |
| MORPH-055 | Limitations: aspirate enumeration | Source-reported limitation: hemodilution; promonocyte/blast separation difficulty | Not applicable | "Aspirate enumeration is likely affected by hemodilution and by the difficulty of separating promonocytes from myeloid blasts on smears." (p. 2, Comment) |
| MORPH-056 | Source-reported interpretation: classification statement (WHO/ICC claim; not guideline evidence) | Source-reported interpretation; classification deferred to ancillary studies | Not applicable | "Under current WHO and ICC classifications, a diagnosis of acute myeloid leukemia does not require a 20% blast count when a defining genetic abnormality is present; classification will therefore depend on integration with flow cytometry, cytogenetic, and molecular results, which are pending at the time of this report." (p. 2, Comment) |
| MORPH-057 | Immunohistochemistry | Not reported | Not stated | No supporting statement located. |
| MORPH-058 | Signatories | Reported: Marcus T. Whitfield, MD; fellow review K. Aboud, MD | Not applicable | "Electronically signed: Marcus T. Whitfield, MD — Hematopathology." (p. 2, signature block) |
| MORPH-059 | Report context: page-label discrepancy | Reported footer "Page 1 of 1" on 2-page PDF | Physical pages cited throughout | "Page 1 of 1 • Accession S26-BM-01187 • MRN-4471902" (physical p. 2, footer) |

### FLOW: Pathology_Report_2_flow_cytometry.pdf

*Locations use physical PDF pages. The printed footer reads "Page 1 of 1" but the file has 2 physical pages.*

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| FLOW-001 | Patient identity: name | Reported: DOE, JONATHAN R. | Not applicable | "DOE, JONATHAN R." (p. 1, Patient block) |
| FLOW-002 | Patient identity: MRN | Reported: MRN-4471902 | Not applicable | "MRN MRN-4471902" (p. 1, Patient block) |
| FLOW-003 | Patient identity: DOB/age/sex | Reported: 1967-09-14, 58 y, Male | Not applicable | "DOB 1967-09-14 58 y / Male" (p. 1, Patient block) |
| FLOW-004 | Study identity: accession | Reported: FC-26-003942 | Not applicable | "Accession FC-26-003942" (physical p. 2, footer); also "FC-26-003942" (p. 1, Specimen block) |
| FLOW-005 | Specimen | Reported: bone marrow aspirate | Not applicable | "Bone marrow aspirate" (p. 1, Specimen block) |
| FLOW-006 | Dates: collected | Reported: 2026-04-22 | Not applicable | "Collected 2026-04-22" (p. 1, Specimen block) |
| FLOW-007 | Dates: received | Reported: 2026-04-22 17:40 | Not applicable | "Received 2026-04-22 17:40" (p. 1, Specimen block) |
| FLOW-008 | Dates: resulted | Reported: 2026-04-23 | Not applicable | "Resulted 2026-04-23" (p. 1, Reporting block) |
| FLOW-009 | Report status | Reported: FINAL | Not applicable | "Status: FINAL" (p. 1, Reporting block) |
| FLOW-010 | Priority | Reported: STAT | Not applicable | "Priority: STAT" (p. 1, Reporting block) |
| FLOW-011 | Ordering provider | Reported: A. Patel, MD | Not applicable | "Ordering: A. Patel, MD" (p. 1, Reporting block) |
| FLOW-012 | Performing laboratory | Reported: Riverbend Regional Medical Center, Flow Cytometry Laboratory, CLIA 14D9999999 | Not applicable | "FLOW CYTOMETRY LABORATORY" (p. 1, letterhead); "CLIA 14D9999999" (p. 1, letterhead) |
| FLOW-013 | Clinical history: presentation | Reported | Not applicable | "58-year-old man with three weeks of progressive fatigue, dyspnea on exertion, gingival bleeding, and scattered lower-extremity ecchymoses." (p. 1, Clinical History / Indication) |
| FLOW-014 | Clinical history: CBC | Reported: WBC 38.4 x10^9/L; Hb 7.9 g/dL; platelets 31 x10^9/L | Units as stated | "CBC on admission: WBC 38.4 x10^9/L, hemoglobin 7.9 g/dL, platelets 31 x10^9/L." (p. 1, Clinical History / Indication) |
| FLOW-015 | Clinical history: peripheral blood blasts | Reported: 41% | Peripheral smear; method/denominator not stated | "Peripheral smear with 41% circulating blasts" (p. 1, Clinical History / Indication) |
| FLOW-016 | Clinical history: prior therapy | Reported: none | Not applicable | "No prior hematologic history, no prior chemotherapy or radiation." (p. 1, Clinical History / Indication) |
| FLOW-017 | Specimen adequacy: viability | Reported: 94% | 7-AAD | "viability 94% by 7-AAD" (p. 1, Specimen Adequacy & Method) |
| FLOW-018 | Gating and method: panel/acquisition | Reported: 8-color panel, 3-laser, ≥100,000 events/tube | Events per tube | "Eight-color panel acquired on a 3-laser cytometer (≥100,000 events per tube)." (p. 1, Specimen Adequacy & Method) |
| FLOW-019 | Gating and method: preparation | Reported: lysis/no-wash | Not applicable | "Lysis/no-wash technique." (p. 1, Specimen Adequacy & Method) |
| FLOW-020 | Gating and method: blast gate | Reported: CD45 vs SSC; CD45-dim/intermediate, low SSC | Sequential gating | "Analysis by sequential gating (CD45 vs side scatter) with blast gate defined by CD45-dim/intermediate, low side scatter events." (p. 1, Specimen Adequacy & Method) |
| FLOW-021 | Population measurements: denominator | Reported: % of total nucleated cells | % TNC | "POPULATION SUMMARY (% of total nucleated cells)" (p. 1, heading) |
| FLOW-022 | Population: myeloid blasts (measurement) | Reported: 22%; discrete abnormal population | % TNC | "Myeloid blasts (CD45-dim, low SSC, CD34+/CD117+) 22% Discrete abnormal population" (p. 1, Population Summary row; whitespace normalized) |
| FLOW-023 | Population: maturing monocytes (measurement) | Reported: 19%; expanded, left-shifted | % TNC | "Maturing monocytes (CD14+/CD64+/CD11b+) 19% Expanded; left-shifted" (p. 1, Population Summary row; whitespace normalized) |
| FLOW-024 | Population: promonocytes / immature monocytic (measurement) | Reported: 11%; counted with monocytic series | % TNC | "Promonocytes / immature monocytic (CD64+, CD14-dim/var, HLA-DR+) 11% Counted with monocytic series" (p. 1, Population Summary row; whitespace normalized) |
| FLOW-025 | Population: maturing granulocytes | Reported: 28%; decreased, left-shifted | % TNC | "Maturing granulocytes 28% Decreased, left-shifted" (p. 1, Population Summary row; whitespace normalized) |
| FLOW-026 | Population: erythroid precursors | Reported: 9%; decreased | % TNC | "Erythroid precursors (CD71+/CD235a+) 9% Decreased" (p. 1, Population Summary row; whitespace normalized) |
| FLOW-027 | Population: mature lymphocytes | Reported: 8%; polytypic, no aberrancy | % TNC | "Mature lymphocytes (T/B/NK) 8% Polytypic, no aberrancy" (p. 1, Population Summary row; whitespace normalized) |
| FLOW-028 | Population: other/unclassified | Reported: 3% | % TNC | "Other / unclassified 3%" (p. 1, Population Summary row; whitespace normalized) |
| FLOW-029 | Myeloid blasts (immunophenotype): CD34 | Positive (subset, ~60%) | Blast gate; ~60% of blasts | "CD34 Positive (subset, ~60%)" (p. 1, Blast Gate Immunophenotype; whitespace normalized) |
| FLOW-030 | Myeloid blasts (immunophenotype): CD117 | Positive | Blast gate | "CD117 Positive" (p. 1, Blast Gate Immunophenotype) |
| FLOW-031 | Myeloid blasts (immunophenotype): HLA-DR | Positive (bright) | Blast gate | "HLA-DR Positive (bright)" (p. 1, Blast Gate Immunophenotype) |
| FLOW-032 | Myeloid blasts (immunophenotype): CD13 | Positive | Blast gate | "CD13 Positive" (p. 1, Blast Gate Immunophenotype) |
| FLOW-033 | Myeloid blasts (immunophenotype): CD33 | Positive (bright) | Blast gate | "CD33 Positive (bright)" (p. 1, Blast Gate Immunophenotype) |
| FLOW-034 | Myeloid blasts (immunophenotype): CD38 | Positive | Blast gate | "CD38 Positive" (p. 1, Blast Gate Immunophenotype) |
| FLOW-035 | Myeloid blasts (immunophenotype): MPO (cyto) | Positive, dim subset | Blast gate; cytoplasmic | "MPO (cyto) Positive, dim subset" (p. 1, Blast Gate Immunophenotype) |
| FLOW-036 | Myeloid blasts (immunophenotype): CD64 | Positive | Blast gate | "CD64 Positive" (p. 1, Blast Gate Immunophenotype) |
| FLOW-037 | Myeloid blasts (immunophenotype): CD4 | Positive (dim) | Blast gate | "CD4 Positive (dim)" (p. 1, Blast Gate Immunophenotype) |
| FLOW-038 | Myeloid blasts (immunophenotype): CD11b | Partial / variable | Blast gate | "CD11b Partial / variable" (p. 1, Blast Gate Immunophenotype) |
| FLOW-039 | Myeloid blasts (immunophenotype): CD14 | Negative on blasts | Blast gate | "CD14 Negative on blasts" (p. 1, Blast Gate Immunophenotype) |
| FLOW-040 | Myeloid blasts (immunophenotype): CD56 | Positive (partial, aberrant) | Blast gate | "CD56 Positive (partial, aberrant)" (p. 1, Blast Gate Immunophenotype) |
| FLOW-041 | Myeloid blasts (immunophenotype): CD7 | Positive (aberrant, subset) | Blast gate | "CD7 Positive (aberrant, subset)" (p. 1, Blast Gate Immunophenotype) |
| FLOW-042 | Myeloid blasts (immunophenotype): CD2 / CD19 / cyCD3 | Negative | Blast gate | "CD2 / CD19 / cyCD3 Negative" (p. 1, Blast Gate Immunophenotype) |
| FLOW-043 | Monocytic population (immunophenotype): CD14 | Positive (maturing fraction) | Monocytic population; sub-gate not otherwise stated | "CD14 Positive (maturing fraction)" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-044 | Monocytic population (immunophenotype): CD64 | Positive (bright, uniform) | Monocytic population | "CD64 Positive (bright, uniform)" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-045 | Monocytic population (immunophenotype): CD11b | Positive | Monocytic population | "CD11b Positive" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-046 | Monocytic population (immunophenotype): CD11c | Positive | Monocytic population | "CD11c Positive" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-047 | Monocytic population (immunophenotype): CD36 | Positive | Monocytic population | "CD36 Positive" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-048 | Monocytic population (immunophenotype): HLA-DR | Positive | Monocytic population | "HLA-DR Positive" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-049 | Monocytic population (immunophenotype): CD4 | Positive (dim) | Monocytic population | "CD4 Positive (dim)" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-050 | Monocytic population (immunophenotype): CD13 / CD33 | Positive | Monocytic population | "CD13 / CD33 Positive" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-051 | Monocytic population (immunophenotype): CD34 | Negative | Monocytic population | "CD34 Negative" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-052 | Monocytic population (immunophenotype): CD56 | Partial (subset) | Monocytic population | "CD56 Partial (subset)" (p. 1, Monocytic Population Immunophenotype) |
| FLOW-053 | Myeloid blasts: source-reported interpretation | Source-reported interpretation: abnormal myeloid blasts ~22% TNC with aberrant CD56, partial CD7 | % TNC (approximate) | "Flow cytometry demonstrates an abnormal myeloid blast population comprising approximately 22% of total nucleated cells" (p. 1, Interpretation) |
| FLOW-054 | Monocytic population: source-reported combined value | Source-reported: maturing monocytes + promonocytes ~30% TNC (sum stated by source) | % TNC (approximate) | "maturing monocytes plus promonocytes together approximately 30% of total nucleated cells" (p. 1, Interpretation) |
| FLOW-055 | Lineage and interpretation: diagnosis | Source-reported interpretation: AML with monocytic differentiation | Not applicable | "The combined findings are diagnostic of acute myeloid leukemia with monocytic differentiation." (p. 2, Interpretation continued) |
| FLOW-056 | Lineage and interpretation: lineage | Source-reported interpretation: monocytic lineage established | Not applicable | "The immunophenotype establishes the monocytic lineage that was only favored on morphology." (p. 2, Interpretation) |
| FLOW-057 | Lineage and interpretation: blast-estimate discrepancy | Source-reported interpretation: flow 22% differs from manual differential | Not applicable | "Note that the flow blast estimate (22%) differs modestly from the manual aspirate differential; flow gating and manual counts are expected to differ and either value supports the diagnosis in this context." (p. 2, Interpretation) |
| FLOW-058 | Lineage and interpretation: MRD comment | Source-reported interpretation | Not applicable | "Aberrant CD56/CD7 expression is noted and may be useful for measurable residual disease tracking." (p. 2, Interpretation) |
| FLOW-059 | Limitations: classification pending | Source-reported: correlation with cytogenetic/molecular required | Not applicable | "Correlation with cytogenetic and molecular studies is required for final classification and is recommended." (p. 2, Interpretation) |
| FLOW-060 | Gating and method: test status | Reported: laboratory-developed test | Not applicable | "Method: laboratory-developed test, performance characteristics established by Riverbend Regional Medical Center." (p. 2, footer note) |
| FLOW-061 | Signatory | Reported: Priya N. Raghavan, MD, 2026-04-23 14:08 | Not applicable | "Electronically verified by Priya N. Raghavan, MD, Director of Flow Cytometry, 2026-04-23 14:08." (p. 2, footer note) |
| FLOW-062 | Gating: relationship of promonocyte population to blast gate | Not stated | Not stated | No supporting statement located. The report does not say whether the 11% promonocyte gate overlaps the 22% blast gate. |
| FLOW-063 | Report context: page-label discrepancy | Reported footer "Page 1 of 1" on 2-page PDF | Physical pages cited | "Accession FC-26-003942 \| MRN-4471902 \| Page 1 of 1" (physical p. 2, footer) |

### CYTO: Pathology_Report_3_cytogenetics_fish.pdf

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| CYTO-001 | Patient identity: name | Reported: DOE, JONATHAN R. | Not applicable | "Patient: DOE, JONATHAN R." (p. 1, header) |
| CYTO-002 | Patient identity: MRN | Reported: MRN-4471902 | Not applicable | "MRN: MRN-4471902" (p. 1, header) |
| CYTO-003 | Patient identity: DOB | Reported: 1967-09-14 (58 y / Male) | Not applicable | "DOB: 1967-09-14 (58 y / Male)" (p. 1, header) |
| CYTO-004 | Study identity: accession | Reported: CG-26-00871 | Not applicable | "Accession: CG-26-00871" (p. 1, header) |
| CYTO-005 | Dates: collected | Reported: 2026-04-22 | Not applicable | "Collected: 2026-04-22" (p. 1, header) |
| CYTO-006 | Dates: reported | Reported: 2026-04-29 | Not applicable | "Reported: 2026-04-29" (p. 1, header) |
| CYTO-007 | Specimen | Reported: bone marrow aspirate | Not applicable | "Specimen: Bone marrow aspirate" (p. 1, header) |
| CYTO-008 | Report status | Reported: FINAL | Not applicable | "Status: FINAL" (p. 1, header) |
| CYTO-009 | Ordering provider | Reported: A. Patel, MD | Not applicable | "Ordering: A. Patel, MD" (p. 1, header) |
| CYTO-010 | Performing laboratory | Reported: Riverbend Regional Medical Center Cytogenetics Laboratory, CLIA 14D9999999 | Not applicable | "CYTOGENETICS LABORATORY — Department of Pathology & Laboratory Medicine" (p. 1, letterhead) |
| CYTO-011 | Clinical indication | Reported (same text as other reports, incl. PB 41% blasts, no prior chemo/radiation) | Not applicable | "No prior hematologic history, no prior chemotherapy or radiation." (p. 1, Clinical Indication) |
| CYTO-012 | Karyotype analysis: tissue | Reported: bone marrow, unstimulated | Not applicable | "Bone marrow, unstimulated" (p. 1, Conventional Chromosome Analysis table) |
| CYTO-013 | Karyotype analysis: cultures | Reported: 24-hour and 48-hour, synchronized | Not applicable | "24-hour and 48-hour, synchronized" (p. 1, Conventional Chromosome Analysis table) |
| CYTO-014 | Karyotype analysis: cells counted | Reported: 20 | Metaphase cells | "Cells counted 20" (p. 1, table; whitespace normalized) |
| CYTO-015 | Karyotype analysis: cells karyotyped | Reported: 5 | Metaphase cells | "Cells karyotyped 5" (p. 1, table; whitespace normalized) |
| CYTO-016 | Karyotype analysis: resolution | Reported: 400–425 bphs | Bands per haploid set | "Band resolution 400-425 bphs" (p. 1, table; whitespace normalized) |
| CYTO-017 | Karyotype: ISCN | Reported: 46,XY[20] | G-banding; 20 metaphases | "46,XY[20]" (p. 1, ISCN Result) |
| CYTO-018 | Karyotype: description | Negative: no clonal numerical/structural abnormality at stated resolution | 20 analyzed, 5 karyotyped; 400–425 bphs | "No clonal numerical or structural abnormality was identified at the stated band resolution." (p. 1, ISCN Result) |
| CYTO-019 | Assay scope: karyotype limitation | Source-reported limitation | Not applicable | "A normal karyotype does not exclude a submicroscopic abnormality; correlation with FISH and molecular studies is advised." (p. 1, ISCN Result) |
| CYTO-020 | FISH: method | Reported: interphase FISH, cultured marrow, AML panel | Not applicable | "Interphase FISH performed on cultured bone marrow using the acute myeloid leukemia panel." (p. 1, FISH) |
| CYTO-021 | FISH: nuclei scored | Reported: 200 per probe | Interphase nuclei per probe | "200 interphase nuclei scored per probe." (p. 1, FISH) |
| CYTO-022 | FISH target: RUNX1-RUNX1T1, t(8;21)(q22;q22) | Negative; 0.5% | % of 200 nuclei | "RUNX1-RUNX1T1 t(8;21)(q22;q22) NEGATIVE 0.5%" (p. 1, FISH table; whitespace normalized) |
| CYTO-023 | FISH target: CBFB, inv(16)/t(16;16)(p13;q22) | Negative; 1.0% | % of 200 nuclei | "CBFB inv(16)/t(16;16)(p13;q22) NEGATIVE 1.0%" (p. 1, FISH table; whitespace normalized) |
| CYTO-024 | FISH target: PML-RARA, t(15;17)(q24;q21) | Negative; 0.5% | % of 200 nuclei | "PML-RARA t(15;17)(q24;q21) NEGATIVE 0.5%" (p. 1, FISH table; whitespace normalized) |
| CYTO-025 | FISH target: KMT2A (MLL), 11q23.3 rearrangement | Negative; 1.5% | % of 200 nuclei | "KMT2A (MLL) 11q23.3 rearrangement NEGATIVE 1.5%" (p. 1, FISH table; whitespace normalized) |
| CYTO-026 | FISH target: MECOM (EVI1), 3q26.2 rearrangement | Negative; 1.0% | % of 200 nuclei | "MECOM (EVI1) 3q26.2 rearrangement NEGATIVE 1.0%" (p. 1, FISH table; whitespace normalized) |
| CYTO-027 | FISH target: -5/5q- (EGR1), deletion 5q31 | Negative; 1.5% | % of 200 nuclei | "-5/5q- (EGR1) deletion 5q31 NEGATIVE 1.5%" (p. 1, FISH table; whitespace normalized) |
| CYTO-028 | FISH target: -7/7q- (D7S486), monosomy 7 / del(7q) | Negative; 1.0% | % of 200 nuclei | "-7/7q- (D7S486) monosomy 7 / del(7q) NEGATIVE 1.0%" (p. 1, FISH table; whitespace normalized) |
| CYTO-029 | FISH target: TP53 (17p13.1), deletion 17p | Negative; 2.0% | % of 200 nuclei | "TP53 (17p13.1) deletion 17p NEGATIVE 2.0%" (p. 1, FISH table; whitespace normalized) |
| CYTO-030 | FISH: cutoff statement | Reported: all within laboratory normal cutoff range | Lab-established cutoff | "All probe signal counts were within the laboratory's established normal cutoff range." (p. 1, below FISH table) |
| CYTO-031 | FISH: numeric cutoff values | Not reported | Not stated | No supporting statement located. |
| CYTO-032 | Other reported assays (e.g., microarray) | Not reported | Not stated | No supporting statement located. |
| CYTO-033 | Interpretation: overall | Source-reported interpretation: normal male karyotype, negative AML FISH panel | Not applicable | "Normal male karyotype (46,XY) with a negative AML FISH panel." (p. 1, Interpretation) |
| CYTO-034 | Interpretation: recurrent abnormality (scope-limited) | Source-reported interpretation: none detected by either method | Limited to karyotype resolution and listed FISH targets | "No recurrent cytogenetic abnormality of acute myeloid leukemia was detected by either method." (p. 1, Interpretation) |
| CYTO-035 | Interpretation: category | Source-reported interpretation: cytogenetically normal | Not applicable | "This places the case in the cytogenetically normal category." (p. 1, Interpretation) |
| CYTO-036 | Interpretation: molecular pending/ordered | Source-reported: molecular testing required; ordered under MMD-26-NGS-22150 | Not applicable | "has been ordered separately (see accession MMD-26-NGS-22150)." (p. 1, Interpretation) |
| CYTO-037 | Signatory | Reported: Helena V. Brandt, PhD, FACMG, 2026-04-29 | Not applicable | "Reviewed and electronically signed by Helena V. Brandt, PhD, FACMG, Director of Cytogenetics, 2026-04-29." (p. 1, signature block) |

### MOLEC: Pathology_Report_4_molecular_ngs.pdf

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| MOLEC-001 | Patient identity: name | Reported: DOE, JONATHAN R. | Not applicable | "DOE, JONATHAN R." (p. 1, Patient block) |
| MOLEC-002 | Patient identity: MRN/DOB | Reported: MRN-4471902; 1967-09-14 | Not applicable | "MRN MRN-4471902 \| DOB 1967-09-14" (p. 1, Patient block) |
| MOLEC-003 | Patient identity: age/sex | Reported: 58 y / Male | Not applicable | "58 y / Male" (p. 1, Patient block) |
| MOLEC-004 | Study identity: reference accession | Reported: MMD-26-NGS-22150 | Not applicable | "Reference accession MMD-26-NGS-22150" (p. 1, Specimen block) |
| MOLEC-005 | Study identity: client accession | Reported: S26-BM-01187 | Not applicable | "Client accession S26-BM-01187" (p. 1, Specimen block) |
| MOLEC-006 | Specimen | Reported: bone marrow aspirate, EDTA | Not applicable | "Bone marrow aspirate, EDTA" (p. 1, Specimen block) |
| MOLEC-007 | Dates: collected | Reported: 2026-04-22 | Not applicable | "Collected 2026-04-22" (p. 1, Specimen block) |
| MOLEC-008 | Dates: received | Reported: 2026-04-25 | Not applicable | "Received 2026-04-25" (p. 1, Requested By block) |
| MOLEC-009 | Dates: reported | Reported: 2026-05-04 | Not applicable | "Reported 2026-05-04" (p. 1, Requested By block) |
| MOLEC-010 | Performing laboratory | Reported: Meridian Molecular Diagnostics | Not applicable | "validated by Meridian Molecular Diagnostics" (p. 1, Methodology & Limitations) |
| MOLEC-011 | Performing laboratory: CLIA/director | Reported: CLIA 14D8888888; Okafor, Daniel U., MD, PhD | Not applicable | "CLIA 14D8888888 • Lab Director: Okafor, Daniel U., MD, PhD" (p. 1, letterhead) |
| MOLEC-012 | Requesting institution | Reported: Riverbend Regional Medical Center; A. Patel, MD | Not applicable | "Riverbend Regional Medical Center" (p. 1, Requested By block) |
| MOLEC-013 | Report status | Reported: FINAL REPORT | Not applicable | "MYELOID NEOPLASM NEXT-GENERATION SEQUENCING PANEL (54-GENE) — FINAL REPORT" (p. 1, title) |
| MOLEC-014 | Clinical history | Reported (provided by ordering site; same text, incl. no prior chemo/radiation) | Not applicable | "CLINICAL HISTORY (PROVIDED BY ORDERING SITE)" (p. 1, heading) |
| MOLEC-015 | Assay and scope: assay | Reported: 54-gene myeloid NGS panel | Not applicable | "MYELOID NEOPLASM NEXT-GENERATION SEQUENCING PANEL (54-GENE)" (p. 1, title) |
| MOLEC-016 | Assay and scope: method | Reported: hybrid-capture targeted NGS, genomic DNA | Not applicable | "Hybrid-capture targeted NGS of 54 myeloid-associated genes performed on genomic DNA from bone marrow." (p. 1, Methodology & Limitations) |
| MOLEC-017 | Assay and scope: coverage | Reported: mean 1,150x; minimum 250x | Read depth | "Mean target coverage 1,150x; minimum 250x." (p. 1, Methodology & Limitations) |
| MOLEC-018 | Assay and scope: sensitivity | Reported: ~5% VAF for SNVs and small indels | VAF | "Analytical sensitivity approximately 5% VAF for single-nucleotide variants and small indels" (p. 1, Methodology & Limitations) |
| MOLEC-019 | Assay and scope: FLT3-ITD method | Reported: supplemented by capillary fragment analysis | Not applicable | "FLT3-ITD detection supplemented by capillary fragment analysis." (p. 1, Methodology & Limitations) |
| MOLEC-020 | Limitations: structural/CNV | Source-reported limitation | Not applicable | "The assay does not reliably detect large structural rearrangements, copy-number changes, or variants in regions of low coverage or high homology." (p. 1, Methodology & Limitations) |
| MOLEC-021 | Limitations: limit of detection | Source-reported limitation | Not applicable | "A negative result does not exclude a mutation below the limit of detection." (p. 1, Methodology & Limitations) |
| MOLEC-022 | Limitations: regulatory status | Reported: LDT, not FDA cleared/approved | Not applicable | "it has not been cleared or approved by the FDA." (p. 1, Methodology & Limitations) |
| MOLEC-023 | Assay and scope: overall result | Reported: POSITIVE | Not applicable | "POSITIVE — Clinically significant variants detected." (p. 1, Result Summary) |
| MOLEC-024 | Variant group 1 (NPM1): identity | Reported: NM_002520.7:c.860_863dup p.(Trp288CysfsTer12) | HGVS; transcript NM_002520.7 | "NPM1 NM_002520.7:c.860_863dup" (p. 1, Detected Variants; whitespace normalized); "p.(Trp288CysfsTer12)" (p. 1, same row) |
| MOLEC-025 | Variant group 1 (NPM1): consequence | Reported: frameshift insertion (type A, 4-bp TCTG duplication) | Not applicable | "Frameshift insertion (type A, 4-bp TCTG duplication)" (p. 1, Detected Variants; table cell spans two lines) |
| MOLEC-026 | Variant group 1 (NPM1): VAF | Reported: 39% | VAF, NGS | "39%" (p. 1, Detected Variants, NPM1 row); "type A frameshift insertion, VAF 39%" (p. 1, Interpretation) |
| MOLEC-027 | Variant group 1 (NPM1): tier | Reported: Tier I | Lab tiering | "NPM1 (Tier I)" (p. 1, Result Summary) |
| MOLEC-028 | Variant group 2 (FLT3): identity | Reported: internal tandem duplication, exon 14 (~36 bp insertion) | Not applicable | "Internal tandem duplication, exon 14 (~36 bp insertion)" (p. 1, Detected Variants; cell spans two lines) |
| MOLEC-029 | Variant group 2 (FLT3): transcript/HGVS | Not reported | Not stated | No supporting statement located. |
| MOLEC-030 | Variant group 2 (FLT3): consequence | Reported: in-frame ITD | Not applicable | "In-frame ITD;" (p. 1, Detected Variants) |
| MOLEC-031 | Variant group 2 (FLT3): VAF | Reported: 31% | VAF, NGS | "FLT3 internal tandem duplication (VAF 31%, ITD/WT allelic ratio 0.62)" (p. 1, Interpretation) |
| MOLEC-032 | Variant group 2 (FLT3): allelic ratio | Reported: ITD/WT 0.62 | Ratio; capillary fragment analysis run in parallel | "FLT3-ITD allelic ratio estimated by fragment analysis run in parallel." (p. 1, table footnote); "ITD/WT allelic ratio 0.62" (p. 1, Detected Variants) |
| MOLEC-033 | Variant group 2 (FLT3): tier | Reported: Tier I | Lab tiering | "FLT3 internal tandem duplication (Tier I)" (p. 1, Result Summary) |
| MOLEC-034 | Variant group 3 (DNMT3A): identity | Reported: NM_022552.5:c.2645G>A p.(Arg882His) | HGVS; transcript NM_022552.5 | "DNMT3A NM_022552.5:c.2645G>A" (p. 1, Detected Variants; whitespace normalized); "p.(Arg882His)" (p. 1, same row) |
| MOLEC-035 | Variant group 3 (DNMT3A): consequence | Reported: missense, R882 hotspot | Not applicable | "Missense, R882 hotspot" (p. 1, Detected Variants) |
| MOLEC-036 | Variant group 3 (DNMT3A): VAF | Reported: 44% | VAF, NGS | "a DNMT3A R882H missense variant (VAF 44%)" (p. 1, Interpretation) |
| MOLEC-037 | Variant group 3 (DNMT3A): tier | Reported: Tier II | Lab tiering | "DNMT3A (Tier II)" (p. 1, Result Summary) |
| MOLEC-038 | Source annotations: tier definitions | Reported | Not applicable | "Tier I: variants of strong clinical significance. Tier II: variants of potential clinical significance." (p. 1, table footnote) |
| MOLEC-039 | Assay scope: selected genes with no reportable variant | Negative within tested scope (≥~5% VAF LOD): CEBPA, RUNX1, TP53, ASXL1, IDH1, IDH2, NRAS, KRAS, KIT, TET2, SRSF2, U2AF1, SF3B1, EZH2, BCOR, STAG2, PTPN11, WT1, PHF6, ZRSR2, JAK2, CALR, MPL, SETBP1, CSF3R, NF1, RAD21, GATA2, ETV6, CBL | Targeted NGS; subject to MOLEC-018, -020, -021 | "No reportable variant detected in: CEBPA, RUNX1, TP53, ASXL1, IDH1, IDH2, NRAS, KRAS, KIT, TET2, SRSF2, U2AF1, SF3B1, EZH2, BCOR, STAG2, PTPN11, WT1, PHF6, ZRSR2, JAK2, CALR, MPL, SETBP1, CSF3R, NF1, RAD21, GATA2, ETV6, CBL." (p. 1, Selected Genes With No Reportable Variant) |
| MOLEC-040 | Assay scope: full gene list / coverage metrics | Not reported in this document (retained by laboratory) | Not stated | "(Full 54-gene list and coverage metrics in appendix retained by the laboratory.)" (p. 1, Selected Genes section) |
| MOLEC-041 | Reported implications: diagnosis | Source-reported interpretation: AML with mutated NPM1; 20% blast threshold not required | Not applicable | "the diagnosis is therefore acute myeloid leukemia with mutated NPM1, and a blast threshold of 20% is not required for this entity." (p. 1, Interpretation) |
| MOLEC-042 | Reported implications: WHO/ICC claim (not guideline evidence) | Source-reported interpretation: NPM1 disease-defining | Not applicable | "mutated NPM1 is a World Health Organization and ICC disease-defining genetic abnormality" (p. 1, Interpretation) |
| MOLEC-043 | Reported implications: FLT3-ITD | Source-reported interpretation: prognostically adverse; FLT3-inhibitor target | Not applicable | "The concurrent FLT3-ITD is prognostically adverse and is a target for FLT3 inhibitor therapy" (p. 1, Interpretation) |
| MOLEC-044 | Reported implications: DNMT3A | Source-reported interpretation: often clonal hematopoiesis founder; does not define/change WHO/ICC category | Not applicable | "it does not by itself define or change the WHO/ICC disease category, and is reported here for completeness and potential prognostic relevance." (p. 1, Interpretation) |
| MOLEC-045 | Signatories | Reported: Okafor, Daniel U., MD, PhD; Lucia M. Fernandez, PhD, 2026-05-04 | Not applicable | "Electronically signed: Okafor, Daniel U., MD, PhD, Laboratory Director, and Lucia M. Fernandez, PhD, Variant Scientist — 2026-05-04." (p. 1, signature block) |

---

## Stage 4: Criteria assessment (paused)

| Criterion ID | Criterion in plain language | Source / section / table | Brief supporting excerpt or precise citation | Case finding IDs | Assessment | Reason / missing evidence |
|---|---|---|---|---|---|---|
| — | **No criteria selected.** | WHO5E_MYEOID_2022: **not read** | None. No source text was retrieved. | — | — | Criteria must come from the actual retrieved Introduction, AML section, tables, footnotes and scope. I did not encode criteria from memory. This table will be filled once the original article is uploaded. |

**Report claims to check against the source once it is available.** These are patient-report statements, not guideline evidence:
- MORPH says WHO/ICC do not require 20% blasts when a defining genetic abnormality is present [MORPH-056].
- MOLEC says mutated NPM1 is WHO/ICC disease-defining and that 20% blasts are not required [MOLEC-041, MOLEC-042].
- MOLEC says DNMT3A does not change the WHO/ICC category [MOLEC-044].
- FLOW says AML with monocytic differentiation [FLOW-055].
- Applicability of the clinical history (no prior chemotherapy or radiation) [MORPH-018] and of the absence of a reported recurrent cytogenetic abnormality in the tested scope [CYTO-034] must be judged against whatever prerequisites and exclusions the retrieved source states.

---

## Integrated draft

**Synthetic teaching draft — human review required**

### 1. Patient and specimen
DOE, JONATHAN R., MRN-4471902, DOB 1967-09-14, 58-year-old male [MORPH-001–003; FLOW-001–003; CYTO-001–003; MOLEC-001–003]. Bone marrow from the left posterior iliac crest, aspirate and core biopsy, collected 2026-04-22 [MORPH-012, MORPH-007; FLOW-006; CYTO-005; MOLEC-007]. Ancillary studies used bone marrow aspirate [FLOW-005; CYTO-007; MOLEC-006]. Identity matches across all four reports.

### 2. Component studies, accessions, and laboratories
- Morphology: S26-BM-01187, Riverbend Regional Medical Center, reported 2026-04-24, FINAL (morphology component) [MORPH-004–006, MORPH-008, MORPH-011].
- Flow cytometry: FC-26-003942, Riverbend Flow Cytometry Laboratory, resulted 2026-04-23, FINAL [FLOW-004, FLOW-008, FLOW-009, FLOW-012].
- Cytogenetics/FISH: CG-26-00871, Riverbend Cytogenetics Laboratory, reported 2026-04-29, FINAL [CYTO-004, CYTO-006, CYTO-008, CYTO-010].
- Molecular: reference MMD-26-NGS-22150, client accession S26-BM-01187, Meridian Molecular Diagnostics (CLIA 14D8888888), reported 2026-05-04, FINAL [MOLEC-004, MOLEC-005, MOLEC-009–011, MOLEC-013].

### 3. Clinical context
The patient had three weeks of fatigue, dyspnea on exertion, gingival bleeding and ecchymoses [MORPH-015]. Admission CBC showed WBC 38.4 x10^9/L, Hb 7.9 g/dL and platelets 31 x10^9/L [MORPH-016]. The peripheral smear showed 41% circulating blasts, with count method and denominator not stated [MORPH-017; FLOW-015]. No prior hematologic history, chemotherapy or radiation is reported [MORPH-018; FLOW-016; CYTO-011]. Family history and germline evaluation are not reported in any component report.

### 4. Morphology
- **Specimen and cellularity.** The aspirate was adequately cellular and spicular [MORPH-019]. The core was markedly hypercellular, about 90–95% [MORPH-040, MORPH-041], with sheets of immature mononuclear cells in an interstitial and paratrabecular distribution [MORPH-042, MORPH-043].
- **Blasts.** Aspirate blasts were 18% by 500-cell manual differential [MORPH-020]. Promonocytes were enumerated separately at 4%, with assignment described as subjective [MORPH-021, MORPH-022]. Mature monocytes were 6% [MORPH-023].
- **Cytology and stains.** No definite Auer rods were seen [MORPH-037]. MPO was positive in about 5–10% of blasts [MORPH-048]. NSE was positive in a subset, with partial fluoride inhibition [MORPH-049]. Reticulin was MF-1 and there were no ring sideroblasts [MORPH-046, MORPH-047]. Immunohistochemistry is not reported [MORPH-057].
- **Source-reported interpretation.** AML, with probable monocytic differentiation to be confirmed by flow [MORPH-050, MORPH-052]. Aspirate enumeration may be affected by hemodilution and by difficulty separating promonocytes from blasts [MORPH-055].

### 5. Flow cytometry
- **Specimen and method.** Viability was 94% by 7-AAD, using an 8-color panel with at least 100,000 events per tube and a CD45/SSC blast gate [FLOW-017, FLOW-018, FLOW-020].
- **Blast population.** Myeloid blasts were 22% of total nucleated cells [FLOW-021, FLOW-022]. They were CD34+ (subset, ~60%), CD117+, HLA-DR bright, CD13+, CD33 bright, CD38+, cytoplasmic MPO dim subset, CD64+ and CD4 dim. CD11b was partial, and CD14 was negative on blasts. CD56 was aberrant partial and CD7 aberrant subset. CD2, CD19 and cyCD3 were negative [FLOW-029–042].
- **Monocytic populations.** Maturing monocytes were 19% TNC and promonocytes/immature monocytic cells were 11% TNC, the latter "Counted with monocytic series" [FLOW-023, FLOW-024]. The source states a combined value of about 30% [FLOW-054]. Monocytic markers were bright uniform CD64, CD14 on the maturing fraction, CD11b, CD11c, CD36, HLA-DR and dim CD4, with CD34 negative [FLOW-043–052]. The relationship between the promonocyte gate and the blast gate is not stated [FLOW-062].
- **Source-reported interpretation.** "Diagnostic of acute myeloid leukemia with monocytic differentiation" [FLOW-055]. Final classification requires cytogenetic and molecular correlation [FLOW-059].

### 6. Cytogenetics and FISH
- **Karyotype.** 46,XY[20]: 20 metaphases counted and 5 karyotyped at 400–425 bphs, with no clonal abnormality at the stated resolution [CYTO-014–018]. A normal karyotype does not exclude a submicroscopic abnormality [CYTO-019].
- **FISH.** Interphase FISH scored 200 nuclei per probe. All eight targets were negative and within the laboratory's normal cutoff range: RUNX1-RUNX1T1, CBFB, PML-RARA, KMT2A, MECOM, -5/5q-, -7/7q- and TP53 [CYTO-021–030]. Numeric cutoff values are not reported [CYTO-031]. No microarray is reported [CYTO-032].
- **Source-reported interpretation.** "Cytogenetically normal category" [CYTO-035]. This negative finding applies only to the tested scope.

### 7. Molecular findings
The 54-gene hybrid-capture NGS panel had mean coverage 1,150x (minimum 250x) and sensitivity of about 5% VAF; FLT3-ITD detection was supplemented by fragment analysis [MOLEC-015–019]. Three variants were detected:

| Variant group | Variant | Measurement | Lab tier | Findings |
|---|---|---|---|---|
| 1 | NPM1 NM_002520.7:c.860_863dup p.(Trp288CysfsTer12), type A frameshift | VAF 39% | Tier I | [MOLEC-024–027] |
| 2 | FLT3 internal tandem duplication, exon 14 (~36 bp), in-frame | VAF 31%; ITD/WT allelic ratio 0.62 by fragment analysis | Tier I | [MOLEC-028, MOLEC-030–033] |
| 3 | DNMT3A NM_022552.5:c.2645G>A p.(Arg882His) | VAF 44% | Tier II | [MOLEC-034–037] |

- **Negative genes.** No reportable variant was found in 30 listed genes, including CEBPA, RUNX1, TP53 and ASXL1. This applies within the assay's limits [MOLEC-039, MOLEC-018, MOLEC-020, MOLEC-021].
- **Not available.** The full 54-gene list and coverage metrics are not included in this document [MOLEC-040].

### 8. Integrated interpretation
This section is descriptive only. No WHO criteria were applied.
- **Concordant reports.** The four component reports describe a hypercellular marrow with an abnormal myeloid blast population and an expanded monocytic compartment [MORPH-040–042; FLOW-022–024]. They also describe a normal karyotype with a negative 8-probe AML FISH panel [CYTO-017, CYTO-033], and NPM1, FLT3-ITD and DNMT3A variants [MOLEC-024–037].
- **Blast measurements differ by method and denominator.** They are preserved, not reconciled:
  - 18% by 500-cell manual aspirate differential [MORPH-020]
  - 22% of TNC by flow [FLOW-022]
  - 41% on peripheral smear, method not stated [MORPH-017]
  - "Extensive" infiltration on core, with no number [MORPH-042]
- **Promonocyte counts also differ.** 4% manually [MORPH-021] vs 11% of TNC by flow [FLOW-024]. Both sources describe promonocyte assignment as separate from blasts, and morphology calls it subjective [MORPH-022, FLOW-024].

### 9. Diagnostic assessment
**Derived WHO classification is paused: insufficient evidence, because the guideline source is unavailable.** The approved WHO 5th-edition overview could not be read (see source card), so no criterion-linked diagnosis is offered.

Source-reported component diagnoses, attributed and not verified against the guideline:
- MORPH: "ACUTE MYELOID LEUKEMIA" [MORPH-050]
- FLOW: "acute myeloid leukemia with monocytic differentiation" [FLOW-055]
- MOLEC: "acute myeloid leukemia with mutated NPM1" [MOLEC-041]

**Needed to proceed:** an uploaded original copy of Khoury et al. 2022 (DOI 10.1038/s41375-022-01613-1), so that the criteria table can be completed from its actual AML section, tables, footnotes and scope.

### 10. Prognostic and predictive observations
These are source-reported only. No formal risk assessment was done; it was not requested, and the ELN source was not consulted.
- MOLEC states that FLT3-ITD "is prognostically adverse and is a target for FLT3 inhibitor therapy" and that the allelic ratio is reported to support treatment decisions [MOLEC-043].
- MOLEC states that DNMT3A R882H is "reported here for completeness and potential prognostic relevance" [MOLEC-044].
- FLOW states that aberrant CD56/CD7 "may be useful for measurable residual disease tracking" [FLOW-058].

### 11. Limitations and unresolved issues
1. The WHO source was not accessed, so derived classification and the criteria assessment are paused (source card).
2. Blast and promonocyte measurements differ by method and denominator [MORPH-020, MORPH-021; FLOW-022, FLOW-024; MORPH-017]. The peripheral blood method is not stated.
3. The flow report does not state whether the promonocyte and blast gates overlap [FLOW-062].
4. FISH numeric cutoffs are not reported [CYTO-031]. The negative karyotype and FISH results are limited to their tested scope [CYTO-019, CYTO-034].
5. The NGS full gene list and coverage metrics are not provided [MOLEC-040]. Negative genes are subject to the assay's limit of detection and its structural/CNV limitations [MOLEC-020, MOLEC-021]. FLT3-ITD has no transcript or HGVS [MOLEC-029].
6. The WHO/ICC statements in the component reports [MORPH-056; MOLEC-041, MOLEC-042, MOLEC-044] are report text, not guideline evidence. ICC is not applied or merged.
7. Immunohistochemistry is not reported [MORPH-057]. Family history and germline information are not reported.
8. The printed page labels ("Page 1 of 1") conflict with the 2-page PDFs for MORPH and FLOW [MORPH-059; FLOW-063]. Physical pages are cited.

---

## Traceable statement (highlight)

> "Mutated NPM1 was detected: NM_002520.7:c.860_863dup p.(Trp288CysfsTer12), VAF 39%, Tier I [MOLEC-024; MOLEC-026; MOLEC-027]."

- **MOLEC-024:** "NPM1 NM_002520.7:c.860_863dup" (MOLEC p. 1, Detected Variants).
- **MOLEC-026:** "type A frameshift insertion, VAF 39%" (MOLEC p. 1, Interpretation).
- **MOLEC-027:** "NPM1 (Tier I)" (MOLEC p. 1, Result Summary).
- **Source criterion link:** none yet. This is a reported fact, not a derived statement. Any derived diagnostic use of it (for example, whether it defines a WHO type and whether a blast threshold applies) needs a criterion (C#) from the retrieved WHO article. That criterion is **pending** because the source was not read.

---

## Stage 6: Same-conversation evidence review

*I re-read the original report passages for this review. No guideline context was available to re-read. This review was done in the same conversation, is not independent QA, and does not certify the draft.*

| Severity | Affected statement / finding | Concern | Evidence needed or suggested correction |
|---|---|---|---|
| High | Sections 8–9; criteria table | The WHO source was not read, so no criterion-linked classification is possible. | Upload the original public article (PMC9252913 or the Nature open-access PDF). Then read the Introduction, the full AML section with tables and footnotes, and the secondary myeloid neoplasm context, and complete C1…Cn. |
| High | MORPH-056; MOLEC-041, MOLEC-042, MOLEC-044 | Component reports make WHO/ICC claims, such as the blast-threshold exemption and NPM1 being disease-defining. These could be mistaken for guideline evidence. | Verify each claim against the retrieved WHO text. Keep it attributed until then. Do not adopt ICC. |
| Moderate | MORPH-020 vs FLOW-022 vs MORPH-017 | Blast values are 18%, 22% and 41%, with different methods and denominators, and the peripheral blood method is unstated. | Keep all values. If the source's criteria depend on the blast percentage or specimen type, state which measurement applies and why, citing the source. |
| Moderate | MORPH-021 vs FLOW-024; FLOW-062 | Promonocytes are 4% manually vs 11% of TNC by flow. Overlap with the blast gate is not stated. Neither report counts promonocytes as blasts. | Clarify the gating relationship with the flow laboratory. Apply any source rule on promonocytes as blast equivalents only from retrieved text. |
| Moderate | MOLEC-039, MOLEC-040 | The negative-gene evidence covers only the listed genes. The full 54-gene list and coverage are not in the document. | Obtain the laboratory appendix if a criterion depends on genes not listed. |
| Low | CYTO-030, CYTO-031 | "Within normal cutoff" is stated, but the cutoff values are not given. | Request the laboratory cutoffs if needed for interpretation. |
| Low | Section 3; MORPH-018 | Absence of prior therapy is reported. Family history and germline status are not reported. | Obtain these only if the retrieved source makes them relevant. |
| Low | MOLEC-029 | FLT3-ITD has no transcript or HGVS expression. | Leave as is; do not reconstruct it. |
| Low | MORPH-059; FLOW-063 | The printed "Page 1 of 1" conflicts with the 2-page PDFs. | Physical pages are cited. No action needed beyond noting it. |

This review is not proof of correctness. The material unresolved issues above remain open.

**Next step:** Upload the original WHO article. I will then complete Stage 4, the criteria assessment, and update sections 8–9 with finding- and criterion-linked statements, keeping the article labeled as an uploaded source. I have not done a formal ELN risk assessment because you did not request one.
