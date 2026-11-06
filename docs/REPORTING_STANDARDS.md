# Reporting Standards

## Why structure matters

A structured report is like a structured clerking: it reduces omissions, and it can be checked. It should not force clinicians to tick boxes when narrative is better.

## Adult chest X-ray template v0.1

**To be reviewed by a radiologist before any use. Not a clinical standard.**

### Examination information

| Field | Source | If missing |
|---|---|---|
| Examination type | Metadata | Block |
| Date | Metadata | Block |
| View | Metadata plus image check | "View not confirmed" |
| Clinical indication | Request | "Not provided". Never inferred |
| Comparison | Linked prior | "None available" |

### Technique

Projection; image adequacy: rotation, inspiration, penetration, coverage; technical limitations.

### Findings

| Section | Check |
|---|---|
| Lungs | Consolidation, nodules, masses, oedema, atelectasis |
| Pleura | Effusion, pneumothorax, thickening |
| Heart | Cardiac silhouette. On AP, size is limited |
| Mediastinum | Width, contour, trachea |
| Hila | Size, density |
| Diaphragm | Contour, free gas under diaphragm if visible |
| Costophrenic angles | Blunting |
| Bones | Fractures, lytic or sclerotic lesions |
| Soft tissues | Swelling, surgical emphysema |
| Lines and tubes | Position, needs human confirmation |

### Impression

Principal findings first, then relevant secondary findings, with appropriate uncertainty. Must follow from Findings.

### Recommendations

Only when supported and appropriate. Phase 1 output: none generated. The reviewer may add them.

### Status line

Mandatory on every page, in plain language: `AI-GENERATED DRAFT`, `PRELIMINARY`, or `FINAL: signed by [name, registration, time]`.

## Terminology

| Standard | Purpose | Use |
|---|---|---|
| Fleischner Glossary [G7] | Thoracic imaging terms | Vocabulary for CXR findings |
| RadLex | Radiology lexicon, from RSNA | Coded terms |
| SNOMED CT | Clinical terminology | Licence and national membership need checking |
| RadElement CDEs | Common data elements | Consider for findings schema |
| RSNA RadReport | Template library | Starting examples; check terms |

**Uncertainty language** needs a defined scale, agreed with radiologists. For example: "consistent with", "suggestive of", "possible". Each phrase maps to a state. Studies show people read such words differently, so keep the list short.

## Consolidation is not pneumonia

Reporting language must separate sign from diagnosis.

| Radiographic | Clinical inference |
|---|---|
| Consolidation | Pneumonia, in the right clinical setting |
| Enlarged cardiac silhouette | Cardiomegaly or pericardial effusion |
| Upper-zone opacity with cavitation | TB is possible. Needs microbiology |

## Other modalities need their own templates

Do not reuse this template. CT brain needs density, ventricles, midline, extra-axial spaces and bone. MRI needs sequence-based reporting. Abdominal X-ray and musculoskeletal films have their own structure.

## Critical result communication

Follow the local policy and professional standards. Direct, documented, acknowledged communication is the norm in international practice. The workflow is in [Clinical workflow](CLINICAL_WORKFLOW.md).

## Exchange formats

| Format | Use |
|---|---|
| PDF | Human-readable, must carry status |
| FHIR `DiagnosticReport` | Interoperable result |
| DICOM SR | Structured, tied to images |
| JSON | Internal, carries `finding_id` links |

## Open items

- Does the Kenya Association of Radiologists or a teaching hospital have a reporting template to align with?
- Which terminology has a workable Kenyan licence?
- English only for Phase 1. Is Kiswahili needed for patient-facing explanation later?
