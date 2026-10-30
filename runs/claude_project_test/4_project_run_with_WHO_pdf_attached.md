# Synthetic teaching draft — human review required

*Fictional teaching case. Not a clinical report and not clinically validated. All stages below ran as steps in one Project conversation. No native Skill was installed, no separate agents were used, and there was no independent QA.*

## Stage status

| # | Stage | Status |
|---|---|---|
| 0 | Instruction access | All 8 Skills modules were read in full as the complete **Markdown (.md)** set (Skills_1 … Skills_8). No .docx versions were uploaded, so there are no duplicate module versions to resolve. |
| 1 | Report inventory and identity check | **Complete.** 4 of 4 reports were read in full. Patient identity is consistent across all four (name, MRN, DOB, sex, collection date). |
| 2 | MORPH, FLOW, CYTO, MOLEC extraction passes | **Complete.** Four tables, done as four separate passes in this conversation. |
| 3 | WHO source access | **No online retrieval in this conversation.** You reported that the article could not be opened online here and attached the original public article PDF. That **uploaded original** (`41375_2022_Article_1613.pdf`) was read directly. Title and DOI were checked against page 1. |
| 4 | Criteria assessment from the source | **Complete.** C1–C12, drawn from the actual article text and tables. |
| 5 | Integrated teaching draft | **Complete.** Eleven sections. |
| 6 | Evidence review (same conversation) | **Complete.** Findings are listed below. This was not an independent review. |

## Opening summary

- **Classification status: supported.** The WHO 5th-edition type **acute myeloid leukaemia with NPM1 mutation** is supported by this case's evidence.
- **Source and framework consulted:** Khoury et al., *The 5th edition of the WHO Classification of Haematolymphoid Tumours: Myeloid and Histiocytic/Dendritic Neoplasms*, Leukemia 2022;36:1703–1719, DOI 10.1038/s41375-022-01613-1. This is the uploaded original PDF.
  - It is a public 2022 author overview. It is not the full or latest WHO Blue Book.
  - ICC and ELN were **not** consulted.
- **Key findings:**
  - Hypercellular marrow (about 90–95%) replaced by sheets of immature cells [MORPH-037; MORPH-038].
  - The blast measurements disagree, and are kept separate here:
    - 18% on the aspirate manual differential [MORPH-017]
    - 22% of TNC by flow [FLOW-019]
    - 41% peripheral blood blasts, stated in the clinical history [MORPH-014]
  - Myeloid blasts with an expanded monocytic compartment [FLOW-050; FLOW-051].
  - 46,XY[20] karyotype with a negative 8-probe AML FISH panel [CYTO-018; CYTO-032].
  - Three variants on the molecular panel:
    - NPM1 c.860_863dup, VAF 39%, Tier I [MOLEC-017; MOLEC-019]
    - FLT3-ITD, VAF 31%, ITD/WT ratio 0.62 [MOLEC-021; MOLEC-023; MOLEC-024]
    - DNMT3A R882H, VAF 44% [MOLEC-028; MOLEC-030]
- **Material unresolved issues:**
  1. Some Table 7 defining rearrangements were not specifically targeted: NUP98 (which the source says may be cryptic on karyotyping), DEK::NUP214, RBM15::MRTFA, and BCR::ABL1 [C7].
  2. Germline predisposition was not evaluated [C11].
  3. Blast and promonocyte values differ between methods and denominators. They are preserved, not reconciled.
  4. The source's requirement for "judicious clinicopathologic correlation" remains a pathologist sign-off item.
  5. Physical PDF pagination differs from the printed "Page 1 of 1" labels on MORPH and FLOW.

**Traceable statement (highlight):** Section 9 states "Acute myeloid leukaemia with NPM1 mutation". It traces as follows:
- **Case evidence:** MOLEC-017, quoting "NM_002520.7:c.860_863dup p.(Trp288CysfsTer12)" (MOLEC p.1, Detected Variants), together with MOLEC-019 (VAF 39%).
- **Source criterion:** C1. WHO Table 7 (journal p.1709) lists "Acute myeloid leukaemia with NPM1 mutation" under *AML with defining genetic abnormalities*.
- **Blast count:** C2. The source says this type "can be diagnosed irrespective of the blast count" (p.1709).

---

## Source card — WHO5E_MYEOID_2022

| Item | Record |
|---|---|
| Source ID, title, DOI | WHO5E_MYEOID_2022. "The 5th edition of the World Health Organization Classification of Haematolymphoid Tumours: Myeloid and Histiocytic/Dendritic Neoplasms." Khoury JD, Solary E, et al. DOI 10.1038/s41375-022-01613-1. Title and DOI were checked on PDF p.1 and match Skills_7. |
| Framework and edition/year | WHO Classification of Haematolymphoid Tumours, 5th edition. Public author overview, Leukemia 2022;36:1703–1719 (published online 22 June 2022). |
| Access method | **Uploaded original**, attached by the user to this chat. **Not** retrieved online in this conversation. |
| Actual URL or uploaded filename | `41375_2022_Article_1613.pdf` (17 PDF pages). Publisher URL per Skills_7: https://www.nature.com/articles/s41375-022-01613-1 (not opened here). |
| Access date | 2026-10-30 (date of this conversation, UTC) |
| Sections/tables read | PDF pp.1–13 (journal pp.1703–1715), read as page images: Introduction and Clonal haematopoiesis (1703–1704); MDS section, including the MDS/AML 20% boundary discussion (1706–1707); full **Acute myeloid leukaemia** section (1708–1710), including **Table 7**, **Table 8** and the AML-MR text, AML with other defined genetic alterations, AML defined by differentiation, myeloid sarcoma, and Summary Box; **Table 9 with all footnotes** (1711); **Secondary myeloid neoplasms**, covering post cytotoxic therapy and germline predisposition, with Table 10 (1710–1712); Acute leukaemias of mixed or ambiguous lineage text, **Table 12** and **Table 13** with footnotes (1712–1714); Disclaimer (1715). |
| Not read | PDF pp.14–17, which appear to be the continued reference list and affiliations. They were not opened and were not needed for any criterion. |
| Limitations | This is an overview by the authors. It does not give complete Blue Book essential/desirable criteria for each type. It gives no qualifying NPM1 variant definition, no minimum blast count for AML with NPM1 mutation, and no explicit hierarchy for two co-occurring defining abnormalities. The Disclaimer (p.1715) says the article represents the authors' views and previews IARC/WHO content. Later WHO updates were not reviewed. |

Optional ELN 2022 risk source: **not used**, because no formal risk assessment was requested.

---

## 1. Report inventory and identity check

| Source ID | Filename | Patient / MRN / DOB / sex | Specimen | Accession | Laboratory | Collected / Reported | Status | Readable pages |
|---|---|---|---|---|---|---|---|---|
| MORPH | Pathology_Report_1_bone_marrow_morphology.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 / Male | Bone marrow aspirate and core, left posterior iliac crest | S26-BM-01187 | Riverbend Regional Medical Center, Dept. of Pathology & Laboratory Medicine (CLIA 14D9999999) | 2026-04-22 / 2026-04-24 | FINAL (morphology component) | Physical pp.1–2; printed label "Page 1 of 1" |
| FLOW | Pathology_Report_2_flow_cytometry.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 / Male | Bone marrow aspirate | FC-26-003942 | Riverbend RMC Flow Cytometry Laboratory (CLIA 14D9999999) | 2026-04-22 / resulted 2026-04-23 | FINAL | Physical pp.1–2; printed label "Page 1 of 1" |
| CYTO | Pathology_Report_3_cytogenetics_fish.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 / Male | Bone marrow aspirate | CG-26-00871 | Riverbend RMC Cytogenetics Laboratory (CLIA 14D9999999) | 2026-04-22 / 2026-04-29 | FINAL | p.1 |
| MOLEC | Pathology_Report_4_molecular_ngs.pdf | DOE, JONATHAN R. / MRN-4471902 / 1967-09-14 / Male | Bone marrow aspirate, EDTA | Reference MMD-26-NGS-22150; client S26-BM-01187 | Meridian Molecular Diagnostics (CLIA 14D8888888) | 2026-04-22 / 2026-05-04 | FINAL | p.1 |

**Identity check:** no conflict was found, so integration proceeds.
- Different accessions are expected for different component studies.
- MOLEC's client accession S26-BM-01187 matches the MORPH accession.
- CYTO cross-references the MOLEC accession MMD-26-NGS-22150.

---

## 2. Extraction tables

Page notes:
- "p." means the physical PDF page.
- MORPH and FLOW each print "Page 1 of 1" but render as two physical pages. Physical pages are cited, and the discrepancy is recorded in MORPH-057 and FLOW-059.

