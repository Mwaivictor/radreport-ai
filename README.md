# RadReport AI

**Research project: how clinically supervised AI might make medical imaging reporting more timely, consistent and accessible in resource-constrained health systems, starting with chest X-ray in Kenya.**

> **Status: research prototype at the design stage. Not a medical device. Not clinically validated. Not for use in patient care.** No model in this repository has been evaluated on Kenyan patients. This repository contains no patient data and must never contain any.

## What this project is

Reaching a facility and having an image taken does not guarantee that a patient gets a timely, reliable interpretation. This project asks whether AI, supervised by authorised clinicians, can improve that step. It treats that as a question to measure, not a result to assume.

The work is split into three separate efforts:

1. **Evidence-grounded drafting.** Image models produce structured findings, each with an explicit state: present, absent, uncertain, or not assessed. A deterministic template turns those findings into a draft. The draft cannot state what the findings do not contain.
2. **Independent quality assurance.** Rule-based checks that work on any report, whether a person or a model wrote it.
3. **External validation.** Testing whether models trained on data from high-income settings hold up on African data.

## Where to start

| If you want to know… | Read |
|---|---|
| Why this exists | [Clinical motivation](docs/CLINICAL_MOTIVATION.md), [Problem statement](docs/PROBLEM_STATEMENT.md) |
| What is being built and for whom | [Project vision](docs/PROJECT_VISION.md), [Product requirements](docs/PRODUCT_REQUIREMENTS.md) |
| What is already known | [Literature review](docs/LITERATURE_REVIEW.md), [References](docs/REFERENCES.md) |
| Which data can be used, and on what terms | [Dataset catalog](docs/DATASET_CATALOG.md), [Data acquisition](docs/DATA_ACQUISITION_GUIDE.md) |
| Imaging basics, for clinicians and engineers | [Imaging fundamentals](docs/MEDICAL_IMAGING_FUNDAMENTALS.md), [DICOM guide](docs/DICOM_GUIDE.md) |
| How drafts and checks work | [Report generation](docs/REPORT_GENERATION.md), [Quality assurance](docs/QUALITY_ASSURANCE.md) |
| How safety and law constrain the design | [Clinical safety](docs/CLINICAL_SAFETY.md), [Privacy and regulation](docs/PRIVACY_AND_REGULATORY.md) |
| What happens next | [Implementation roadmap](docs/IMPLEMENTATION_ROADMAP.md), [Research roadmap](docs/RESEARCH_ROADMAP.md) |

## Documents

**Foundation:** [Vision](docs/PROJECT_VISION.md) · [Problem](docs/PROBLEM_STATEMENT.md) · [Motivation](docs/CLINICAL_MOTIVATION.md) · [Requirements](docs/PRODUCT_REQUIREMENTS.md) · [Literature](docs/LITERATURE_REVIEW.md) · [References](docs/REFERENCES.md)

**Data:** [Catalog](docs/DATASET_CATALOG.md) · [Acquisition](docs/DATA_ACQUISITION_GUIDE.md) · [Dictionary](docs/DATA_DICTIONARY.md) · [Preprocessing](docs/DATA_PREPROCESSING.md) · [Storage](docs/STORAGE_STRATEGY.md)

**Imaging:** [Fundamentals](docs/MEDICAL_IMAGING_FUNDAMENTALS.md) · [DICOM](docs/DICOM_GUIDE.md)

**Models and reporting:** [Model research](docs/MODEL_RESEARCH.md) · [Report generation](docs/REPORT_GENERATION.md) · [Reporting standards](docs/REPORTING_STANDARDS.md) · [Quality assurance](docs/QUALITY_ASSURANCE.md) · [Training guide](docs/MODEL_TRAINING_GUIDE.md) · [Experiment tracking](docs/EXPERIMENT_TRACKING.md)

**Evaluation and safety:** [Model evaluation](docs/MODEL_EVALUATION.md) · [Clinical validation](docs/CLINICAL_VALIDATION.md) · [Clinical safety](docs/CLINICAL_SAFETY.md) · [Privacy and regulation](docs/PRIVACY_AND_REGULATORY.md)

**System and delivery:** [Architecture](docs/SYSTEM_ARCHITECTURE.md) · [Clinical workflow](docs/CLINICAL_WORKFLOW.md) · [Infrastructure and costs](docs/INFRASTRUCTURE_AND_COSTS.md) · [Release policy](docs/GITHUB_RELEASE_POLICY.md) · [Research roadmap](docs/RESEARCH_ROADMAP.md) · [Implementation roadmap](docs/IMPLEMENTATION_ROADMAP.md) · [Publication strategy](docs/PUBLICATION_STRATEGY.md)

## Current scope

- **Modality:** adult chest X-ray only. Other modalities are planned as separate modules, each with its own validation.
- **Data:** public research data used under each dataset's terms, plus synthetic data.
- **Kenyan patient data:** none, and none until ethics, NACOSTI, institutional and legal requirements are met. See [Privacy and regulation](docs/PRIVACY_AND_REGULATORY.md).

## Licensing

- **Code:** Apache License 2.0, see [LICENSE](LICENSE).
- **Documentation:** CC BY 4.0.
- **Datasets and pretrained weights** keep their own terms and are not redistributed here. See the [catalog](docs/DATASET_CATALOG.md).

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). If you think you have found patient data or credentials here, do not open a public issue. Follow [SECURITY.md](SECURITY.md).
