# Implementation Roadmap

**Four weeks gets you a research foundation. It does not get you clinical validation.** Weeks are estimates for a clinician working part-time alongside rotations. Dependencies matter more than dates. PhysioNet approval time is outside your control.

## Week 1: Clinical problem and research foundation

| Task | Output |
|---|---|
| Read these documents, and correct them | Comments |
| Run the VPS read-only audit | Audit output |
| Read: *Rology* judgment, LN 77, ODPC note, PPB guideline | Updated privacy document |
| Create private GitHub repo; review, commit and push | Live repos |
| Apply for PhysioNet access; start CITI | Pending application |
| Look for a radiologist mentor; informal only, no data | Named person |
| Request Naija-CXR term clarification from the authors | Reply |
| Install Python environment | Working `torchxrayvision` |

**Deliverable:** verified research and requirements foundation.

## Week 2: Data foundation

| Task | Output |
|---|---|
| Select first data: RSNA Pneumonia subset | Dated terms; registry entry |
| Inspect format, labels, patient IDs | Notebook |
| Data quality checks | Script with test |
| Reproducible preprocessing | `cxr-0.1.0` pipeline |
| Document limitations | Dataset card |
| Add MIMIC, VinDr when access arrives | Registry entries |

**Deliverable:** reproducible CXR data pipeline.

## Week 3: Baseline model research

| Task | Output |
|---|---|
| Run pretrained baseline | Scores |
| Independent test per [Model evaluation](MODEL_EVALUATION.md) | Metrics with intervals |
| Calibration | Curves |
| Error analysis, with your clinical eye | Case table |
| Explainability on public images | Grad-CAM review |
| Record limits | Model card |

**Deliverable:** reproducible baseline experiment.

## Week 4: Reporting prototype design

| Task | Output |
|---|---|
| Finding schema, states | JSON Schema with tests |
| CXR template | Reviewed by a radiologist if possible |
| Deterministic composer | Small script |
| QA Layer 1: 5 rules | Tests with injected errors |
| Simple review page, synthetic or public data | Research prototype |
| Human evaluation protocol | Protocol draft |
| Pathway study concept note | For ethics |

**Deliverable:** end-to-end research prototype design. **Not** a clinical tool.

## Milestones

| Milestone | Criteria |
|---|---|
| M0 Foundation | Docs reviewed, repos live, VPS audited |
| **M1 First milestone** | Independent external evaluation of one open model, reproducible from a clean checkout, with limitations documented |
| M2 Prototype | Image to findings to draft to QA to review, on public data |
| M3 Preprint | External validation written up |
| M4 Partnership | Radiologist co-investigator, legal opinion, ethics application |
| M5 Local evidence | Silent evaluation in Kenya |
| M6 Reader study | Crossover study complete |

## Code limits

Do not write the platform yet. Weeks 1–4 should give a few small, tested scripts in the public repository. Build the application only after M2 shows what is needed, and after the legal path is clearer.

## Risk register

| Risk | Effect | Response |
|---|---|---|
| PhysioNet delay | Week 2–3 slip | Continue with RSNA, NIH |
| Naija-CXR terms unclear | No African test | Use for non-commercial research only |
| No radiologist partner | Stops clinical work | Priority one in Week 1 |
| Legal barrier to transfer | No offshore compute | Compute in Kenya |
| Clinical rotations | Part-time pace | Small weekly goals |
| VPS contention | Harms production | Keep research off it |
| Regulators reclassify | Added cost | Keep records from day one |

## How to run

No components exist yet. Each script added in Weeks 2–4 must come with a run command in its folder's README and a sample of expected output.
