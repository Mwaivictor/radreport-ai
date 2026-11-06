# Clinical Safety

**Status: research prototype. Not clinically validated. Not for patient care.** A demonstration that runs says nothing about clinical safety.

## Human oversight policy

1. Only an authorised professional can issue a report.
2. The reviewer sees the original image.
3. AI output is labelled at every step.
4. "AI found nothing" is never reassurance.
5. AI failure never stops the usual reporting route.
6. No autonomous output to patients or treating clinicians.
7. Patients are told when AI is used, as the protocol and law require.
8. Changing a model needs re-evaluation. There is no learning in deployment.

## Clinical risk register

Likelihood and severity are provisional judgements: L/M/H. A clinician and a radiologist must review this.

| ID | Hazard | Harm | L | S | Control |
|---|---|---|---|---|---|
| R1 | Model misses a critical finding, and reviewer trusts draft | Delayed treatment | M | H | Reader-first review; `not_assessed` sections; no reassurance language |
| R2 | Fabricated finding in draft | Unnecessary tests or treatment | M | H | Template renders only from records |
| R3 | Wrong laterality | Wrong-side intervention | L | H | Laterality only from fields; QA rule |
| R4 | Draft used as final | Unreviewed diagnosis in care | M | H | Status watermark; no timed transition; permissions |
| R5 | Automation bias | Reader accepts AI error | H | H | Reader-first; training; monitor unchanged drafts [C7, C8] |
| R6 | Adult model used on a child | Wrong output | M | H | Age gate; reject unknown age |
| R7 | TB not flagged, because no TB output | Missed infectious disease | H | H | Explicit "TB not assessed by this model" statement; local priority |
| R8 | Poor performance on local equipment | Systematic error | H | H | Local validation before use |
| R9 | Subgroup underperformance | Inequity | M | H | Subgroup analysis [B1, B3] |
| R10 | Wrong-patient linkage | Wrong patient's report | L | H | Patient checks at every link |
| R11 | Poor image, confident output | False assurance | M | M | Quality flag; adequacy statement |
| R12 | Alert fatigue from QA | Warnings ignored | M | M | Few rules; track dismissals |
| R13 | Model drift | Falling performance | M | H | Ongoing audit |
| R14 | Deskilling | Weakened human backstop | M | M | Reader-first; audit; education |
| R15 | Staff believe clinician may sign | Unauthorised reports | M | H | Role permissions; policy |
| R16 | Privacy breach | Harm to patient, loss of trust | L | H | See privacy controls |
| R17 | Patient cost rises | Worse access | M | H | Access study; do not add a fee |
| R18 | Developer works unsupervised | Unsafe clinical choices | M | H | Named clinical safety lead, radiologist partner |

## Model limitations statement (to accompany any output)

- Trained on data mainly from outside Kenya.
- Not validated on Kenyan patients or on children.
- Limited set of findings. It cannot see what it was not trained for.
- Low resolution input may miss fine detail.
- Scores are not diagnoses.

## Bias assessment

Report performance by age band, sex, site, equipment and view, and by ancestry-related group only where data and ethics allow. Set a minimum subgroup size before reporting. Small groups need wide confidence intervals, not silence. Failure in a subgroup is reported.

## Incident management

| Stage | Action |
|---|---|
| Detect | Reader flag, QA signal, or audit |
| Contain | Pause the model version |
| Report | To PI, ethics committee, facility, and regulators as required. ODPC breach duties for data incidents |
| Investigate | Root cause, with no blame on staff |
| Correct | Fix and re-evaluate |
| Learn | Publish a summary where appropriate |

Set the reporting timelines in the protocol. ODPC breach deadlines should be confirmed.

## Drift and post-deployment monitoring

Monitored per version and site:

- Input distribution: exposure, equipment, age.
- Score distribution.
- Agreement with final reports.
- Reviewer edit rates.
- Rate of rejected drafts.
- Sampled independent re-reads of signed reports.

A change in these triggers review. It does not change the model automatically.

## Audit logging

Every view, edit, rejection, sign-off and export is logged immutably, with user, role, time and model version. See [Data dictionary](DATA_DICTIONARY.md).

## Governance

Roles to fill before local work:

| Role | Who |
|---|---|
| Principal investigator | To appoint |
| Clinical safety lead | To appoint |
| Radiologist lead | To appoint |
| Data protection lead | To appoint |
| Independent reviewer | To appoint |

The project lead is a clinician in training. That is valuable, but the project needs senior radiology and research supervision before it touches patients.

## Public communication rules

- Say "research prototype". Never "clinically validated".
- No identifiable cases, images or records in demonstrations.
- No individual patient story becomes a case report without consent and ethics review.
- Use "may" until it is measured.
