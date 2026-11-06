# Privacy and Regulatory Position

> **Not legal advice.** Written by a non-lawyer from the sources below on 2026-11-06. Kenyan digital health law is changing and under litigation. A Kenyan advocate must review this before any step involving patients or patient data.

## Bottom line

1. **Public-data research can proceed.** Using public, de-identified datasets under their terms does not itself touch these Kenyan rules.
2. **Kenyan patient data must not leave Kenya** under this project's default, even pseudonymised, until a written legal opinion says otherwise. Digital Health Act s.47 reads as a very narrow permission.
3. **A live service is a regulated activity on several fronts at once:** data protection, digital health certification, medical device software, and medical practice registration.
4. **The *Rology* judgment is a warning.** A Kenyan High Court suspended a teleradiology company, described as AI-assisted, until it complies with these same regimes.

## The law that applies

### Data Protection Act, Cap. 411C [L1] (Verified, full text)

| Section | Effect for this project |
|---|---|
| s.2 | Health status is **sensitive personal data**. Anonymisation means the person is **no longer identifiable** |
| s.18 | Controllers and processors must register, subject to thresholds |
| s.25 | Principles: lawful, fair, transparent, limited purpose and so on |
| s.31 | DPIA before high-risk processing. It would be required here in practice |
| s.33 | Child data needs parent or guardian consent, and must protect the child's best interests |
| s.35 | Right not to be subject to solely automated decisions with significant effect. Human review must be real |
| s.46 | Health data may only be processed by or under the responsibility of a health-care provider, or a person under a duty of professional secrecy |
| s.48 | Conditions for transfer abroad: proof of safeguards, or a listed necessity |
| s.49(1) | **Sensitive data may be processed outside Kenya only with the data subject's consent and confirmation of safeguards** |
| s.49(3) | Commissioner may prohibit, suspend or condition a transfer |
| s.50 | Cabinet Secretary may require certain processing to be in Kenya |
| s.51(1) | Exemptions do not remove duties of lawful processing, minimisation, data quality and security |
| s.53 | Further processing for research is compatible if safeguards apply and results are not published in identifiable form |

### Digital Health Act, No. 15 of 2023 [L2] (Verified, full text)

| Section | Effect |
|---|---|
| s.3(h) | An object of the Act is safe transfer of health data within and outside Kenya |
| s.4 | "Health data is a strategic national asset" |
| s.22 | The Digital Health Agency is custodian of all health data in Kenya |
| s.41 | E-health services may only be provided by licensed providers or facilities |
| s.43 | Minors need consent of parent or guardian. Sharing images on e-health platforms must follow standards |
| **s.46(2)** | A controller transferring **health images** of a Kenyan citizen abroad must ensure confidentiality. For health research, it must report to the Director-General for Health, not share without notifying the Cabinet Secretary, and seek guidance on storage, processing and destruction |
| **s.47** | **"Personal health information may only be shared to any person outside Kenya for the purposes of health tourism."** |
| s.61 | The Data Protection Act still applies |

**The problem.** Read literally, s.47 forbids sending personal health information abroad except for health tourism. Yet s.3(h) contemplates transfers, and s.46(2) describes research transfers. The heading of s.46 is about health tourism guidelines, so its research proviso might not be a general permission. How these fit together is a question for an advocate. **This project assumes the stricter reading.**

### Digital Health Regulations 2025 [L3, L4]

Legal Notice 76 of 2025 (Verified, partial reading):

- Controllers and processors notify the Agency in writing on ODPC registration (r.4).
- Security requirements include encryption at rest and in transit.
- Research requests for System data need an ethics approval and a NACOSTI licence (r.17).
- The Agency tracks transfers of health images abroad (r.18(6)).
- The Agency **certifies digital health solutions**, including e-health and telemedicine platforms (rr.36–38), with application fees.
- Data use fees include KES 30,000 for an independent researcher, KES 5,000 for a master's student, and 1% of total research budget for a research institution (Second Schedule).
- Disclosing personal health data for market research is an offence (r.24).

Legal Notice 77 of 2025 was **not read**, and it was cited in the *Rology* orders.

**Litigation.** Secondary sources report that the High Court ruled against parts of this legislation, and the Court of Appeal suspended that ruling. Confirm the current position.

### ODPC cross-border guidance [L5] (Secondary only)

Law-firm summaries say that ODPC guidance, with its own standard clauses, treats storing personal data on servers abroad as a cross-border transfer, and that sensitive-data consent should appear in contracts and transfer records. Sources disagree on the publication date. The document could not be opened. **Obtain and read it.**

