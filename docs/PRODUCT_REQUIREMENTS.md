# Product Requirements

Status: design requirements for a **research prototype**. Nothing here describes a released product.

## Product definition

A workflow to receive an imaging examination, inspect it, obtain AI-assisted structured findings, generate a draft, and send it to an authorised reviewer who edits, rejects or signs it.

## Output states

These four states must never be confused, in the database, in the interface or on any export.

| State | Meaning | Who creates it | May reach a treating clinician? |
|---|---|---|---|
| AI prediction | Model output for one finding | Model | No, unless a validated, approved use exists |
| AI-generated draft | Text assembled from predictions | System | No |
| Preliminary interpretation | Clinician's own provisional read, labelled as such | Authorised clinician | Yes, labelled preliminary |
| Authorised final report | Signed formal report | Authorised reporter | Yes |

No automatic or time-based transition may ever turn a draft into a final report.

## Users, permissions and responsibilities

The table below is a **default to confirm** with the institution, KMPDC and the Clinical Officers Council. This project could not confirm who may legally issue a formal radiology report in Kenya. Until that is settled, only a consultant radiologist signs.

| Role | View images and drafts | Edit draft | Issue preliminary | Sign final | Configure | Responsibility |
|---|---|---|---|---|---|---|
| Consultant radiologist | Yes | Yes | Yes | **Yes** | No | Final report content |
| Radiology registrar | Yes | Yes | Yes | Only under institutional policy, countersigned | No | Draft accuracy under supervision |
| Medical officer | Yes | No | Own clinical note only | No | No | Own clinical decision |
| Clinical officer | Yes | No | Own clinical note only | No, unless authorised in writing | No | Own clinical decision |
| Emergency or paediatric clinician | Yes | No | Own clinical note only | No | No | Own clinical decision |
| Radiographer | Image and technique only | Technique fields | No | No | No | Image quality and metadata |
| Hospital administrator | Operational metrics, no clinical content | No | No | No | Facility settings | Service governance |
| Researcher | Approved de-identified sets only | No | No | No | No | Protocol compliance |
| Developer | Synthetic or public data only | No | No | No | System | Software safety |

**Rule:** a user who cannot issue a formal report cannot gain that power because AI produced the draft.

Paediatric clinicians are a future user group. The Phase 1 module excludes patients under 18 at ingestion until paediatric validation exists.

## Core workflow

1. Examination requested.
2. Image acquired.
3. Examination enters the imaging system.
4. Platform receives it by upload or from PACS.
5. Image and metadata validated.
6. Modality-specific engine runs.
7. Structured findings extracted.
8. Uncertainty and technical limits identified.
9. Draft assembled.
10. Reviewer opens the **original image** and the draft.
11. Reviewer edits, corrects or rejects each finding.
12. Authorised professional signs.
13. Report released to the clinical team.
14. Complete audit trail retained.

## Features

Priority: **P0** research prototype, **P1** pilot, **P2** later.

| Feature | Priority | Clinical purpose | Risk if done badly |
|---|---|---|---|
| Image upload | P0 | Starting point for research | Identifiers uploaded by accident |
| De-identification gate | P0 | Prevents PHI entering research systems | Privacy breach |
| Input validation | P0 | Rejects wrong body part, age, view | Model used outside its limits |
| AI inference | P0 | Candidate findings | Over-trust |
| Finding states and uncertainty | P0 | Prevents false certainty | Silent false negatives |
| Report templates | P0 | Consistent structure | Forcing one structure on all modalities |
| Report editing | P0 | Human control | Automation bias |
| Audit log | P0 | Accountability | Unattributable decisions |
| Report status tracking | P0 | Prevents draft being treated as final | Draft used clinically |
| Quality assurance checks | P0 | Catches laterality and contradictions | False reassurance |
| Abnormality localisation | P1 | Shows the reviewer where to look | Saliency maps misread as proof |
| DICOM ingestion | P1 | Real-world data | Tag handling errors |
| Patient and study management | P1 | Links examinations | Wrong-patient error |
| Image viewer | P1 | Diagnostic-quality review | Non-diagnostic display |
| Turnaround monitoring | P1 | Measures the problem | Metric pressure |
| Exportable reports | P1 | Delivers results | Unlabelled draft export |
| Comparison with priors | P2 | Temporal context | Invented comparison |
| Second-opinion workflow | P2 | Specialist access | Credential gaps |
| Critical-findings alerts | P2 | Urgent escalation | Sole reliance on the alert |
| Segmentation | P2 | Measurement | Spurious precision |
| PACS, RIS, HL7, FHIR integration | P2 | Reduces re-entry | Patient mix-ups |

## Non-functional requirements

- **Traceability:** each sentence links to a finding, a model version and an examination.
- **Reversibility:** originals are never altered.
- **Availability:** failure of AI must never block reporting. Reporters fall back to usual practice.
- **Low-bandwidth use:** must work on constrained connections. Study this in the field.
- **Data location:** live Kenyan data is processed in Kenya unless legal advice clearly permits otherwise.
- **Registration readiness:** keep the records PPB, ODPC, the Digital Health Agency and KMPDC would ask for.

## Compliance gates

Before any live patient use, all of these must be complete. See [Privacy and regulation](PRIVACY_AND_REGULATORY.md).

- Ethics approval and NACOSTI licence.
- Institutional agreement naming the health-care provider responsible for processing.
- Data protection impact assessment, and ODPC registration where needed.
- Digital Health Agency notification and certification review.
- PPB classification decision for the software.
- KMPDC position on telemedicine or reporting service registration.
- Written legal opinion on cross-border issues.

## Out of scope for Phase 1

Autonomous reporting, paediatric use, CT, MRI, ultrasound, EEG, triage alerts in live care, patient-facing output and billing.
