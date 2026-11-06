# Model Research

Performance figures are deliberately left out of the tables below. Published numbers from different datasets cannot be compared, and this project has measured nothing yet.

## Architecture families

| Family | Plain explanation | Strengths | Weaknesses | Use here |
|---|---|---|---|---|
| CNN | Scans for local patterns, like moving a lens over the film | Well understood, works on smaller data | Limited global context | Baseline |
| ResNet | Deep CNN with shortcut connections | Stable to train | Less memory-efficient than DenseNet | Comparison |
| DenseNet | CNN where each layer sees earlier layers | Long history in CXR | High memory use at high resolution | **First baseline** |
| EfficientNet | CNN scaled for efficiency | Good accuracy per compute | Sensitive to training recipe | Later |
| Vision Transformer | Treats image as a set of patches | Global context | Data-hungry | Via pretrained encoders only |
| Swin Transformer | Transformer with local windows | Good for high resolution and 3D | More complex | CT and MRI phases |
| Vision-language model | Image encoder plus language model | Report text directly | **Hallucination; licence limits** | Research comparator |
| Foundation model | Large pretrained general encoder | Few labels needed | Unclear terms; heavy | Evaluate later |

## Image models

| Model | Task | Training data | Weights | Licence | Limits | Suitability |
|---|---|---|---|---|---|---|
| TorchXRayVision [M2] | CXR classification, 18 outputs; segmentation; features | NIH, PadChest, CheXpert, MIMIC and others per weight | Pip-installable | Code: custom (GitHub says NOASSERTION). Weight terms not stated | 224 px; not validated for Africa; no TB output | **First baseline** |
| CheXNet [M1] | Pneumonia, 14 findings | ChestX-ray14 | Community re-implementation; no licence detected | Unclear | Historic | Reference only |
| CheXzero [M12] | Zero-label detection | MIMIC-CXR | Yes | MIT code. Training-data limits may apply | Text prompts must be validated | Comparator |
| BioViL / BioViL-T [M4, M5] | Vision-language features | MIMIC-derived | Hugging Face | MIT; **card says deployed use out of scope** | English; ICU spacing | Research only |
| MedCLIP [M6] | Image-text features from unpaired data | Mixed | Yes | No licence detected in repository | Check before use | Research |
| RadImageNet [M7] | Pretrained encoders for transfer | Radiology images across modalities | By request/download | MIT code; weights: read terms | Not a CXR reader | CT, MRI transfer learning |
| MONAI models | Framework, bundles | Varies by bundle | Bundle-specific | Apache-2.0 framework | Each bundle has own licence | CT, MRI |

**Trap.** Some TorchXRayVision weights do not train every output, and the result for an untrained output is effectively random. Use `all`, or restrict to `.pathologies` for that dataset [M2].

## Report generation models

| Model | Approach | Training data | Weights | Licence | Limits | Suitability |
|---|---|---|---|---|---|---|
| R2Gen [M8] | Memory-driven transformer | MIMIC-CXR, IU X-ray | Repository | No licence detected | Older, 2020 | Teaching baseline only |
| R2GenCMN [M9] | Cross-modal memory | Same | Repository | Apache-2.0 code | Older, last pushed 2021 | Teaching baseline |
| MAIRA-2 [M10] | Grounded findings generation | MIMIC-CXR, PadChest, private USMix | Gated Hugging Face | **MSRLA, research only** | Card warns of fabricated and omitted findings; English; findings section only | **Research comparator** |
| RadFM [M11] | Generalist multimodal | Web-scale | Repository | MIT code; weight terms to confirm | Generalist | Investigate |
| MedGemma | Medical vision-language | See card | Gated | HAI-DEF terms: not banned commercially, but user must not make Google a device "manufacturer", and must obtain regulatory authorisation before distribution; indemnity [L15] | Not validated for reporting. Legal review needed | Investigate |
| CheXOne [M13] | Reasoning vision-language model | 30 public datasets | Described as open; licence not verified | Unverified | Preprint | Watch |
| UniRG-CXR [M14] | Reinforcement-tuned generation | Public | Unverified | Unverified | Preprint | Watch |

## Approaches compared

| Approach | Data need | Compute | Hallucination risk | Effort | For a small team? |
|---|---|---|---|---|---|
| Train from scratch | Very high | Very high | High | Very high | No |
| Fine-tuning an image model | Medium | Medium | N/A for classifier | Medium | Yes, later |
| Frozen encoder plus small head | Low | Low | N/A | Low | **Yes** |
| Vision-language end to end | High if trained; low if run | Needs GPU | **High** | Low to run | Comparator only |
| Retrieval-augmented generation | Needs a report archive | Medium | Medium; can import false priors | Medium | Later, and only with data rights |
| Template-based reporting | Low | Very low | **Very low** | Low | **Yes** |
| Hybrid: findings then template, optional LLM rephrase | Low to medium | Low | Low, if guarded | Medium | **Recommended** |

## Recommendation

**Phase 1 stack:**

1. **Classifier:** TorchXRayVision `densenet121-res224-all`. It runs on CPU, is well documented, and gives a reproducible first result in days.
2. **Findings layer:** project schema with explicit states and calibrated thresholds.
3. **Draft:** deterministic templates. No generative text at first.
4. **Comparator:** MAIRA-2 for research only, to test the hybrid hypothesis.

**Why this order.** A template can only state what the findings contain, so it cannot invent. It is cheap and explainable. Its output is limited and repetitive, but measuring that against generative output is itself the research question.

**Limitations to state openly.**

- The first classifier has no TB output. In Kenya that is a significant clinical gap.
- 224 px resolution will miss fine detail.
- No Kenyan validation exists.
- Template reports cover only what the classifier supports. Everything else must read "not assessed by AI", which the reviewer must then check.

## The licence lineage problem

A model carries its training data's obligations in practice, whatever the licence on the code says.

| Asset | Research use | Publish | Product |
|---|---|---|---|
| TorchXRayVision `all` weights | Yes | Yes | **Unclear**: trained on restricted data, and weight terms not stated |
| MAIRA-2 | Yes | Yes | **No** |
| BioViL-T | Yes | Yes | Card: out of scope |
| Own model trained on MIMIC | Yes | Yes, code must be shared | **Unclear; assume no until advised** |
| Own model trained on RSNA Pneumonia | Yes | Yes | Possible, once attribution terms are read |
| Rule-based QA | Yes | Yes | **Yes**: no data lineage issue |
| Templates and schema | Yes | Yes | **Yes** |

Every model record must carry a lineage entry. See [Experiment tracking](EXPERIMENT_TRACKING.md). The product route probably needs a model trained on properly licensed Kenyan data, under agreement, or a licensed commercial engine.

## Unresolved

- Does TorchXRayVision's custom licence cover commercial use? Read `LICENSE`.
- Which composition of datasets went into the `all` weights? Confirm from the source, since that decides what counts as an external test.
- Can MedGemma terms be met in Kenya?
- Is a licensed commercial image engine, with a project-built QA layer, a better product route than training?
