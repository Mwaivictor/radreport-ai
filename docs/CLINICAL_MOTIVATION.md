# Clinical Motivation

> **Privacy note.** This account is generalised on purpose. It leaves out identifying details such as the patient's age, the facility, the dates and the amounts. It is a description of a pattern, not a case report. Any publication of an individual case would first need consent, privacy review and compliance with publication ethics. The full account stays with the project lead and is not stored in either repository.

## The experience behind the project

During clinical training, the project lead saw a pattern that exposed a gap in the diagnostic pathway.

A child with a neurological condition that had not been fully investigated was referred for further evaluation, including possible neuroimaging. The family was under significant financial strain. They spent days raising what they needed for health insurance arrangements. They then met a further, relatively small charge linked to obtaining an imaging report, and could not raise it at that time. They asked for discharge so they could go home and try to find the money.

The image, the equipment and the clinical team were not the failing part here. The barrier arose around getting an interpretation that could inform the next decision.

## Why that matters for the design

A patient can reach a facility and still be stopped by barriers to interpretation. These can involve availability, affordability, timeliness or quality. That moves the focus from image acquisition to the steps after it.

## Connected problems seen in practice

**Delays.** Reports can take considerable time, decisions wait, referrals stall, and external review adds further waiting.

**Quality and consistency.** People make errors. Reports may omit findings or vary in structure and terminology. Clinicians sometimes request a second opinion when a report does not fit the patient.

**Resources.** Radiologists carry heavy workloads, specialist coverage may be limited, smaller facilities may rely on external reporting, and reporting costs can add to financial barriers.

**Workflow.** Images, reports and clinical data may sit in separate systems. Earlier reports can be hard to find, and data is re-entered by hand.

These are observations from practice. They are hypotheses to test, not measurements. [Research study 1](RESEARCH_ROADMAP.md) exists to measure them.

## What this experience does not establish

Being honest about these limits is part of taking the experience seriously.

1. **The first product would not have helped this child.** The motivating need was neuroimaging. The first module is adult chest X-ray, because that is where public data, open models and evaluation methods exist. Brain CT and MRI come later, and paediatric validation later still.
2. **AI does not automatically lower a fee.** A report fee is set by a facility, a provider or a payer. A faster draft changes the provider's cost only if the workflow really changes. It changes what a patient pays only if someone decides to pass that on. An authorised professional still has to sign.
3. **The reason for the fee is not yet known.** Whether a report fee of this kind reflects reader time, contract terms, facility policy or a tariff gap needs investigation. This project found no published SHA tariff for reporting. It found reported imaging tariffs only. See [Problem statement](PROBLEM_STATEMENT.md).
4. **One experience does not measure prevalence.** It shows that the barrier can happen, not how often.

## What the experience does ask of the project

- Measure the reporting pathway in Kenyan facilities, including who pays what and when. That study needs no AI, and it could change what the project builds.
- Treat "access to a report" as a separate outcome from "accuracy of a model".
- Include affordability as a research question, with a clear line between direct savings and theoretical efficiency.
- Keep paediatrics on the roadmap, because children are where this began. Do not deploy adult models on children in the meantime.
