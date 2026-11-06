# Research Roadmap

## Programme

| # | Research question | Study | Needs local ethics? | Earliest |
|---|---|---|---|---|
| 1 | Where do reporting delays and costs arise in Kenya? *(added)* | Pathway study | Yes | Early, high priority |
| 2 | How do open CXR models perform on non-Western public data? | External validation | No, public data | Months 1–3 |
| 3 | How often do generated reports contain unsupported findings? | Unsupported statement study | No for public data | Months 3–6 |
| 4 | Can hybrid outperform purely generative reporting? | Head-to-head | No for public data | Months 3–9 |
| 5 | How accurately do AI reports represent important findings? | Radiologist review | Depends on data | Months 6–12 |
| 6 | How do international models perform on Kenyan data? | Silent evaluation | **Yes** | After approvals |
| 7 | Does human review improve reliability? | Seeded error study | Yes | After 6 |
| 8 | Can AI-assisted reporting reduce turnaround? | Crossover reader study | **Yes** | After 6 |
| 9 | Can it raise capacity in constrained facilities? | Pilot, service evaluation | **Yes** | After 8 |
| 10 | What are the financial implications? | Economic evaluation | **Yes** | Alongside 9 |
| 11 | What are the barriers in African hospitals? | Qualitative | Yes | Parallel to 1 |
| 12 | Does independent QA find real errors? *(added)* | Rule evaluation | No for injected; yes for real | Months 3–9 |

## Study 1: reporting pathway study

The study that links most directly to the project's origin, and needs no AI.

- **Design:** mixed-methods, cross-sectional, at a few facilities of different levels.
- **Quantitative:** timestamps from request to report; share of images reported; fees and who pays; reporter workload.
- **Qualitative:** interviews with clinicians, radiographers, radiologists, administrators and, if approved, patients and families.
- **Sampling:** consecutive examinations over an agreed period. Calculate sample size from the precision of median turnaround, after a small pilot.
- **Analysis:** medians, IQRs; time-to-report curves; thematic analysis.
- **Ethics:** ERC and NACOSTI. Family interviews need particular care around money and vulnerability.
- **Limits:** few sites; records may be incomplete; the study may itself change behaviour.

**Why first:** it might show that delays lie elsewhere, which would redirect the project before it spends heavily.

## Study 10: economics

Distinguish:

| Type | Example |
|---|---|
| Direct saving | Measured reduction in paid reader time |
| Efficiency gain | Time freed, not necessarily turned into savings |
| Capacity gain | Extra reports per shift |
| Patient cost | Actual out-of-pocket change |
| New costs | Software, compliance, validation, hardware, oversight |

Use micro-costing. **No claim that AI removes a patient fee without a real service model that shows it.**

Potential outcomes: cost per examination; turnaround; exams processed; specialist review availability; time from imaging to clinical decision; repeat reporting; delays attributable to reporting.

## Reporting guidelines

STARD-AI for diagnostic accuracy [G6]; TRIPOD+AI for prediction models [G1]; CLAIM for imaging AI [G2]; DECIDE-AI for early clinical evaluation [G5]; SPIRIT-AI and CONSORT-AI for trials [G3, G4].

## Modality timeline

| Phase | Scope | Entry condition |
|---|---|---|
| 1 | Adult chest X-ray | Now |
| 2 | Abdominal and musculoskeletal X-ray | Phase 1 evaluated |
| 3 | CT brain: haemorrhage, mass effect, midline shift, hydrocephalus | Phase 1 evaluated; partners |
| 4 | Brain MRI: T1, T2, FLAIR, DWI, ADC, contrast | CT work stable |
| 5 | Ultrasound and others. EEG as a separate neurophysiology project, not imaging | Later |

Ambition for many modalities must not delay a properly evaluated first module.

**Paediatric track.** The originating problem was paediatric neuroimaging. A paediatric module needs its own data, validation and ethics. It should be planned early even if delivered late. Note that CQ500 and BraTS-style sets do not address childhood epilepsy imaging.
