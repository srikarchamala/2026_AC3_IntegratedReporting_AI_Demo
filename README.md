# Integrated Reporting with AI: Chatbot vs Agent

Demo materials for **"Bridging the AI Readiness Gap: A Five-Pillar Framework for Equitable Cancer Research"**, 9th Biennial African Caribbean Cancer Consortium (AC3) Conference, Bridgetown, Barbados, October 2026.

**Open the demo:** [srikarchamala.github.io/2026_AC3_IntegratedReporting_AI_Demo](https://srikarchamala.github.io/2026_AC3_IntegratedReporting_AI_Demo/) (or download `index.html` and open it in any browser; it works offline).

> Everything here is a **synthetic teaching case**. No real patient data. Not for clinical use.

## The case

One fictional patient, one bone marrow specimen, four separately issued reports (in [`case/`](case/)):

| Report | What only it shows |
|---|---|
| `01_bone_marrow_morphology.pdf` | Blasts 18% by manual count; monocytic lineage only "probable" |
| `02_flow_cytometry.pdf` | Blasts 22% by gated count; proves monocytic lineage |
| `03_cytogenetics_fish.pdf` | Normal karyotype 46,XY[20]; AML FISH panel negative |
| `04_molecular_ngs.pdf` | NPM1 (defining), FLT3-ITD, DNMT3A R882H (not classifying) |

No single report is enough. The diagnosis is **acute myeloid leukemia with mutated NPM1, with monocytic differentiation**. The built-in trap: DNMT3A is real and prognostic but belongs in the prognostic notes, not the diagnosis line. The pathologist-authored answer key is `case/05_GOLD_STANDARD_integrated_report.pdf`.

## Three ways to do the same task

| Approach | What it is | Prompts | Outputs |
|---|---|---|---|
| **Chatbot** | Attach the four reports, ask once | [`prompts/agent_pipeline/chatbot__DEFAULT_SYSTEM_PROMPT.txt`](prompts/agent_pipeline/) | [`runs/chatbot/`](runs/chatbot/) (3 runs) |
| **Two prompts by hand** | Extract with quotes, then integrate with a trace, in any chat tool | [`prompts/two_prompt_by_hand/`](prompts/two_prompt_by_hand/) | [`runs/two_prompt_by_hand/`](runs/two_prompt_by_hand/) |
| **Agent pipeline** | 12 steps: per-report extraction, cross-report analysis, parsers, WHO classifier, QA | [`prompts/agent_pipeline/`](prompts/agent_pipeline/) | [`runs/agent_pipeline/`](runs/agent_pipeline/) |

## Try the two-prompt version yourself (no code)

You need any AI chat tool. Use only the synthetic files here, never patient data in a public tool.

1. Open a new chat. Attach the four PDFs from `case/`.
2. Paste the contents of `prompts/two_prompt_by_hand/prompt_extractor.txt`, then the contents of `schema_extractor_output.json`. Send.
3. You get one block of structured data (JSON). Every finding is tagged with its report and a quote.
4. Paste the contents of `prompt_integrator.txt`, then the JSON from step 3. Send.
5. You get the 11-section integrated report and an evidence trace: every sentence of the interpretation and diagnosis mapped to its source.
6. Compare with `case/05_GOLD_STANDARD_integrated_report.pdf`. Check the diagnosis line, both blast counts, and where DNMT3A landed. Run it again and see what changes.

## What happened in these runs

| Check | Chatbot (3 runs) | Agent pipeline | Two prompts |
|---|---|---|---|
| Diagnosis names NPM1 | 3 of 3 | Yes | Yes |
| DNMT3A kept out of the diagnosis | 0 of 3 | Yes | Yes |
| Diagnosis lines match the gold standard | 0 of 3 | Close (FLT3-ITD sent to prognostic notes) | Yes |
| Every sentence traced to a source report | No trace | 19 of 19 | 27 of 27 |
| Extracted quotes found in the source text | n/a | 61 of 61 | 33 of 33 |
| Lab names and accessions carried through | Yes | No (not in its extraction schema) | Yes |

The chatbot was usually close. The difference is that the structured versions can be checked.

**How these runs were made:** all three approaches used Claude with the prompts in this repo, one fresh call per step. The live workshop below ran on a different model, so wording differs.

## From demo to practice

A real deployment brings the model to the data: an on-premises or contractually walled-off model, fed by the lab information system rather than PDFs, producing a draft a pathologist reviews and signs, validated and governed like any other clinical tool. See Part 3 of `case/00_DEMO_GUIDE.pdf`.

## Credits

The synthetic case, the two-prompt pipeline, the gold standard and the agent pipeline come from the **Agentic Pathology Workshop**, API Summit 2026: [github.com/hesamhakim/agentic-pathology-workshop](https://github.com/hesamhakim/agentic-pathology-workshop)

- Hesam H. Javadi, PhD (Medical College of Wisconsin, Children's Wisconsin): workshop infrastructure, LangFlow components
- Srikar Chamala, PhD (Children's Hospital Los Angeles, USC Keck School of Medicine)
- Omar Baba, MD (Henry Ford Health): AML case design, gold standard, two-stage prompts

Workshop materials are used under the MIT License; see [`LICENSE-workshop-materials`](LICENSE-workshop-materials).

Contact: Srikar Chamala, schamala@chla.usc.edu
