# Literature Review

Scope: chest radiograph AI, draft reporting, human-AI interaction, and evidence relevant to Kenya. Figures are quoted from the paper's own abstract unless marked. Search date: 2026-11-06. This is a structured narrative review, not a systematic review. A systematic review is proposed in [Publication strategy](PUBLICATION_STRATEGY.md).

## 1. Summary

1. Chest X-ray classifiers can perform strongly in retrospective tests, but performance varies by site and falls on complex studies.
2. Early evidence suggests draft reports can save documentation time. The best clinical study was prospective but non-randomised. No published randomised clinical trial was found.
3. Vision-language models frequently produce unsupported statements. One 2026 preprint found this in most outputs.
4. AI errors can degrade radiologists' performance, so a human in the loop is not automatically a safeguard.
5. African evidence is thin, with TB screening the strongest area. No open Kenyan chest X-ray dataset was found.

## 2. Does AI detect findings on chest radiographs?

**Assisted reading.** Seah et al. tested a model trained on 821,681 images across 127 findings. Twenty radiologists read 2,568 enriched adult cases with and without assistance, separated by a three-month washout [C6]. This shows the design standard: paired reading, a washout, and a broad finding set.

**Head-to-head commercial tools.** Lind Plesner et al. tested commercially available tools in 2,040 patients at four Danish hospitals. AUCs ranged 0.83–0.88 for airspace disease, 0.89–0.97 for pneumothorax and 0.94–0.97 for effusion. Sensitivities ranged 72%–91%, 63%–90% and 62%–95%. Specificity fell markedly with four or more findings: for airspace disease, from 85%–96% on simple studies to 27%–69% [C5].

*Clinical reading:* the patients who are sickest, with the most findings, are where these tools behaved worst. An average AUC would hide this.

**Generalisation.** Zech et al. showed variable performance across hospitals [B2]. Cohen et al. studied the limits of cross-domain generalisation [M3]. Oakden-Rayner et al. showed that average performance can conceal failure in important subgroups [B4]. This could be, for example, a model that detects a chest drain rather than a pneumothorax.

## 3. Does drafting save time without harming quality?

| Study | Design | Setting | Result | Limits |
|---|---|---|---|---|
| Huang 2023 [C1] | Retrospective, 500 ED encounters | US tertiary | ED physicians rated AI reports similarly to radiologist reports | Rated quality. Did not measure time |
| Hong 2025 [C3] | Retrospective, sequential, multireader; 758 CXRs, 5 radiologists | Public dataset from 2009–2017 | Reading time 34.2 ± 20.4 s to 19.8 ± 12.5 s | Small reader pool. Sequential sessions can favour the second session |
| Huang 2025 [C2] | Prospective cohort, 23,960 radiographs | Tertiary academic system | 159.8 s vs 189.2 s, a 15.5% gain. No difference in accuracy or quality on peer review of 800 studies | Not randomised. Baseline comparison. Unexpected pneumothorax sensitivity 72.7% |

**Reading the evidence fairly.** The direction is promising, but none of this is Kenyan, and none of it is randomised clinical evidence. Trials are registered, for example NCT06456203 and NCT07634861, and no results for them were found. The 72.7% pneumothorax sensitivity [C2] shows why an AI flag cannot be a safety net on its own.

## 4. Does AI work without a radiologist?

Plesner et al. assessed a CE-marked tool aimed at autonomous reporting of normal radiographs. AI sensitivity for abnormal radiographs was 99.1% against 72.3% for clinical reports, using a thoracic-radiologist reference. Only 7.8% of all posteroanterior radiographs could be autonomously reported [C4].

This matters in two ways. The potential workload effect was modest even when the tool performed well. It also looked only at adult hospital posteroanterior films in Denmark. This project does not pursue autonomous reporting.

## 5. Report generation