### MORPH — Pathology_Report_1_bone_marrow_morphology.pdf

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| MORPH-001 | Patient identity — name | Reported: DOE, JONATHAN R. | Not applicable | "Patient: DOE, JONATHAN R." — p.1, header table |
| MORPH-002 | Patient identity — MRN | Reported: MRN-4471902 | Not applicable | "MRN: MRN-4471902" — p.1, header table |
| MORPH-003 | Patient identity — DOB/age/sex | Reported: 1967-09-14 / 58 y / Male | Not applicable | "DOB / Age / Sex: 1967-09-14 / 58 y / Male" — p.1, header table |
| MORPH-004 | Study identity — accession | Reported: S26-BM-01187 | Not applicable | "Accession: S26-BM-01187" — p.1, header table |
| MORPH-005 | Study identity — collection date | Reported: 2026-04-22 | Not applicable | "Collected: 2026-04-22" — p.1, header table |
| MORPH-006 | Study identity — report date | Reported: 2026-04-24 | Not applicable | "Reported: 2026-04-24" — p.1, header table |
| MORPH-007 | Performing laboratory | Reported: Riverbend Regional Medical Center | CLIA 14D9999999 (letterhead) | "1200 Halsted Avenue, Lakeshore, IL 60000 • CLIA 14D9999999" — p.1, letterhead |
| MORPH-008 | Patient location | Reported: Inpatient — 6 West Hematology | Not applicable | "Location: Inpatient — 6 West Hematology" — p.1, header table |
| MORPH-009 | Specimen — site/type | Reported: bone marrow aspirate and core, left posterior iliac crest | Not applicable | "Bone marrow, left posterior iliac crest (aspirate and core biopsy)." — p.1, Specimen |
| MORPH-010 | Specimen — preparations | Reported: Wright-Giemsa smears, clot section, decalcified core (H&E) | Not applicable | "Aspirate smears (Wright-Giemsa), clot section, and decalcified core biopsy (H&E) received." — p.1, Specimen |
| MORPH-011 | Report context — ancillary studies | Reported: flow, cytogenetics and molecular studies were submitted under separate accession | Not applicable | "Aspirate also submitted for flow cytometry, cytogenetics, and molecular studies under separate accession." — p.1, Specimen |
| MORPH-012 | Clinical history — presentation | Reported | Not applicable | "58-year-old man with three weeks of progressive fatigue, dyspnea on exertion, gingival bleeding, and scattered lower-extremity ecchymoses." — p.1, Clinical History |
| MORPH-013 | Clinical history — CBC | Reported: WBC 38.4 x10^9/L; Hb 7.9 g/dL; platelets 31 x10^9/L | Units as stated. CBC report not provided. | "CBC on admission: WBC 38.4 x10^9/L, hemoglobin 7.9 g/dL, platelets 31 x10^9/L." — p.1, Clinical History |
| MORPH-014 | Clinical history — peripheral blood blasts | Reported: 41% circulating blasts | Peripheral smear. Count method and denominator not stated. | "Peripheral smear with 41% circulating blasts, some with folded nuclei and abundant cytoplasm." — p.1, Clinical History |
| MORPH-015 | Clinical history — prior disease/therapy | Negative (as stated in the history): no prior hematologic history, chemotherapy or radiation | Clinical history statement | "No prior hematologic history, no prior chemotherapy or radiation." — p.1, Clinical History |
| MORPH-016 | Specimen adequacy — aspirate | Reported: adequately cellular and spicular | Not applicable | "Smears are adequately cellular and spicular." — p.1, Microscopic Description, Aspirate |
| MORPH-017 | Aspirate differential — Blasts | Reported: 18% | Manual differential; 500-cell count | "Blasts 18" — p.1, Aspirate Differential (500-cell count) table |
| MORPH-018 | Aspirate differential — Promyelocytes | Reported: 3% | 500-cell count | "Promyelocytes 3" — p.1, Aspirate Differential table |
| MORPH-019 | Aspirate differential — Myelocytes/metamyelocytes | Reported: 8% | 500-cell count | "Myelocytes / metamyelocytes 8" — p.1, Aspirate Differential table |
| MORPH-020 | Aspirate differential — Neutrophils/bands | Reported: 21% | 500-cell count | "Neutrophils / bands 21" — p.1, Aspirate Differential table |
| MORPH-021 | Aspirate differential — Eosinophils | Reported: 2% | 500-cell count | "Eosinophils 2" — p.1, Aspirate Differential table |
| MORPH-022 | Aspirate differential — Basophils | Reported: 1% | 500-cell count | "Basophils 1" — p.1, Aspirate Differential table |
| MORPH-023 | Aspirate differential — Lymphocytes | Reported: 9% | 500-cell count | "Lymphocytes 9" — p.1, Aspirate Differential table |
| MORPH-024 | Aspirate differential — Plasma cells | Reported: 1% | 500-cell count | "Plasma cells 1" — p.1, Aspirate Differential table |
| MORPH-025 | Aspirate differential — Monocytes (mature) | Reported: 6% | 500-cell count | "Monocytes (mature) 6" — p.1, Aspirate Differential table |
| MORPH-026 | Aspirate differential — Promonocytes | Reported: 4% (enumerated separately from blasts) | 500-cell count | "Promonocytes* 4" — p.1, Aspirate Differential table |
| MORPH-027 | Aspirate differential — Promonocytes, qualifier | Reported: assignment is subjective | Not applicable | "Promonocytes were enumerated separately; their assignment is morphologically subjective and is discussed below." — p.1, table footnote |
| MORPH-028 | Aspirate differential — Erythroid precursors | Reported: 14% | 500-cell count | "Erythroid precursors 14" — p.1, Aspirate Differential table |
| MORPH-029 | Aspirate differential — M:E ratio | Reported: ~4.4:1 | Ratio | "M:E ratio ~4.4:1" — p.1, Aspirate Differential table |
| MORPH-030 | Blast morphology | Reported: medium-to-large blasts, high N:C ratio, fine chromatin, 1–3 nucleoli | Wright-Giemsa smear | "a population of medium-to-large blasts with high nuclear-to-cytoplasmic ratio, fine chromatin, and one to three nucleoli" — p.1, Microscopic Description, Aspirate |
| MORPH-031 | Blast morphology — subset | Reported: folded/indented nuclei, grayish cytoplasm, occasional fine azurophilic granulation | Wright-Giemsa smear | "A subset of blasts shows slightly folded or indented nuclei with moderate amounts of grayish cytoplasm and occasional fine azurophilic granulation" — p.1, Aspirate |
| MORPH-032 | Blast morphology — vacuoles | Reported: rare cells with delicate cytoplasmic vacuoles | Wright-Giemsa smear | "rare cells contain delicate cytoplasmic vacuoles" — p.1, Aspirate |
| MORPH-033 | Morphology and lineage — monocytoid cells | Reported, with a hedge: promonocytes are difficult to distinguish | Morphology alone | "Occasional cells with monocytoid features are noted, but unequivocal promonocytes are difficult to distinguish from immature myeloid forms on morphology alone." — p.1, Aspirate |
| MORPH-034 | Auer rods | Negative | Review of multiple smears | "No definite Auer rods are identified after review of multiple smears." — p.1, Aspirate |
| MORPH-035 | Erythropoiesis | Reported: left-shifted, mild megaloblastoid change | Aspirate | "Erythropoiesis is left-shifted with mild megaloblastoid change." — p.1, Aspirate |
| MORPH-036 | Megakaryocytes — aspirate | Reported: reduced | Aspirate | "Megakaryocytes are reduced." — p.1, Aspirate |
| MORPH-037 | Core cellularity | Reported: approximately 90–95% | Core biopsy (H&E) | "The core is markedly hypercellular (cellularity approximately 90-95%)" — p.1, Core biopsy and clot |
| MORPH-038 | Core architecture — infiltrate | Reported: extensive replacement by immature mononuclear cells in sheets | Core biopsy | "extensive replacement by immature mononuclear cells arranged in sheets" — p.1, Core biopsy and clot |
| MORPH-039 | Core architecture — distribution | Reported: interstitial and paratrabecular | Core biopsy | "Interstitial and paratrabecular distribution is noted." — p.1, Core biopsy and clot |
| MORPH-040 | Residual hematopoiesis | Reported: present but markedly decreased | Core/clot | "Residual maturing granulopoiesis and erythropoiesis are present but markedly decreased." — p.1, Core biopsy and clot |
| MORPH-041 | Megakaryocytes — core | Reported: markedly reduced | Core/clot | "Megakaryocytes are markedly reduced." — p.1, Core biopsy and clot |
| MORPH-042 | Fibrosis | Reported: no significant fibrosis (MF-1) | Reticulin stain | "Reticulin stain shows no significant fibrosis (MF-1)." — p.1, Core biopsy and clot |
| MORPH-043 | Iron / ring sideroblasts | Reported: storage iron present; Negative for ring sideroblasts | Iron stain, aspirate | "Iron stain (aspirate): storage iron present; no ring sideroblasts." — p.1, Core biopsy and clot |
| MORPH-044 | Cytochemistry — MPO | Reported: positive in about 5–10% of blasts | MPO cytochemistry; denominator is blasts | "Myeloperoxidase (MPO): positive in a minor subset of blasts (approximately 5-10%)." — p.1, Cytochemistry |
| MORPH-045 | Cytochemistry — NSE | Reported: positive subset with partial fluoride inhibition | Alpha-naphthyl butyrate NSE. Denominator not stated. | "positive in a subset of cells with partial fluoride inhibition, supporting a monocytic component" — p.1, Cytochemistry |
| MORPH-046 | Cytochemistry — interpretation | **Source-reported interpretation**: probable monocytic differentiation | Not applicable | "consistent with a myeloid process with probable monocytic differentiation; correlation with flow cytometry is recommended" — p.1, Cytochemistry |
| MORPH-047 | Immunohistochemistry | Not reported | Not applicable | No supporting statement located. |
| MORPH-048 | Diagnosis | **Source-reported interpretation**: AML | Not applicable | "HYPERCELLULAR MARROW WITH ACUTE MYELOID LEUKEMIA (see comment)." — p.1, Diagnosis |
| MORPH-049 | Diagnosis — blast statement | **Source-reported interpretation**: aspirate blasts 18%; extensive blast-equivalent infiltration in core | 500-cell manual differential | "Aspirate blast count 18% by 500-cell manual differential; core biopsy with extensive blast-equivalent infiltration." — p.1, Diagnosis |
| MORPH-050 | Diagnosis — lineage | **Source-reported interpretation**: probable monocytic differentiation, pending flow | Morphology and cytochemistry | "Probable monocytic differentiation by morphology and cytochemistry; to be confirmed by flow cytometry." — p.2, Diagnosis (continued) |
| MORPH-051 | Comment — blast discrepancy | **Source-reported interpretation** | Not applicable | "The manual aspirate blast percentage (18%) is below the historical 20% threshold; however, the core biopsy demonstrates extensive infiltration by immature cells well in excess of that proportion, and the peripheral blood blast count is 41%." — p.2, Comment |
| MORPH-052 | Comment — limitation | Reported: possible hemodilution; promonocyte/blast separation difficulty | Not applicable | "Aspirate enumeration is likely affected by hemodilution and by the difficulty of separating promonocytes from myeloid blasts on smears." — p.2, Comment |
| MORPH-053 | Comment — classification statement | **Source-reported interpretation** (refers to WHO and ICC) | Not applicable | "Under current WHO and ICC classifications, a diagnosis of acute myeloid leukemia does not require a 20% blast count when a defining genetic abnormality is present" — p.2, Comment |
| MORPH-054 | Comment — pending studies | Pending at the time of this report | Not applicable | "classification will therefore depend on integration with flow cytometry, cytogenetic, and molecular results, which are pending at the time of this report" — p.2, Comment |
| MORPH-055 | Report status | Reported: FINAL (morphology component) | Not applicable | "Report status: FINAL (morphology component)." — p.2, footer |
| MORPH-056 | Signing pathologist | Reported: Marcus T. Whitfield, MD | Not applicable | "Electronically signed: Marcus T. Whitfield, MD — Hematopathology." — p.2, footer |
| MORPH-057 | Pagination | Printed label "Page 1 of 1" appears on physical p.2 of a 2-page PDF | Not applicable | "Page 1 of 1 • Accession S26-BM-01187 • MRN-4471902" — p.2, footer |
| MORPH-058 | Core biopsy blast percentage (numeric) | Not reported | Not applicable | No supporting statement located. |

