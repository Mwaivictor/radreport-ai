# Model Evaluation

## Questions, in order

1. Is the result valid? Check for leakage and label problems.
2. How good is it, overall and in subgroups?
3. Do its probabilities mean anything?
4. Will it help a clinician?

## Classification metrics in clinical terms

| Metric | Clinical question | Caution |
|---|---|---|
| Sensitivity | Of those with the finding, how many flagged? | Depends on threshold |
| Specificity | Of those without it, how many cleared? | Depends on threshold |
| PPV | If flagged, how likely is it real? | Falls when prevalence falls |
| NPV | If not flagged, how likely is it truly absent? | Looks high when disease is rare |
| ROC-AUC | Ranking ability | Can look good in rare disease |
| PR-AUC | Precision against recall | Better for rare findings |
| F1 | Balance of PPV and sensitivity | Ignores true negatives |
| Calibration | Does 70% happen 70% of the time? | Often poor across sites |
| Brier score | Mean squared probability error | Combines discrimination and calibration |

PPV example, to show why local prevalence matters. With sensitivity 90% and specificity 90%: at 10% prevalence PPV is 50%; at 1% prevalence it is about 8%. The arithmetic is exact, and the operating point is invented for illustration.

## Localisation and segmentation

| Task | Metric |
|---|---|
| Boxes | Intersection over union; mAP at stated IoU |
| Pointing | Pointing game hit rate |
| Segmentation | Dice; Hausdorff distance |

## Design rules

- **Patient-level splits** only.
- **Report confidence intervals**, using patient-level bootstrap.
- **Handle uncertain labels explicitly**: report sensitivity to the choice.
- **Define the reference standard.** Report NLP, single reader and consensus are not equally strong.
- **External validation** means a different population, from a different source. Report it separately.
- **Pre-register** thresholds and analysis where possible.
- Follow CLAIM, TRIPOD+AI and STARD-AI [G1, G2, G6].

## Week 3 baseline protocol

| Item | Choice |
|---|---|
| Model A | `densenet121-res224-chex` (trained on CheXpert only) on an RSNA Pneumonia subset: a truly independent test, because RSNA derives from NIH data, which that weight set did not use. Confirm the weight's training data first |
| Model B | `densenet121-res224-all` on VinDr-CXR and, once terms are clear, Naija-CXR. Not on NIH or RSNA: its training includes NIH |
| Findings | Those labelled in both model and dataset |
| Primary | ROC-AUC, PR-AUC, calibration curve, Brier score, sensitivity at fixed specificity |
| Stated limitation | RSNA labels opacity, not pneumonia. So map carefully and do not call it pneumonia detection |
| Error analysis | Radiologist-guided review of false positives and negatives; look for shortcut signals |
| Explainability | Grad-CAM on selected cases, read as hypothesis only |

No target figures are set. The aim is a credible estimate, not a target score.

## Report evaluation

### Text metrics

| Metric | Measures | Limits |
|---|---|---|
| BLEU | Word sequence overlap | Blind to meaning. "No effusion" and "effusion" look nearly the same |
| ROUGE | Overlap | As above |
| METEOR | Overlap with synonyms | Weak clinical meaning |
| BERTScore | Embedding similarity | Can reward similar-sounding wrong statements |

### Clinically aware metrics

| Metric | Measures |
|---|---|
| CheXbert similarity [M16] | Agreement on extracted labels |
| RadGraph F1 [M15] | Entities and relations |
| RadCliQ [E1] | Composite tuned to radiologist error judgement |

Yu et al. found that metrics differ in sensitivity to clinically important errors [E1]. Use these for screening models only. **No text metric replaces radiologist review.**

### Project metrics

| Metric | Definition |
|---|---|
| Unsupported statement rate | Share of sentences with no support in image-based reference |
| Important omission rate | Share of reference critical findings absent |
| Laterality error rate | Share of lateralised statements with the wrong side |
| Unsupported negative rate | Share of "no X" statements not supported |
| False prior rate | Share of reports with invented comparison |
| Edit burden | Word edit distance, and time |

### Human evaluation protocol

- At least three qualified radiologists, independent of development.
- Cases sampled to include normal and abnormal, with enrichment declared.
- Blinded to the source: human report, template or generative.
- Order randomised.
- Scores per report: clinical correctness, completeness, unsupported findings, important omissions, impression quality.
- Severity scale, for example: none, not significant, significant, critical.
- Report inter-rater agreement.

Sample size guidance is in [Clinical validation](CLINICAL_VALIDATION.md).

## Comparison: hybrid against generative

Compare template or hybrid against one generative comparator on the same held-out images. Primary outcome: unsupported statement rate. Key secondary outcome: important omission rate. Report both, so a model cannot win simply by saying less.