Early models such as R2Gen [M8] and R2GenCMN [M9] used memory-driven transformers. Current systems are vision-language models, including MAIRA-2 with grounded reporting [M10], RadFM [M11], CheXOne with reasoning traces [M13], and UniRG-CXR [M14]. Public benchmarking exists through ReXrank [E2].

**Hallucination.** HalluCXR evaluated six vision-language models on 856 stratified MIMIC-CXR radiographs. It reported hallucinations in 61.9–82.3% of outputs, with clinically dangerous errors in up to 80.2%. Normal radiographs attracted the most severe errors. Ensembling reduced fabrication by up to 84.8%, at the cost of more omissions [E3]. It is a single preprint and has not been peer reviewed, and its question format differs from a full reporting pipeline. Even so, the direction supports grounding reports in structured evidence. FactCheXcker addresses invented measurements specifically [E4].

**Metrics.** Yu et al. showed that common text metrics fail to capture clinically important errors. Radiologist-informed composites such as RadCliQ, and RadGraph-based measures, align better with what matters [E1, M15].

## 6. Human-AI interaction

Yu et al. studied 140 radiologists across 15 tasks. Experience, subspecialty and AI familiarity did not reliably predict who benefited. Inaccurate AI harmed performance on the aggregate of all pathologies and on half of the individual pathologies [C7]. Dratsch et al. found automation bias in mammography at every experience level, with very experienced readers' accuracy falling from 82.3% to 45.5% when AI was wrong [C8].

**Design consequence:** review must be structured to resist anchoring. See [Clinical safety](CLINICAL_SAFETY.md).

## 7. Bias and equity

Seyyed-Kalantari et al. found that CXR classifiers underdiagnosed under-served groups more often [B1]. Gichoya et al. showed that models can detect self-reported race from images alone, even when humans cannot, and the mechanism is not understood [B3]. So excluding race as an input does not make a model blind to it. Evaluation in African populations is needed. It cannot be inferred.

## 8. Evidence from Kenya and Africa

- **TB screening.** Using the 2016 Kenya National TB Prevalence Survey, 61,848 analysable images and 298 confirmed TB cases, CAD4TBv6 met the optimum target product profile: mean sensitivity 95%, specificity 83.3% [C9]. The WHO's 2021 screening guidance includes CAD (secondary). This is the most mature African imaging AI evidence, and it is for a narrower task than reporting.
- **Datasets.** Naija-CXR, published in 2026, pairs frontal images from a Nigerian teaching hospital with radiologist reports [D10]. BraTS-Africa provides 146 brain MRI cases from Nigerian centres [D18]. A Uganda TB study collected 1,835 images, and public access to them was not confirmed.
- **Workforce.** Reliable Kenyan numbers were not found, see [Problem statement](PROBLEM_STATEMENT.md).
- **Paediatrics.** VinDr-PCXR offers 9,125 paediatric scans from Vietnam [D6]. No African paediatric CXR dataset was found.

## 9. Existing solutions

| Type | Examples | Implication |
|---|---|---|
| Finding detection | Commercial tools evaluated in [C5] | Mature field. A new generic classifier adds little |
| Autonomous normal triage | CE-marked tool in [C4] | Possible but limited yield, and not suitable for this context yet |
| TB CAD | CAD4TB, qXR, INSIGHT CXR (secondary) | Established in screening |
| Draft reporting | Health-system models [C1, C2] | Early clinical data |
| Teleradiology in Kenya | Aga Khan, Tenwek (reported), Rology | Existing route to radiologists, now legally contested [L7] |

## 10. Gaps this project could fill

1. External validation of open CXR models on African data, with calibration and subgroup analysis.
2. Evidence-grounded drafting compared directly with end-to-end generation on unsupported statements.
3. Independent, rule-based report QA evaluated on real and injected errors.
4. A measured Kenyan reporting pathway, including cost and delay.
5. Implementation barriers after *Rology*.

## 11. Limitations of this review

Single reviewer. One date. Not PRISMA-compliant. Several sources were read only as abstracts. Company-reported claims were not used as evidence of effectiveness.