### FLOW — Pathology_Report_2_flow_cytometry.pdf

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| FLOW-001 | Patient identity — name | Reported: DOE, JONATHAN R. | Not applicable | "DOE, JONATHAN R." — p.1, Patient box |
| FLOW-002 | Patient identity — MRN | Reported: MRN-4471902 | Not applicable | "MRN MRN-4471902" — p.1, Patient box |
| FLOW-003 | Patient identity — DOB/age/sex | Reported: 1967-09-14, 58 y, Male | Not applicable | "DOB 1967-09-14 58 y / Male" — p.1, Patient box |
| FLOW-004 | Study identity — accession | Reported: FC-26-003942 | Not applicable | "FC-26-003942" — p.1, Specimen box |
| FLOW-005 | Specimen type | Reported: bone marrow aspirate | Not applicable | "Bone marrow aspirate" — p.1, Specimen box |
| FLOW-006 | Collection date | Reported: 2026-04-22 | Not applicable | "Collected 2026-04-22" — p.1, Specimen box |
| FLOW-007 | Received | Reported: 2026-04-22 17:40 | Not applicable | "Received 2026-04-22 17:40" — p.1, Specimen box |
| FLOW-008 | Result date | Reported: 2026-04-23 | Not applicable | "Resulted 2026-04-23" — p.1, Reporting box |
| FLOW-009 | Ordering provider | Reported: A. Patel, MD | Not applicable | "Ordering: A. Patel, MD" — p.1, Reporting box |
| FLOW-010 | Report status | Reported: FINAL | Not applicable | "Status: FINAL" — p.1, Reporting box |
| FLOW-011 | Performing laboratory | Reported: Riverbend RMC Flow Cytometry Laboratory, CLIA 14D9999999 | Not applicable | "FLOW CYTOMETRY LABORATORY" — p.1, letterhead |
| FLOW-012 | Clinical history — peripheral blood blasts | Reported: 41% | Peripheral smear. Method/denominator not stated. | "Peripheral smear with 41% circulating blasts" — p.1, Clinical History / Indication |
| FLOW-013 | Clinical history — prior disease/therapy | Negative (as stated in the history) | Clinical history statement | "No prior hematologic history, no prior chemotherapy or radiation." — p.1, Clinical History / Indication |
| FLOW-014 | Specimen adequacy — viability | Reported: 94% | 7-AAD | "viability 94% by 7-AAD" — p.1, Specimen Adequacy & Method |
| FLOW-015 | Method — panel | Reported: 8-color, 3-laser, ≥100,000 events per tube | Events per tube | "Eight-color panel acquired on a 3-laser cytometer (≥100,000 events per tube)." — p.1, Specimen Adequacy & Method |
| FLOW-016 | Method — technique | Reported: lysis/no-wash | Not applicable | "Lysis/no-wash technique." — p.1, Specimen Adequacy & Method |
| FLOW-017 | Gating strategy | Reported: CD45 vs SSC; blast gate CD45-dim/intermediate, low SSC | Sequential gating | "Analysis by sequential gating (CD45 vs side scatter) with blast gate defined by CD45-dim/intermediate, low side scatter events." — p.1, Specimen Adequacy & Method |
| FLOW-018 | Population denominator | Reported: % of total nucleated cells | % TNC | "POPULATION SUMMARY (% of total nucleated cells)" — p.1, section heading |
| FLOW-019 | Myeloid blasts — measurement | Reported: 22% | % TNC; CD45-dim, low SSC, CD34+/CD117+ gate | "Myeloid blasts (CD45-dim, low SSC, CD34+/CD117+) 22% Discrete abnormal population" — p.1, Population Summary table |
| FLOW-020 | Maturing monocytes — measurement | Reported: 19%; expanded, left-shifted | % TNC; CD14+/CD64+/CD11b+ | "Maturing monocytes (CD14+/CD64+/CD11b+) 19% Expanded; left-shifted" — p.1, Population Summary table |
| FLOW-021 | Promonocytes / immature monocytic — measurement | Reported: 11%; counted with the monocytic series | % TNC; CD64+, CD14-dim/var, HLA-DR+ | "Promonocytes / immature monocytic (CD64+, CD14-dim/var, HLA-DR+) 11% Counted with monocytic series" — p.1, Population Summary table |
| FLOW-022 | Maturing granulocytes — measurement | Reported: 28%; decreased, left-shifted | % TNC | "Maturing granulocytes 28% Decreased, left-shifted" — p.1, Population Summary table |
| FLOW-023 | Erythroid precursors — measurement | Reported: 9%; decreased | % TNC; CD71+/CD235a+ | "Erythroid precursors (CD71+/CD235a+) 9% Decreased" — p.1, Population Summary table |
| FLOW-024 | Mature lymphocytes — measurement | Reported: 8%; polytypic, no aberrancy | % TNC | "Mature lymphocytes (T/B/NK) 8% Polytypic, no aberrancy" — p.1, Population Summary table |
| FLOW-025 | Other/unclassified — measurement | Reported: 3% | % TNC | "Other / unclassified 3% --" — p.1, Population Summary table |
| FLOW-026 | Blast gate — CD34 | Reported: positive (subset, ~60%) | Flow; denominator is the blast gate (implied by the table heading) | "CD34 Positive (subset, ~60%)" — p.1, Blast Gate Immunophenotype |
| FLOW-027 | Blast gate — CD117 | Reported: positive | Flow | "CD117 Positive" — p.1, Blast Gate Immunophenotype |
| FLOW-028 | Blast gate — HLA-DR | Reported: positive (bright) | Flow | "HLA-DR Positive (bright)" — p.1, Blast Gate Immunophenotype |
| FLOW-029 | Blast gate — CD13 | Reported: positive | Flow | "CD13 Positive" — p.1, Blast Gate Immunophenotype |
| FLOW-030 | Blast gate — CD33 | Reported: positive (bright) | Flow | "CD33 Positive (bright)" — p.1, Blast Gate Immunophenotype |
| FLOW-031 | Blast gate — CD38 | Reported: positive | Flow | "CD38 Positive" — p.1, Blast Gate Immunophenotype |
| FLOW-032 | Blast gate — MPO (cytoplasmic) | Reported: positive, dim subset | Flow. Percentage and intensity relative to neutrophils not stated. | "MPO (cyto) Positive, dim subset" — p.1, Blast Gate Immunophenotype |
| FLOW-033 | Blast gate — CD64 | Reported: positive | Flow | "CD64 Positive" — p.1, Blast Gate Immunophenotype |
| FLOW-034 | Blast gate — CD4 | Reported: positive (dim) | Flow | "CD4 Positive (dim)" — p.1, Blast Gate Immunophenotype |
| FLOW-035 | Blast gate — CD11b | Reported: partial/variable | Flow | "CD11b Partial / variable" — p.1, Blast Gate Immunophenotype |
| FLOW-036 | Blast gate — CD14 | Negative on blasts | Flow | "CD14 Negative on blasts" — p.1, Blast Gate Immunophenotype |
| FLOW-037 | Blast gate — CD56 | Reported: positive (partial, aberrant) | Flow | "CD56 Positive (partial, aberrant)" — p.1, Blast Gate Immunophenotype |
| FLOW-038 | Blast gate — CD7 | Reported: positive (aberrant, subset) | Flow | "CD7 Positive (aberrant, subset)" — p.1, Blast Gate Immunophenotype |
| FLOW-039 | Blast gate — CD2 / CD19 / cyCD3 | Negative (grouped result as reported) | Flow | "CD2 / CD19 / cyCD3 Negative" — p.1, Blast Gate Immunophenotype |
| FLOW-040 | Monocytic population — CD14 | Reported: positive (maturing fraction) | Flow | "CD14 Positive (maturing fraction)" — p.1, Monocytic Population Immunophenotype |
| FLOW-041 | Monocytic population — CD64 | Reported: positive (bright, uniform) | Flow | "CD64 Positive (bright, uniform)" — p.1, Monocytic Population Immunophenotype |
| FLOW-042 | Monocytic population — CD11b | Reported: positive | Flow | "CD11b Positive" — p.1, Monocytic Population Immunophenotype |
| FLOW-043 | Monocytic population — CD11c | Reported: positive | Flow | "CD11c Positive" — p.1, Monocytic Population Immunophenotype |
| FLOW-044 | Monocytic population — CD36 | Reported: positive | Flow | "CD36 Positive" — p.1, Monocytic Population Immunophenotype |
| FLOW-045 | Monocytic population — HLA-DR | Reported: positive | Flow | "HLA-DR Positive" — p.1, Monocytic Population Immunophenotype |
| FLOW-046 | Monocytic population — CD4 | Reported: positive (dim) | Flow | "CD4 Positive (dim)" — p.1, Monocytic Population Immunophenotype |
| FLOW-047 | Monocytic population — CD13 / CD33 | Reported: positive | Flow | "CD13 / CD33 Positive" — p.1, Monocytic Population Immunophenotype |
| FLOW-048 | Monocytic population — CD34 | Negative | Flow | "CD34 Negative" — p.1, Monocytic Population Immunophenotype |
| FLOW-049 | Monocytic population — CD56 | Reported: partial (subset) | Flow | "CD56 Partial (subset)" — p.1, Monocytic Population Immunophenotype |
| FLOW-050 | Interpretation — blast population | **Source-reported interpretation**: abnormal myeloid blasts about 22% of TNC | % TNC | "Flow cytometry demonstrates an abnormal myeloid blast population comprising approximately 22% of total nucleated cells" — p.1, Interpretation |
| FLOW-051 | Interpretation — monocytic compartment | **Source-reported interpretation**: maturing monocytes plus promonocytes together about 30% of TNC (the source's own combined figure) | % TNC | "maturing monocytes plus promonocytes together approximately 30% of total nucleated cells" — p.1, Interpretation |
| FLOW-052 | Interpretation — diagnosis | **Source-reported interpretation**: AML with monocytic differentiation | Not applicable | "The combined findings are diagnostic of acute myeloid leukemia with monocytic differentiation." — p.2, Interpretation |
| FLOW-053 | Interpretation — lineage | **Source-reported interpretation** | Not applicable | "The immunophenotype establishes the monocytic lineage that was only favored on morphology." — p.2, Interpretation |
| FLOW-054 | Interpretation — blast discrepancy | **Source-reported interpretation** | Not applicable | "flow gating and manual counts are expected to differ and either value supports the diagnosis in this context" — p.2, Interpretation |
| FLOW-055 | Interpretation — MRD | **Source-reported interpretation** | Not applicable | "Aberrant CD56/CD7 expression is noted and may be useful for measurable residual disease tracking." — p.2, Interpretation |
| FLOW-056 | Interpretation — limitation | Reported: final classification requires cytogenetic/molecular correlation | Not applicable | "Correlation with cytogenetic and molecular studies is required for final classification and is recommended." — p.2, Interpretation |
| FLOW-057 | Verifying director | Reported: Priya N. Raghavan, MD, 2026-04-23 14:08 | Not applicable | "Electronically verified by Priya N. Raghavan, MD, Director of Flow Cytometry, 2026-04-23 14:08." — p.2, footer |
| FLOW-058 | Method status | Reported: laboratory-developed test | Not applicable | "Method: laboratory-developed test, performance characteristics established by Riverbend Regional Medical Center." — p.2, footer |
| FLOW-059 | Pagination | Printed label "Page 1 of 1" appears on physical p.2 of a 2-page PDF | Not applicable | "Accession FC-26-003942 \| MRN-4471902 \| Page 1 of 1" — p.2, footer |
| FLOW-060 | Absolute counts / events in blast gate | Not reported | Not stated | No supporting statement located. |

### CYTO — Pathology_Report_3_cytogenetics_fish.pdf

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| CYTO-001 | Patient identity — name | Reported: DOE, JONATHAN R. | Not applicable | "Patient: DOE, JONATHAN R." — p.1, header table |
| CYTO-002 | Patient identity — MRN | Reported: MRN-4471902 | Not applicable | "MRN: MRN-4471902" — p.1, header table |
| CYTO-003 | Study identity — accession | Reported: CG-26-00871 | Not applicable | "Accession: CG-26-00871" — p.1, header table |
| CYTO-004 | Patient identity — DOB/age/sex | Reported: 1967-09-14, 58 y, Male | Not applicable | "DOB: 1967-09-14 (58 y / Male)" — p.1, header table |
| CYTO-005 | Collection date | Reported: 2026-04-22 | Not applicable | "Collected: 2026-04-22" — p.1, header table |
| CYTO-006 | Report date | Reported: 2026-04-29 | Not applicable | "Reported: 2026-04-29" — p.1, header table |
| CYTO-007 | Specimen | Reported: bone marrow aspirate | Not applicable | "Specimen: Bone marrow aspirate" — p.1, header table |
| CYTO-008 | Report status | Reported: FINAL | Not applicable | "Status: FINAL" — p.1, header table |
| CYTO-009 | Performing laboratory | Reported: Riverbend RMC Cytogenetics Laboratory, CLIA 14D9999999 | Not applicable | "CYTOGENETICS LABORATORY — Department of Pathology & Laboratory Medicine" — p.1, letterhead |
| CYTO-010 | Ordering provider | Reported: A. Patel, MD | Not applicable | "Ordering: A. Patel, MD" — p.1, header table |
| CYTO-011 | Clinical indication — prior disease/therapy | Negative (as stated in the history) | Clinical history statement | "No prior hematologic history, no prior chemotherapy or radiation." — p.1, Clinical Indication |
| CYTO-012 | Clinical indication — peripheral blood blasts | Reported: 41% | Peripheral smear. Method not stated. | "Peripheral smear with 41% circulating blasts" — p.1, Clinical Indication |
| CYTO-013 | Karyotype — tissue cultured | Reported: bone marrow, unstimulated | Not applicable | "Bone marrow, unstimulated" — p.1, Conventional Chromosome Analysis table |
| CYTO-014 | Karyotype — cultures | Reported: 24-hour and 48-hour, synchronized | Not applicable | "24-hour and 48-hour, synchronized" — p.1, Conventional Chromosome Analysis table |
| CYTO-015 | Karyotype — cells counted | Reported: 20 | Metaphases | "Cells counted 20" — p.1, Conventional Chromosome Analysis table |
| CYTO-016 | Karyotype — cells karyotyped | Reported: 5 | Metaphases | "Cells karyotyped 5" — p.1, Conventional Chromosome Analysis table |
| CYTO-017 | Karyotype — band resolution | Reported: 400–425 bphs | Bands per haploid set | "400-425 bphs" — p.1, Conventional Chromosome Analysis table |
| CYTO-018 | Karyotype — ISCN | Reported: 46,XY[20] | G-banding; 20 metaphases | "46,XY[20]" — p.1, ISCN Result |
| CYTO-019 | Karyotype — abnormality | Negative within the stated band resolution | G-banding | "No clonal numerical or structural abnormality was identified at the stated band resolution." — p.1, ISCN Result narrative |
| CYTO-020 | Karyotype — limitation | Reported: does not exclude submicroscopic abnormality | Not applicable | "A normal karyotype does not exclude a submicroscopic abnormality; correlation with FISH and molecular studies is advised." — p.1, ISCN Result narrative |
| CYTO-021 | FISH — method | Reported: interphase FISH, cultured marrow, AML panel; 200 nuclei per probe | 200 interphase nuclei per probe | "Interphase FISH performed on cultured bone marrow using the acute myeloid leukemia panel. 200 interphase nuclei scored per probe." — p.1, FISH |
| CYTO-022 | FISH — RUNX1-RUNX1T1, t(8;21) | Negative; 0.5% nuclei | % of 200 nuclei | "RUNX1-RUNX1T1 t(8;21)(q22;q22) NEGATIVE 0.5%" — p.1, FISH table |
| CYTO-023 | FISH — CBFB, inv(16)/t(16;16) | Negative; 1.0% nuclei | % of 200 nuclei | "CBFB inv(16)/t(16;16)(p13;q22) NEGATIVE 1.0%" — p.1, FISH table |
| CYTO-024 | FISH — PML-RARA, t(15;17) | Negative; 0.5% nuclei | % of 200 nuclei | "PML-RARA t(15;17)(q24;q21) NEGATIVE 0.5%" — p.1, FISH table |
| CYTO-025 | FISH — KMT2A (MLL), 11q23.3 rearrangement | Negative; 1.5% nuclei | % of 200 nuclei | "KMT2A (MLL) 11q23.3 rearrangement NEGATIVE 1.5%" — p.1, FISH table |
| CYTO-026 | FISH — MECOM (EVI1), 3q26.2 rearrangement | Negative; 1.0% nuclei | % of 200 nuclei | "MECOM (EVI1) 3q26.2 rearrangement NEGATIVE 1.0%" — p.1, FISH table |
| CYTO-027 | FISH — -5/5q- (EGR1), deletion 5q31 | Negative; 1.5% nuclei | % of 200 nuclei | "-5/5q- (EGR1) deletion 5q31 NEGATIVE 1.5%" — p.1, FISH table |
| CYTO-028 | FISH — -7/7q- (D7S486), monosomy 7/del(7q) | Negative; 1.0% nuclei | % of 200 nuclei | "-7/7q- (D7S486) monosomy 7 / del(7q) NEGATIVE 1.0%" — p.1, FISH table |
| CYTO-029 | FISH — TP53 (17p13.1), deletion 17p | Negative; 2.0% nuclei | % of 200 nuclei | "TP53 (17p13.1) deletion 17p NEGATIVE 2.0%" — p.1, FISH table |
| CYTO-030 | FISH — cutoff statement | Reported: all within normal cutoff range | Laboratory cutoff | "All probe signal counts were within the laboratory's established normal cutoff range." — p.1, FISH table note |
| CYTO-031 | FISH — numeric cutoff values | Not reported | Not stated | No supporting statement located. |
| CYTO-032 | Interpretation — summary | **Source-reported interpretation**: normal male karyotype, negative FISH panel | Not applicable | "Normal male karyotype (46,XY) with a negative AML FISH panel." — p.1, Interpretation |
| CYTO-033 | Interpretation — recurrent abnormalities | **Source-reported interpretation**: none detected by either method (within tested scope) | Karyotype and FISH | "No recurrent cytogenetic abnormality of acute myeloid leukemia was detected by either method." — p.1, Interpretation |
| CYTO-034 | Interpretation — category | **Source-reported interpretation**: cytogenetically normal | Not applicable | "This places the case in the cytogenetically normal category." — p.1, Interpretation |
| CYTO-035 | Interpretation — pending molecular study | Reported: molecular testing ordered separately | Not applicable | "has been ordered separately (see accession MMD-26-NGS-22150)" — p.1, Interpretation |
| CYTO-036 | Microarray / other cytogenomic assay | Not reported | Not applicable | No supporting statement located. |
| CYTO-037 | Signing director | Reported: Helena V. Brandt, PhD, FACMG, 2026-04-29 | Not applicable | "Reviewed and electronically signed by Helena V. Brandt, PhD, FACMG, Director of Cytogenetics, 2026-04-29." — p.1, footer |

### MOLEC — Pathology_Report_4_molecular_ngs.pdf

| Finding ID | Field / population | Reported value / status | Method / units / denominator | Exact quote and location |
|---|---|---|---|---|
| MOLEC-001 | Patient identity — name | Reported: DOE, JONATHAN R. | Not applicable | "DOE, JONATHAN R." — p.1, Patient box |
| MOLEC-002 | Patient identity — MRN/DOB | Reported: MRN-4471902; 1967-09-14 | Not applicable | "MRN MRN-4471902 \| DOB 1967-09-14" — p.1, Patient box |
| MOLEC-003 | Patient identity — age/sex | Reported: 58 y, Male | Not applicable | "58 y / Male" — p.1, Patient box |
| MOLEC-004 | Study identity — reference accession | Reported: MMD-26-NGS-22150 | Not applicable | "Reference accession MMD-26-NGS-22150" — p.1, Specimen box |
| MOLEC-005 | Study identity — client accession | Reported: S26-BM-01187 | Not applicable | "Client accession S26-BM-01187" — p.1, Specimen box |
| MOLEC-006 | Specimen | Reported: bone marrow aspirate, EDTA | Not applicable | "Bone marrow aspirate, EDTA" — p.1, Specimen box |
| MOLEC-007 | Collection date | Reported: 2026-04-22 | Not applicable | "Collected 2026-04-22" — p.1, Specimen box |
| MOLEC-008 | Received date | Reported: 2026-04-25 | Not applicable | "Received 2026-04-25" — p.1, Requested By box |
| MOLEC-009 | Report date | Reported: 2026-05-04 | Not applicable | "Reported 2026-05-04" — p.1, Requested By box |
| MOLEC-010 | Performing laboratory | Reported: Meridian Molecular Diagnostics, CLIA 14D8888888 | Not applicable | "CLIA 14D8888888 • Lab Director: Okafor, Daniel U., MD, PhD" — p.1, letterhead |
| MOLEC-011 | Laboratory accreditation | Reported: CAP-accredited / CLIA-certified | Not applicable | "CAP-accredited / CLIA-certified reference laboratory" — p.1, letterhead |
| MOLEC-012 | Requesting institution | Reported: Riverbend Regional Medical Center | Not applicable | "Riverbend Regional Medical Center" — p.1, Requested By box |
| MOLEC-013 | Clinical history provenance | Reported: provided by the ordering site | Not applicable | "CLINICAL HISTORY (PROVIDED BY ORDERING SITE)" — p.1, section heading |
| MOLEC-014 | Clinical history — prior disease/therapy | Negative (as stated in the provided history) | Clinical history statement | "No prior hematologic history, no prior chemotherapy or radiation." — p.1, Clinical History |
| MOLEC-015 | Assay name and scope | Reported: 54-gene myeloid NGS panel | Not applicable | "MYELOID NEOPLASM NEXT-GENERATION SEQUENCING PANEL (54-GENE) — FINAL REPORT" — p.1, title |
| MOLEC-016 | Overall result | Reported: positive | Not applicable | "POSITIVE — Clinically significant variants detected." — p.1, Result Summary |
| MOLEC-017 | Variant group 1 (NPM1) — identity | Reported: NM_002520.7:c.860_863dup p.(Trp288CysfsTer12) | HGVS; transcript NM_002520.7 | "NM_002520.7:c.860_863dup p.(Trp288CysfsTer12)" — p.1, Detected Variants table |
| MOLEC-018 | Variant group 1 (NPM1) — consequence | Reported: frameshift insertion, type A, 4-bp TCTG duplication | Not applicable | "Frameshift insertion (type A, 4-bp TCTG duplication)" — p.1, Detected Variants table |
| MOLEC-019 | Variant group 1 (NPM1) — measurement | Reported: VAF 39% | Variant allele frequency, NGS | "39%" in NPM1 row, VAF column — p.1, Detected Variants table |
| MOLEC-020 | Variant group 1 (NPM1) — tier | Reported: Tier I | Laboratory tiering | "NPM1 (Tier I)" — p.1, Result Summary |
| MOLEC-021 | Variant group 2 (FLT3) — identity | Reported: internal tandem duplication, exon 14 (~36 bp insertion) | Not applicable | "Internal tandem duplication, exon 14 (~36 bp insertion)" — p.1, Detected Variants table |
| MOLEC-022 | Variant group 2 (FLT3) — consequence | Reported: in-frame ITD | Not applicable | "In-frame ITD;" — p.1, Detected Variants table |
| MOLEC-023 | Variant group 2 (FLT3) — measurement (VAF) | Reported: VAF 31% | VAF, NGS | "31%" in FLT3 row, VAF column — p.1, Detected Variants table |
| MOLEC-024 | Variant group 2 (FLT3) — measurement (allelic ratio) | Reported: ITD/WT allelic ratio 0.62 | Ratio, fragment analysis (see MOLEC-025). Not converted to VAF. | "ITD/WT allelic ratio 0.62" — p.1, Detected Variants table |
| MOLEC-025 | Variant group 2 (FLT3) — ratio method | Reported: fragment analysis run in parallel | Capillary fragment analysis | "FLT3-ITD allelic ratio estimated by fragment analysis run in parallel." — p.1, table footnote |
| MOLEC-026 | Variant group 2 (FLT3) — tier | Reported: Tier I | Laboratory tiering | "FLT3 internal tandem duplication (Tier I)" — p.1, Result Summary |
| MOLEC-027 | Variant group 2 (FLT3) — transcript / HGVS | Not reported | Not applicable | No supporting statement located. |
| MOLEC-028 | Variant group 3 (DNMT3A) — identity | Reported: NM_022552.5:c.2645G>A p.(Arg882His) | HGVS; transcript NM_022552.5 | "NM_022552.5:c.2645G>A p.(Arg882His)" — p.1, Detected Variants table |
| MOLEC-029 | Variant group 3 (DNMT3A) — consequence | Reported: missense, R882 hotspot | Not applicable | "Missense, R882 hotspot" — p.1, Detected Variants table |
| MOLEC-030 | Variant group 3 (DNMT3A) — measurement | Reported: VAF 44% | VAF, NGS | "44%" in DNMT3A row, VAF column — p.1, Detected Variants table |
| MOLEC-031 | Variant group 3 (DNMT3A) — tier | Reported: Tier II | Laboratory tiering | "DNMT3A (Tier II)" — p.1, Result Summary |
| MOLEC-032 | Tier definitions | Reported | Not applicable | "Tier I: variants of strong clinical significance. Tier II: variants of potential clinical significance." — p.1, table footnote |
| MOLEC-033 | Genes with no reportable variant | Negative within assay scope and limits, for the 30 listed genes only | NGS, approximately 5% VAF sensitivity (MOLEC-042) | "No reportable variant detected in: CEBPA, RUNX1, TP53, ASXL1, IDH1, IDH2, NRAS, KRAS, KIT, TET2, SRSF2, U2AF1, SF3B1, EZH2, BCOR, STAG2, PTPN11, WT1, PHF6, ZRSR2, JAK2, CALR, MPL, SETBP1, CSF3R, NF1, RAD21, GATA2, ETV6, CBL." — p.1, Selected Genes With No Reportable Variant |
| MOLEC-034 | Full gene list / coverage appendix | Not reported in the document (kept by the laboratory) | Not applicable | "(Full 54-gene list and coverage metrics in appendix retained by the laboratory.)" — p.1, Selected Genes With No Reportable Variant |
| MOLEC-035 | Interpretation — NPM1 | **Source-reported interpretation** | Not applicable | "mutated NPM1 is a World Health Organization and ICC disease-defining genetic abnormality" — p.1, Interpretation |
| MOLEC-036 | Interpretation — diagnosis | **Source-reported interpretation**: AML with mutated NPM1 | Not applicable | "the diagnosis is therefore acute myeloid leukemia with mutated NPM1, and a blast threshold of 20% is not required for this entity" — p.1, Interpretation |
| MOLEC-037 | Interpretation — FLT3-ITD | **Source-reported interpretation** (prognostic and predictive) | Not applicable | "The concurrent FLT3-ITD is prognostically adverse and is a target for FLT3 inhibitor therapy; the allelic ratio is reported to support treatment decisions." — p.1, Interpretation |
| MOLEC-038 | Interpretation — DNMT3A origin | **Source-reported interpretation** | Not applicable | "is frequently a clonal hematopoiesis founder event" — p.1, Interpretation |
| MOLEC-039 | Interpretation — DNMT3A and category | **Source-reported interpretation** | Not applicable | "it does not by itself define or change the WHO/ICC disease category, and is reported here for completeness and potential prognostic relevance" — p.1, Interpretation |
| MOLEC-040 | Method | Reported: hybrid-capture targeted NGS of 54 genes, genomic DNA from bone marrow | Not applicable | "Hybrid-capture targeted NGS of 54 myeloid-associated genes performed on genomic DNA from bone marrow." — p.1, Methodology & Limitations |
| MOLEC-041 | Coverage | Reported: mean 1,150x; minimum 250x | Read depth | "Mean target coverage 1,150x; minimum 250x." — p.1, Methodology & Limitations |
| MOLEC-042 | Sensitivity | Reported: approximately 5% VAF for SNVs and small indels; ITD supplemented by fragment analysis | VAF | "Analytical sensitivity approximately 5% VAF for single-nucleotide variants and small indels; FLT3-ITD detection supplemented by capillary fragment analysis." — p.1, Methodology & Limitations |
| MOLEC-043 | Limitation — structural / copy-number | Reported: not reliably detected | Not applicable | "The assay does not reliably detect large structural rearrangements, copy-number changes, or variants in regions of low coverage or high homology." — p.1, Methodology & Limitations |
| MOLEC-044 | Limitation — negative results | Reported | Not applicable | "A negative result does not exclude a mutation below the limit of detection." — p.1, Methodology & Limitations |
| MOLEC-045 | Regulatory status | Reported: LDT, not FDA-cleared | Not applicable | "This laboratory-developed test was validated by Meridian Molecular Diagnostics; it has not been cleared or approved by the FDA." — p.1, Methodology & Limitations |
| MOLEC-046 | Signatories | Reported: Okafor, Daniel U., MD, PhD; Lucia M. Fernandez, PhD; 2026-05-04 | Not applicable | "Electronically signed: Okafor, Daniel U., MD, PhD, Laboratory Director, and Lucia M. Fernandez, PhD, Variant Scientist — 2026-05-04." — p.1, footer |
| MOLEC-047 | Germline / paired-normal testing | Not reported | Not applicable | No supporting statement located. |

---

## 3. Criteria assessment

Source: WHO5E_MYEOID_2022, the uploaded original. Page numbers are journal pages; PDF page = journal page − 1702.

| Criterion ID | Criterion in plain language | Source / section / table | Brief supporting excerpt or precise citation | Case finding IDs | Assessment | Reason / missing evidence |
|---|---|---|---|---|---|---|
| C1 | The case has a defining genetic abnormality listed for a Table 7 type: an **NPM1 mutation** (AML with defining genetic abnormalities family). | AML section, "Enhanced grouping framework…" (p.1708); Table 7 (p.1709); "AML with defining genetic abnormalities" text (p.1709) | Table 7 lists "Acute myeloid leukaemia with NPM1 mutation" under "Acute myeloid leukaemia with defining genetic abnormalities". | MOLEC-017, MOLEC-018, MOLEC-019, MOLEC-020 | **Met** | NPM1 frameshift c.860_863dup was reported at VAF 39%, Tier I. The overview does not define which NPM1 variant types qualify, so that detail is left for Blue Book or pathologist confirmation. |
| C2 | The 20% blast requirement is removed for AML with defining genetic abnormalities, except AML with BCR::ABL1 and AML with CEBPA mutation. AML with NPM1 mutation may be diagnosed irrespective of blast count. | p.1708, AML framework paragraph; p.1709, "AML defined by mutations…" | "with the exception of AML with BCR::ABL1 fusion and AML with CEBPA mutation" (p.1708); "AML with NPM1 mutation can be diagnosed irrespective of the blast count" (p.1709) | MORPH-017, MORPH-026, MORPH-049, FLOW-019, MORPH-014, MOLEC-017 | **Met** (no blast threshold applies) | The measurements disagree and are kept separate: 18% (500-cell manual aspirate), 22% TNC (flow), 41% peripheral blood (clinical history). None needs to reach 20% for this type. |
| C3 | Without a blast cutoff, the defining abnormality must correlate clinicopathologically with the morphology, so that it plausibly drives the disease. | p.1708 ("Removal of the blast cutoff requires correlation between morphologic findings and the molecular genetic studies"); p.1709 ("albeit again with emphasis on judicious clinicopathologic correlation"; NPM1 in CH context) | Quoted excerpts in the previous column | MORPH-037, MORPH-038, MORPH-048, FLOW-050, FLOW-051, FLOW-052, MOLEC-019, MOLEC-038 | **Met** on the reported evidence. Pathologist confirmation is required. | The marrow is about 90–95% cellular, with sheets of immature cells and an abnormal myeloid blast population plus an expanded monocytic compartment. NPM1 is at VAF 39%. The source notes that CH can acquire NPM1, and DNMT3A (VAF 44%) is described by MOLEC as frequently a CH founder event. Correlating the clone with the leukaemic population is a human judgment. No clonal fraction was calculated here. |
| C4 | The neoplasm is myeloid. Lineage criteria for mixed-phenotype acute leukaemia (B or T lineage per Table 13) are not met. | Introduction p.1704 (integration of morphology, immunophenotype, molecular, cytogenetic data); Table 13 and footnotes (p.1714) | Table 13: T lineage requires CD3 (cytoplasmic or surface). B lineage requires CD19 with CD10/CD22/CD79a. Myeloid lineage includes "Monocytic differentiation: 2 or more expressed: Non-specific esterase, CD11c, CD14, CD64 or lysozyme". | FLOW-027, FLOW-029, FLOW-030, FLOW-032, FLOW-039, FLOW-040, FLOW-041, FLOW-043, MORPH-044, MORPH-045 | **Met** (myeloid). Table 13 B/T criteria not met. | cyCD3 and CD19 are negative on blasts. Myeloid antigens are expressed. The monocytic population expresses CD14, CD64 and CD11c, and NSE is positive. CD7 (partial) is aberrant but is not a Table 13 T-lineage criterion. |
| C5 | AML with CEBPA mutation (a Table 7 type that still requires ≥20% blasts). | p.1708; p.1709 (CEBPA paragraph) | Defined as biallelic or single bZIP CEBPA mutations (p.1709) | MOLEC-033, MOLEC-044 | **Not met** | No reportable CEBPA variant, within assay limits (about 5% VAF). |
| C6 | Other Table 7 rearrangement or fusion types tested by FISH: PML::RARA, RUNX1::RUNX1T1, CBFB::MYH11, KMT2A rearrangement, MECOM rearrangement. | Table 7 (p.1709); text p.1709 | Table 7 type list | CYTO-018, CYTO-019, CYTO-022, CYTO-023, CYTO-024, CYTO-025, CYTO-026, CYTO-030 | **Not met** (within tested scope) | Karyotype 46,XY[20] at 400–425 bphs. FISH is negative for these targets, with 200 nuclei per probe and results within lab cutoffs. |
| C7 | Table 7 types not specifically targeted: NUP98 rearrangement, DEK::NUP214, RBM15::MRTFA, BCR::ABL1. | Table 7 (p.1709); p.1709 text | "particularly NUP98, may be cryptic on conventional karyotyping" (p.1709) | CYTO-018, CYTO-019, CYTO-020, CYTO-021, MOLEC-043 | **Unknown** | There was no targeted FISH or RNA fusion test. The karyotype showed no structural abnormality at the stated resolution. NGS does not reliably detect structural rearrangements. The overview gives no rule for ranking two co-occurring defining abnormalities, so this is kept as an unresolved issue. It does not negate C1. |
| C8 | AML, myelodysplasia-related: Table 8 cytogenetic or somatic mutation abnormality, and/or a history of MDS or MDS/MPN. | AML section, Table 8 and AML-MR text (p.1710) | "The presence of one or more cytogenetic or molecular abnormalities listed in Table 8 and/or history of MDS or MDS/MPN are required for diagnosing AML-MR." | CYTO-018, CYTO-019, CYTO-027, CYTO-028, CYTO-029, MOLEC-033, MORPH-015, FLOW-013 | **Not met** | Normal karyotype. FISH negative for 5q, 7/7q and 17p. All eight Table 8 genes (ASXL1, BCOR, EZH2, SF3B1, SRSF2, STAG2, U2AF1, ZRSR2) are on the no-reportable-variant list. No prior hematologic history is reported. |
| C9 | AML defined by differentiation (Table 9) applies only when criteria for AML types with defined genetic alterations are not met. | AML defined by differentiation (p.1710); Table 9 shared-criteria footnote (p.1711) | "Criteria for AML types with defined genetic alterations are not met." (Table 9 footnote) | MOLEC-017 (via C1), FLOW-052 | **Not applicable** | C1 is met, so no Table 9 differentiation type is assigned. FLOW's "AML with monocytic differentiation" stays as a source-reported descriptor. |
| C10 | Myeloid neoplasm post cytotoxic therapy requires a documented history of cytotoxic therapy or large-field radiation. NPM1 cases with such a history would still receive this designation. | Secondary myeloid neoplasms (pp.1710–1711) | "Cases with a 'de novo molecular signature' such as NPM1 mutation … should still be assigned to this category" (p.1711) | MORPH-015, FLOW-013, CYTO-011, MOLEC-014 | **Not met** | All four reports state "no prior chemotherapy or radiation". PARP1 inhibitor exposure, a qualifying criterion per p.1711, is not specifically addressed. |
| C11 | "Associated with germline [gene] variant" qualifier for germline predisposition. Family history and genetic counselling evaluation are expected. | Secondary myeloid neoplasms (p.1710); germline predisposition section and Table 10 (pp.1711–1712) | "Genetic counseling and evaluation of family history is an expected component of the diagnostic evaluation of index patients." (p.1712) | MOLEC-047, MOLEC-033 | **Unknown** | No germline or paired-normal testing and no family history are reported. Tumour-only NGS cannot settle the germline question. The overview presents this as a qualifier, not a prerequisite for the C1 type. |
| C12 | AML arising from a prior MPN is kept in the MPN category (blast phase), not classified as de novo AML. | Secondary myeloid neoplasms (p.1710); Table 9 footnote ("No prior history of myeloproliferative neoplasm") (p.1711) | "AML transformation of MPN is retained in the MPN category" (p.1710) | MORPH-015, FLOW-013, MOLEC-033 | **Not met** | No prior hematologic history is reported. JAK2, CALR and MPL have no reportable variant. |

**Classification status: supported.** The WHO 5th edition type *Acute myeloid leukaemia with NPM1 mutation* rests on:
- C1, C2, C3 and C4, which are met.
- The competing or overriding categories in C8, C10 and C12, which are not met.
- C9, which does not apply.

C7 and C11 remain unknown. They are disclosed as unresolved issues and do not cancel C1 under the retrieved overview. The overview cannot rule on how two co-occurring defining abnormalities should be ranked.

---

## 4. Integrated teaching draft

**Synthetic teaching draft — human review required**

### 1. Patient and specimen
- DOE, JONATHAN R.; MRN-4471902; DOB 1967-09-14; 58-year-old male [MORPH-001; MORPH-002; MORPH-003; FLOW-001; FLOW-002; FLOW-003; CYTO-001; CYTO-002; CYTO-004; MOLEC-001; MOLEC-002; MOLEC-003].
- Bone marrow aspirate and core biopsy, left posterior iliac crest, collected 2026-04-22 [MORPH-005; MORPH-009; MORPH-010; FLOW-006; CYTO-005; MOLEC-007].
- Identity is consistent across all four component reports.

### 2. Component studies, accessions, and laboratories
- **Morphology:** S26-BM-01187. Riverbend Regional Medical Center (CLIA 14D9999999). Reported 2026-04-24, FINAL (morphology component). Signed by Marcus T. Whitfield, MD [MORPH-004; MORPH-006; MORPH-007; MORPH-055; MORPH-056].
- **Flow cytometry:** FC-26-003942. Riverbend Flow Cytometry Laboratory. Resulted 2026-04-23, FINAL. Verified by Priya N. Raghavan, MD [FLOW-004; FLOW-008; FLOW-010; FLOW-011; FLOW-057].
- **Cytogenetics/FISH:** CG-26-00871. Riverbend Cytogenetics Laboratory. Reported 2026-04-29, FINAL. Signed by Helena V. Brandt, PhD, FACMG [CYTO-003; CYTO-006; CYTO-008; CYTO-009; CYTO-037].
- **Molecular NGS:** reference MMD-26-NGS-22150, client S26-BM-01187. Meridian Molecular Diagnostics (CLIA 14D8888888). Received 2026-04-25, reported 2026-05-04. Signed by Daniel U. Okafor, MD, PhD, and Lucia M. Fernandez, PhD [MOLEC-004; MOLEC-005; MOLEC-008; MOLEC-009; MOLEC-010; MOLEC-046].

### 3. Clinical context
- Three weeks of progressive fatigue, exertional dyspnea, gingival bleeding and lower-extremity ecchymoses [MORPH-012].
- Admission CBC: WBC 38.4 x10^9/L, hemoglobin 7.9 g/dL, platelets 31 x10^9/L [MORPH-013].
- The clinical history states 41% circulating blasts on peripheral smear [MORPH-014; FLOW-012; CYTO-012]. The primary peripheral blood report was not provided.
- No prior hematologic history, chemotherapy or radiation [MORPH-015; FLOW-013; CYTO-011; MOLEC-014].

### 4. Morphology
- **Aspirate:** adequately cellular and spicular [MORPH-016].
- **500-cell manual differential:**
  - 18% blasts [MORPH-017]
  - 4% promonocytes, enumerated separately. The report calls their assignment "morphologically subjective" [MORPH-026; MORPH-027].
  - 6% mature monocytes [MORPH-025]
- **Blasts:** medium-to-large with a high N:C ratio and 1–3 nucleoli. A subset has folded or indented nuclei, grayish cytoplasm and fine azurophilic granulation [MORPH-030; MORPH-031].
- No definite Auer rods were seen [MORPH-034].
- **Core:** markedly hypercellular (about 90–95%), with extensive replacement by immature mononuclear cells in sheets. Megakaryocytes are markedly reduced, and fibrosis is MF-1 [MORPH-037; MORPH-038; MORPH-041; MORPH-042].
- No ring sideroblasts [MORPH-043].
- **Cytochemistry:** MPO is positive in about 5–10% of blasts. NSE is positive in a subset, with partial fluoride inhibition [MORPH-044; MORPH-045].
- **Source-reported interpretation:** "HYPERCELLULAR MARROW WITH ACUTE MYELOID LEUKEMIA", with probable monocytic differentiation [MORPH-048; MORPH-050].
- The source attributes the low aspirate count to hemodilution and to the difficulty of separating promonocytes from blasts [MORPH-052].
- No numeric core blast percentage or immunohistochemistry is reported [MORPH-047; MORPH-058].

### 5. Flow cytometry
- **Specimen:** viability 94% by 7-AAD. Eight-color panel, CD45/SSC gating [FLOW-014; FLOW-015; FLOW-017].
- **Populations, as % of total nucleated cells:**
  - Myeloid blasts 22% [FLOW-019]
  - Maturing monocytes 19% [FLOW-020]
  - Promonocytes/immature monocytic cells 11% [FLOW-021]
  - Maturing granulocytes 28% [FLOW-022]
- **Blast immunophenotype:**
  - Positive: CD34 (subset, ~60%), CD117, HLA-DR (bright), CD13, CD33 (bright), CD38, CD64, CD4 (dim) [FLOW-026 to FLOW-031; FLOW-033; FLOW-034]
  - Cytoplasmic MPO: dim subset [FLOW-032]
  - Aberrant: CD56 (partial) and CD7 (subset) [FLOW-037; FLOW-038]
  - Negative: CD14, CD2, CD19, cyCD3 [FLOW-036; FLOW-039]
- **Monocytic population:** CD14 (maturing fraction), bright uniform CD64, CD11b, CD11c, CD36, HLA-DR, dim CD4; CD34 negative [FLOW-040 to FLOW-048].
- **Source-reported interpretation:** "acute myeloid leukemia with monocytic differentiation" [FLOW-052]. The report also says the blast estimate differs from the manual count and that "either value supports the diagnosis in this context" [FLOW-054].

### 6. Cytogenetics and FISH
- **Karyotype:** 46,XY[20]. 20 metaphases counted, 5 karyotyped, 400–425 bphs. No clonal abnormality at the stated resolution [CYTO-015 to CYTO-019].
- **FISH:** interphase FISH, 200 nuclei per probe. Negative for RUNX1-RUNX1T1, CBFB, PML-RARA, KMT2A, MECOM, -5/5q-, -7/7q- and TP53/17p, all within lab cutoffs [CYTO-021 to CYTO-030]. Numeric cutoffs were not reported [CYTO-031].
- **Source-reported interpretation:** "cytogenetically normal category" [CYTO-034].
- The source's limitation that a normal karyotype does not exclude submicroscopic abnormality is retained [CYTO-020].

### 7. Molecular findings
54-gene hybrid-capture NGS. Coverage mean 1,150x and minimum 250x; sensitivity about 5% VAF [MOLEC-015; MOLEC-040 to MOLEC-042].
- **NPM1** NM_002520.7:c.860_863dup p.(Trp288CysfsTer12): frameshift (type A), VAF 39%, Tier I [MOLEC-017 to MOLEC-020].
- **FLT3** internal tandem duplication, exon 14 (~36 bp): in-frame, VAF 31%, Tier I [MOLEC-021 to MOLEC-023; MOLEC-026].
  - The ITD/WT allelic ratio of 0.62 was measured by fragment analysis [MOLEC-024; MOLEC-025]. The VAF and the ratio are reported as separate measurements and are not converted.
  - No transcript was given [MOLEC-027].
- **DNMT3A** NM_022552.5:c.2645G>A p.(Arg882His): missense, VAF 44%, Tier II [MOLEC-028 to MOLEC-031].

No reportable variant was found in the 30 listed genes, including CEBPA, TP53, RUNX1, and all eight AML-MR genes [MOLEC-033]. The full 54-gene list was not supplied [MOLEC-034]. The assay does not reliably detect structural rearrangements or copy-number changes [MOLEC-043].

### 8. Integrated interpretation
- **Myeloid neoplasm:** the marrow is extensively replaced by a myeloid neoplasm. There is an abnormal CD34+/CD117+ myeloid blast population and an expanded monocytic compartment [MORPH-037; MORPH-038; FLOW-019; FLOW-050; FLOW-051; C4].
- **Lineage:** the immunophenotype shows no B or T lineage commitment by the source's Table 13 criteria [FLOW-039; C4].
- **Genetics:** cytogenetics shows no recurrent abnormality within the tested scope [CYTO-018; CYTO-033; C6]. The molecular study identifies an NPM1 mutation, which is a defining genetic abnormality for a Table 7 AML type [MOLEC-017; MOLEC-019; C1].
- **Blast count:** the three blast measurements (18%, 22%, 41%) are not reconciled here. Under the source, AML with NPM1 mutation does not depend on a blast threshold [MORPH-017; FLOW-019; MORPH-014; C2].
- **Correlation:** the NPM1 VAF (39%) and the extent of marrow replacement are consistent with NPM1 driving the disease. However, the source's call for "judicious clinicopathologic correlation" is left for the signing pathologist [MOLEC-019; MORPH-038; C3].
- **Excluded or not applicable:**
  - Myelodysplasia-related AML, post cytotoxic therapy, and AML arising from MPN are not supported [CYTO-019; MOLEC-033; MORPH-015; C8; C10; C12].
  - Differentiation-based typing is not applicable [C9].

### 9. Diagnostic assessment
**Acute myeloid leukaemia with NPM1 mutation (WHO 5th edition, as described in the public 2022 overview by Khoury et al.) [MOLEC-017; MOLEC-019; MORPH-048; FLOW-052; C1; C2; C3; C4; C8; C9; C10; C12]**

- **Germline qualifier:** "associated with germline [gene] variant" was not assessed [MOLEC-047; C11].
- **Untested defining rearrangements:** NUP98, DEK::NUP214, RBM15::MRTFA and BCR::ABL1 were not specifically excluded [C7].
- **Source-reported component diagnoses (attribution only):**
  - MORPH: "ACUTE MYELOID LEUKEMIA" [MORPH-048]
  - FLOW: "acute myeloid leukemia with monocytic differentiation" [FLOW-052]
  - MOLEC: "acute myeloid leukemia with mutated NPM1" [MOLEC-036]
- MOLEC and MORPH also refer to ICC [MORPH-053; MOLEC-035]. ICC was not consulted, and this draft applies WHO only.

### 10. Prognostic and predictive observations
No formal risk assessment was performed. None was requested, and the ELN 2022 source was not consulted. The following is source-reported wording only:
- **MOLEC on FLT3-ITD:** "prognostically adverse and is a target for FLT3 inhibitor therapy; the allelic ratio is reported to support treatment decisions" [MOLEC-037].
- **MOLEC on DNMT3A R882H:** "frequently a clonal hematopoiesis founder event"; reported "for completeness and potential prognostic relevance" [MOLEC-038; MOLEC-039].
- **FLOW:** aberrant CD56/CD7 "may be useful for measurable residual disease tracking" [FLOW-055].

This draft adds no new prognostic, predictive, or treatment conclusion.

### 11. Limitations and unresolved issues
1. **Defining rearrangements not specifically targeted:** NUP98, DEK::NUP214, RBM15::MRTFA, BCR::ABL1 [C7; CYTO-019; MOLEC-043]. The source says NUP98 may be cryptic on karyotyping.
2. **Germline status not evaluated:** no family history and no paired-normal testing [C11; MOLEC-047].
3. **Blast and monocytic measurements differ by method and denominator.** These are not combined or averaged here.
   - Blasts: 18% on the 500-cell manual differential [MORPH-017], 22% TNC by flow [FLOW-019], and 41% in peripheral blood per the clinical history [MORPH-014].
   - Promonocytes: 4% manual [MORPH-026] versus 11% TNC by flow [FLOW-021].
   - The source flags promonocyte assignment as subjective [MORPH-027].
4. **Clinicopathologic correlation [C3]:** DNMT3A VAF 44% is described by MOLEC as frequently a CH founder event [MOLEC-038], so correlating the NPM1 clone with the leukaemia is a pathologist judgment.
5. **NGS scope:** the full 54-gene list and coverage appendix were not provided [MOLEC-034]. The FLT3-ITD transcript/HGVS was not reported [MOLEC-027].
6. **FISH numeric cutoffs** were not reported [CYTO-031].
7. **No core immunohistochemistry or numeric core blast percentage** [MORPH-047; MORPH-058].
8. **Source scope:** WHO 5th-edition public 2022 overview only (uploaded original). It is not the full or latest Blue Book, it lacks Blue Book essential/desirable criteria, and later updates were not reviewed.
9. **Pagination:** physical PDF pagination differs from the printed "Page 1 of 1" on MORPH and FLOW [MORPH-057; FLOW-059].

---

## 5. Review stage (same conversation)

This review was done in the same conversation, not as an independent QA. It re-read the report passages (all four PDFs) and the WHO article pages listed on the source card.

| Severity | Affected statement / finding | Concern | Evidence needed or suggested correction |
|---|---|---|---|
| Moderate | Section 9 diagnosis; C7 | Several Table 7 defining rearrangements were not specifically tested. NUP98 can be cryptic on karyotype, and NGS does not reliably detect fusions. The overview gives no hierarchy for co-occurring defining abnormalities. | Consider targeted FISH or RNA fusion testing (e.g., NUP98), or document the pathologist's rationale. Check the full WHO Blue Book for hierarchy rules. |
| Moderate | Section 9 qualifier; C11 | Germline predisposition was not evaluated. Tumour-only VAFs (NPM1 39%, DNMT3A 44%) must not be read as germline or somatic origin. | Family history and germline testing per the source's expectation (p.1712), if clinically indicated. |
| Moderate | Section 8; C3 | "Met" for clinicopathologic correlation rests on reported morphology and VAF, without a formal clone-to-blast correlation. MOLEC describes DNMT3A as frequently a CH founder. | Signing pathologist confirmation. No clonal fraction should be calculated from VAFs in this draft. |
| Low | MORPH-014, FLOW-012, CYTO-012 (peripheral blood 41%) | The peripheral blood blast value comes only from clinical-history text repeated in each report. The primary peripheral blood report is absent. | Obtain the peripheral blood smear/differential report if the value is to be relied on. |
| Low | MORPH-017 vs FLOW-019; MORPH-026 vs FLOW-021 | Different methods and denominators (500-cell manual vs % TNC by flow) give discordant blast and promonocyte values. Not reconciled. | None needed for C1/C2. Retain both values as reported. |
| Low | C1 | The overview does not specify which NPM1 variant types qualify. The assessment relies on the reported frameshift and Tier I annotation. | Confirm against the full WHO Blue Book entry. |
| Low | C10 | PARP1 inhibitor exposure (a qualifying criterion on p.1711) is not explicitly addressed in the clinical histories. | Confirm the complete therapy history. |
| Low | Source card | The WHO article was used as an uploaded original, not opened online in this conversation. PDF pp.14–17 were not opened. | None for criteria, which drew on pp.1703–1715. |
| Info | MORPH-057, FLOW-059 | Printed "Page 1 of 1" appears on physical page 2. Physical pages are cited. | None. |

Checks repeated against the original passages:
- Identity across reports
- All numeric values and units (VAFs, ratio, percentages, denominators)
- Variant strings
- That quotes are contiguous text
- Separation of source-reported from derived statements
- Scope of the WHO-only framework

No further concerns were found beyond those listed. This does not mean the draft is validated or correct. The table above lists the issues that remain open.