### PPB medical device software guideline [L6] (Secondary only)

HPT/PER/GUD/099 Rev. 0. Reported as issued February 2026 and published April 2026, though some press called it a draft. **Confirm its status.** Reported content:

- Covers SaMD, SiMD and AI-enabled devices, on any platform.
- IMDRF-style matrix: state of condition against significance of the software's function.
- Higher categories need verification, validation, risk files, clinical evidence and post-market surveillance.
- Good Machine Learning Practice principles.
- Annex I lists software below the threshold.

**Provisional classification:** software that informs a radiologist's diagnosis on chest disease, including critical conditions, is unlikely to fall below the threshold. Treat it as medical device software until the PPB says otherwise. Whether the guideline exempts research is **not known**. Ethics approval does not settle device status, and the study may need separate PPB input. Note NACOSTI requires PPB approval for clinical trials.

### The Rology case [L7] (Secondary; judgment not read)

Reported as decided 11 June 2026 by Justice Mande. Petition by officials of the Kenya Association of Radiologists.

| Point | Reported |
|---|---|
| Company | Kenyan affiliate of an Egyptian-founded teleradiology platform; described as AI-assisted. **The company denied that AI generates diagnoses** |
| Orders | Operations suspended until registered and compliant with the medical practice, data protection and digital health laws; MoH and KMPDC to cancel approvals; costs against KMPDC and the company |
| Reported reasoning | Registration is not mere bureaucracy; platform handling of portable health records cannot sit outside the framework; ODPC registration alone did not end the matter; disclaimers threatened consumer rights under Article 46. Outlets differ on how far the court ruled on data transfer |
| Status | Company applied for a stay. **Outcome not found** |

**Lessons for this project.**

1. ODPC registration is not enough. A claim that "a Kenyan radiologist reviews it" did not protect the company.
2. KMPDC registration may apply to a reporting service, and regulators can be held to account.
3. Who generates and validates a report must be transparent to patients and clinicians.
4. Liability disclaimers are a risk, not a protection.
5. Radiologists are organised and will litigate. Involve them first.
6. **Obtain and read the judgment before any design freeze.**

### Research approvals

Ethics approval from a NACOSTI-accredited committee, then a NACOSTI licence [L8]. A foreign committee is not a substitute. The 2004 biomedical guidelines were cited. Confirm fees directly.

### AI legislation

The Artificial Intelligence Bill 2026 was reported rejected at Senate committee stage in October 2026 [L17]. Monitor.

### International

| Item | Position | Status |
|---|---|---|
| WHO [L9, L10, L11] | Six principles for AI in health; guidance on large multi-modal models; regulatory considerations | Secondary |
| FDA [L12] | CDS guidance revised January 2026. Software analysing medical images stays under device oversight | Secondary |
| EU MDR and AI Act [L16] | Provisional deal moves AI Act dates: Annex III to 2 December 2027, Annex I products to 2 August 2028. Final adoption not confirmed | Secondary |
| EU GDPR | Likely applies to some processing on EU-hosted servers | Assumption |

## Who may sign a report

**Unresolved.** Sources did not settle whether clinical officers can issue formal radiology reports. Default: a consultant radiologist only. Obtain written positions from KMPDC, the Clinical Officers Council and the institution.

## Data location rules

| Data | Laptop | EU VPS | Cloud GPU | Kenyan facility machine |
|---|---|---|---|---|
| Synthetic | Yes | Yes | Yes | Yes |
| Open public data | Yes | Yes, within disk limits | Yes | Yes |
| PhysioNet credentialed | Encrypted, credentialed user only | Avoid | Contracted provider only, encrypted | Check licence |
| Kenyan patient data | **No** | **No** | **No** | **Only under approved protocol** |

## Compliance roadmap

| Step | Owner | Timing |
|---|---|---|
| Read judgment, LN 77, ODPC note, PPB guideline | Project lead | Week 1 |
| Kenyan advocate's opinion | Project lead | Before partner talks |
| Radiologist co-investigator | Project lead | Before partner talks |
| Ethics, NACOSTI, institutional approval | Principal investigator | Before local data |
| DPIA | Controller | Before local data |
| PPB consultation | Project lead | Before reader study |
| Digital Health Agency certification | Later | Before service |

## Unresolved decisions

1. Does anonymised image data fall outside s.47?
2. Is a reader study on retrospective images a clinical investigation of a device?
3. Does the sponsor need KMPDC registration, and from what stage?
4. Is a separate legal entity needed? An individual cannot easily hold the required registrations.
5. Which entity is controller, and which processor?
