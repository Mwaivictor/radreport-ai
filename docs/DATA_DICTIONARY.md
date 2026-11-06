# Data Dictionary

These are schema definitions for research work. They do not describe any collected data.

## Dataset registry (`dataset_registry`)

| Field | Type | Description | Example |
|---|---|---|---|
| `dataset_id` | text | Stable project identifier | `vindr_cxr` |
| `source_url` | text | Official source | PhysioNet URL |
| `version` | text | Exact version | `1.0.0` |
| `doi` | text | Dataset DOI | `10.13026/3akn-b287` |
| `licence` | text | Licence name and version | `PhysioNet Credentialed 1.5.0` |
| `licence_file` | text | Dated local copy of the terms | `registry/terms/vindr_2026-11-06.pdf` |
| `access_date` | date | Date obtained | |
| `accessed_by` | text | Named credentialed person | |
| `restrictions` | text | Limits on use | `research only; no third-party sharing` |
| `commercial_status` | enum | `permitted`, `restricted`, `unclear`, `prohibited` | `unclear` |
| `storage_location` | text | Where it lives | |

## File manifest (`file_manifest`)

| Field | Type | Description |
|---|---|---|
| `file_id` | uuid | Project identifier |
| `dataset_id` | text | Registry link |
| `relative_path` | text | Path within the dataset |
| `sha256` | text | File checksum |
| `size_bytes` | int | Size |
| `layer` | enum | `raw`, `derived` |
| `parent_file_id` | uuid | Source file for derived data |
| `processing_step` | text | Pipeline step and version |

## Image and study metadata (`image`)

| Field | Type | Description | Clinical meaning |
|---|---|---|---|
| `patient_key` | text | Dataset's patient ID, or a hash | Unit for splitting |
| `study_key` | text | Study ID | One examination |
| `image_key` | text | Image ID | One image |
| `view_position` | enum | `PA`, `AP`, `LATERAL`, `UNKNOWN` | AP magnifies the heart |
| `age_band` | enum | `0-9`, `10-17`, `18-39`, `40-64`, `65+`, `unknown` | Eligibility check |
| `sex` | enum | `F`, `M`, `unknown` | Subgroup analysis |
| `manufacturer` | text | Equipment, if present | Dataset shift |
| `split` | enum | `train`, `val`, `test`, `external` | Set at patient level |
| `quality_flag` | enum | `ok`, `limited`, `reject` | Adequacy |

## Label record (`label`)

| Field | Type | Description |
|---|---|---|
| `image_key` | text | Link to image |
| `finding_code` | text | Project code, see below |
| `state` | enum | `present`, `absent`, `uncertain`, `not_assessed` |
| `label_source` | enum | `report_nlp`, `single_reader`, `multi_reader_consensus`, `model` |
| `reader_count` | int | Number of readers |

**A blank label is not a negative label.** In several datasets a missing value means the finding was not mentioned. Treating that as absent is a common error.

## Phase 1 finding codes

| Code | Finding | Note |
|---|---|---|
| `NORMAL_STUDY` | No reportable abnormality | Derived, never a single model output |
| `CONSOLIDATION` | Consolidation | Radiographic sign, not pneumonia |
| `PNEUMONIA_SUSPECTED` | Opacity that may represent pneumonia | A clinical inference. Keep separate |
| `EFFUSION` | Pleural effusion | |
| `PNEUMOTHORAX` | Pneumothorax | Candidate critical finding |
| `CARDIOMEGALY` | Enlarged cardiac silhouette | Unreliable on AP films |
| `EDEMA` | Pulmonary oedema | |
| `ATELECTASIS` | Atelectasis | |
| `NODULE` | Pulmonary nodule | |
| `MASS` | Mass | |
| `TB_SUSPECTED` | Features of possible TB | **Local priority. Not in most open models** |
| `LINE_TUBE` | Lines and tubes | Position needs human check |

## Structured finding

The full schema is in [Report generation](REPORT_GENERATION.md).

## Audit event

| Field | Description |
|---|---|
| `event_id`, `timestamp_utc` | Unique, time-stamped |
| `actor_id`, `actor_role` | Who, and in what role |
| `action` | `viewed`, `edited`, `rejected_finding`, `signed` and so on |
| `object_id` | Report or finding |
| `before_hash`, `after_hash` | Evidence of change |
| `model_version` | Model involved |

## Identifiers never stored in research tables

Name, national ID, SHA number, phone, address, medical record number, exact birth date, accession number, referring clinician name, and free-text with such content.
