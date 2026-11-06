> Published essay that sets out the motivation for this project.
> Medium: https://medium.com/@mwaivictorbrian68/the-unfinished-diagnosis-2784a7c71fa3
> LinkedIn: https://www.linkedin.com/pulse/unfinished-diagnosis-scan-mwai-victor-brian-j6o4f/
> A peer-review manuscript version is in preparation and is not included here.

# The Unfinished Diagnosis

### A scan is not a diagnosis. In much of Africa, the hardest part of medical imaging starts after the image is taken.

*By Mwai Victor | Clinician, data scientist, digital health researcher*

---

It is mid-afternoon on a children's ward. The X-ray was done this morning. The images exist. Somewhere on a workstation, or on a film in an envelope, the answer to your clinical question is sitting there.

You just can't read it yet.

The report hasn't come. Maybe the radiologist covers three hospitals. Maybe the request is in a pile. Maybe the report is ready but nobody has walked it to the ward. Or maybe, as I once saw with a family already stretched to their limit, there is one more payment standing between the image and the interpretation, and they cannot make it.

The scan was done. The diagnosis was not.

That moment stayed with me, and it changed the question I ask about medical imaging. We usually ask: **can the patient get a scan?** The better question is: **can the patient get an answer?**

This essay is about the space between those two questions.

---

## Contents

1. The step we forget to count
2. Naming the problem: the diagnostic interpretation gap
3. What the evidence says about Kenya and Africa
4. The patient pays twice: in money and in waiting
5. Why "just buy more machines" is not enough
6. Where AI fits, and where it does not
7. Kenya just showed us why governance is not optional
8. What we should be measuring
9. Why I am building radreport-ai
10. References

---

## 1. The step we forget to count

A diagnostic image is useful only if a chain holds together:

1. Someone decides imaging is needed.
2. The right examination is requested.
3. The examination is performed.
4. The images are interpreted.
5. The findings are written into a clear report.
6. The report reaches the clinician who asked.
7. The clinician integrates it into a decision.
8. The patient is managed accordingly.

Health policy talks a lot about steps 1 to 3: equipment, scanners, how far a patient travels. Steps 4 to 6 are quieter. They happen in reading rooms, inboxes and corridors. But if they fail, everything before them was money, time and radiation spent for nothing.

**A medical image is not yet a diagnosis.**

## 2. Naming the problem: the diagnostic interpretation gap

I call this the **diagnostic interpretation gap**: the distance between getting an imaging examination and getting a timely, affordable, reliable interpretation that can actually change care.

To be clear, this is a framing I am proposing, not an established metric. Part of the point is that nobody is measuring it properly yet, at least not in the places I work.

## 3. What the evidence says about Kenya and Africa

**There are not many people to read the images.** A 2022 review by African radiology leaders compiled workforce figures across the continent. Kenya was listed with about 250 radiologists for roughly 55 million people. Several countries reported fewer than ten radiologists in total (Kawooya et al., 2022). The numbers are approximate, but the scale is not in doubt.

**The machines and the readers are not in the same places.** An analysis of Kenya's national register of radiological equipment found 24.5 general X-ray units per million people overall, but only about 9.6 per million in the public sector, under the 20 per million benchmark the authors cite. Nairobi was the only region with every modality, and CT availability varied almost thirty-fold between regions (Gathuru et al., 2021).

**We bought equipment faster than we trained interpreters.** Kenya's Managed Equipment Services programme put imaging equipment into 98 public hospitals across all 47 counties. A 2025 review of the programme reports that only 25 radiologists were available across a quarter of the targeted hospitals, and remote image transmission was used so X-rays from hospitals without radiologists could be reported elsewhere (Njagi et al., 2025).

**We don't actually know how long reports take.** I could not find a single peer-reviewed multicentre study of imaging report turnaround times in Kenyan public hospitals. That silence is a finding. For comparison, a study of routine blood tests at a Kenyan referral hospital found an average of about 21.5 hours from order to result, with printing and dispatch the biggest delay, and 13.5% of results never reached the clinical team at all (Mwogi et al., 2020). Imaging reports often travel through the same paper and people. Do they get lost the same way? We don't know.

**Reading images is hard, tiring work.** In one US centre, the number of CT and MRI images per radiologist per minute rose from 2.9 in 1999 to 16.1 in 2010 (McDonald et al., 2015). Another study found that radiologists detected fractures less accurately at the end of a day of reading than at the start (Krupinski et al., 2010). Those are high-income settings. In places with far fewer readers, the pressure is unlikely to be smaller.

## 4. The patient pays twice: in money and in waiting

A scan is rarely just the scan fee. There is transport. Time off work. A second trip to collect results. Sometimes a review fee, a specialist visit, a repeat examination.

Reporting is not always charged separately, and I want to be careful here: I found no published data on how often Kenyan patients pay specifically for interpretation. What we do know is the wider picture. Using national survey data from 2018, Salari and colleagues found that about 1 in 10 Kenyan households spent more than 10% of their total spending on out-of-pocket health payments, with outpatient care the main driver and the poorest and rural households hit hardest (Salari et al., 2019).

Then there is the waiting. A pending report means a pending decision: a delayed admission, a postponed discharge, a referral sent with images but no interpretation, a family coming back again. These consequences make clinical sense, but outcome data in African settings are thin. So I am stating them as things we need to measure, not things we have proven.

## 5. Why "just buy more machines" is not enough

There are good tools already. Each solves part of the problem.

- **Training more radiologists** is the foundation. It also takes years, and graduates concentrate in cities and the private sector.
- **Teleradiology** moves expertise to where images are. A review of African teleradiology found real benefits, but most programmes were feasibility projects held back by infrastructure, support and politics (Ewing & Holmes, 2022).
- **Structured reporting** makes reports more complete and consistent. Clinicians and radiologists in large surveys preferred itemised reports for complex studies (Bosmans et al., 2011).
- **Quality assurance and peer review** accept that discrepancy is part of radiology everywhere and build systems to learn from it (Brady, 2017).
- **PACS and RIS** replace film with digital images that can be tracked and shared. Kericho County's move from film to digital imaging is one Kenyan example.

None of these is optional. None is enough alone.

## 6. Where AI fits, and where it does not

I build AI tools, so let me be the one to say it: **AI is not the answer to a workforce and financing problem.** It can be part of the response if we are precise about what it does.

**Where the evidence is strongest: narrow detection tasks.** In Kenya's 2016 national TB prevalence survey, computer-aided detection software read more than 61,000 adult chest X-rays and reached an AUC of 96.7% for confirmed TB, with higher sensitivity than the clinical officers who also read the films (Mungai et al., 2022). WHO now allows this kind of software to replace human readers for TB screening and triage in people aged 15 and over (WHO, 2021). That is screening, though, not a full radiology report.

**Where the evidence is weak: writing the report.** Generating a full report from an image is much harder. A Harvard-led study found that the automated scores commonly used to grade AI-written chest X-ray reports did not match radiologists' judgement and missed clinical errors (Yu et al., 2023). A 2025 Nature Medicine study found clinically significant errors in both AI-written and human-written reports, and pointed toward clinicians and AI working together rather than AI working alone (Tanno et al., 2025).

**And the failure modes are real:**

- Only 6% of 516 published imaging AI studies reviewed in one analysis tested their model on outside data (Kim et al., 2019).
- A pneumonia model trained in one hospital system did worse in others (Zech et al., 2018).
- Chest X-ray classifiers under-diagnosed under-served patient groups more often (Seyyed-Kalantari et al., 2021).
- When radiologists were shown wrong AI suggestions, their accuracy dropped sharply, including experienced readers (Dratsch et al., 2023).

My position is simple. **AI-assisted, not AI-autonomous.** A licensed professional signs the report and owns it. The tool is validated on local images first. Its performance is monitored after deployment. Patient data stays under the law.

## 7. Kenya just showed us why governance is not optional

In June 2026, Kenya's High Court suspended the local operations of a teleradiology and AI-assisted reporting company pending compliance with data protection and digital health law. The petition was brought by officials of the Kenya Association of Radiologists, alleging images were sent abroad without consent and responsibility for report accuracy was unclear. The company disputed this (The Standard, 2026). The Kenya Association of Radiologists and the Kenya Medical Association then called on facilities to make sure every report is issued by a radiologist licensed in Kenya with clear accountability, while saying they support AI that assists professionals rather than bypassing them (People Daily, 2026).

Whatever happens next in that case, the lesson is clear. **You cannot close the interpretation gap with technology that sits outside professional regulation and data protection.** Accountability is part of the product.

## 8. What we should be measuring

If the interpretation gap is real, we should be able to count it. Here is what I would want every imaging department to know about itself:

- **Reach:** what share of examinations ever gets a verified report?
- **Timeliness:** how long from image to report *in the clinician's hands*, not just "report signed"?
- **Closed loop:** what share of reports are actually opened or acknowledged by the person who asked?
- **Affordability:** what does a patient pay, in total, for a finished diagnosis?
- **Quality:** how complete are reports, and how often are they amended or contradicted on review?
- **Equity:** do these numbers differ by county, facility level and patient income?

Two of these, reach and closed-loop delivery, are simple and almost never reported. Start there.

## 9. Why I am building radreport-ai

This essay is the motivation behind **radreport-ai** (this repository), an early-stage open-source research project on clinically supervised, AI-assisted imaging reporting, starting with chest X-rays.

I want to be honest about what it is and what it is not. It is not a product that replaces radiologists. It is a research effort built around the principles above: assist the qualified reporter, structure the report, flag what might be urgent, check for missing pieces, measure turnaround, validate locally, keep the human accountable. If you are a radiologist, clinician, researcher or engineer working on any part of this problem, especially in East Africa, I would like to hear from you.

The value of imaging is realised when an interpretation is reliable, timely, delivered and acted on. Until then, the diagnosis is unfinished.

---

*Disclaimer: This essay reflects my views as a clinician and researcher, not those of any institution. The clinical scene is a composite reflection with no identifying details, and it is not evidence of how often such events occur. A fuller academic version is being prepared for peer review.*

---

## 10. References

1. Kawooya MG, Kisembo HN, Remedios D, et al. An Africa point of view on quality and safety in imaging. *Insights Imaging.* 2022;13:58. https://doi.org/10.1186/s13244-022-01203-w
2. Gathuru LM, Elias GDO, Pitcher RD. Analysis of registered radiological equipment in Kenya. *Pan Afr Med J.* 2021;40:205. https://doi.org/10.11604/pamj.2021.40.205.29570
3. Njagi E, Iloka K, Wawira S, Thiga L, Muraguri N. Learning from the Kenyan experiment: key takeaways for implementing managed equipment services in developing countries. *Front Health Serv.* 2025;5:1361261. https://doi.org/10.3389/frhs.2025.1361261
4. Mwogi T, Mercer T, Tran DN, et al. Therapeutic turnaround times for common laboratory tests in a tertiary hospital in Kenya. *PLoS One.* 2020;15(4):e0230858. https://doi.org/10.1371/journal.pone.0230858
5. McDonald RJ, Schwartz KM, Eckel LJ, et al. The effects of changes in utilization and technological advancements of cross-sectional imaging on radiologist workload. *Acad Radiol.* 2015;22(9):1191-8. https://doi.org/10.1016/j.acra.2015.05.007
6. Krupinski EA, Berbaum KS, Caldwell RT, Schartz KM, Kim J. Long radiology workdays reduce detection and accommodation accuracy. *J Am Coll Radiol.* 2010;7(9):698-704. https://doi.org/10.1016/j.jacr.2010.03.004
7. Salari P, Di Giorgio L, Ilinca S, Chuma J. The catastrophic and impoverishing effects of out-of-pocket healthcare payments in Kenya, 2018. *BMJ Glob Health.* 2019;4(6):e001809. https://doi.org/10.1136/bmjgh-2019-001809
8. Ewing B, Holmes D. Evaluation of current and former teleradiology systems in Africa: a review. *Ann Glob Health.* 2022;88(1):43. https://doi.org/10.5334/aogh.3711
9. Bosmans JML, Weyler JJ, De Schepper AM, Parizel PM. The radiology report as seen by radiologists and referring clinicians. *Radiology.* 2011;259(1):184-95. https://doi.org/10.1148/radiol.10101045
10. Brady AP. Error and discrepancy in radiology: inevitable or avoidable? *Insights Imaging.* 2017;8(1):171-82. https://doi.org/10.1007/s13244-016-0534-1
11. Mungai B, Ong'angò J, Ku CC, et al. Accuracy of computer-aided chest X-ray in community-based tuberculosis screening: lessons from the 2016 Kenya National Tuberculosis Prevalence Survey. *PLOS Glob Public Health.* 2022;2(11):e0001272. https://doi.org/10.1371/journal.pgph.0001272
12. World Health Organization. WHO consolidated guidelines on tuberculosis. Module 2: screening. 2021. https://www.who.int/publications/i/item/9789240022676
13. Yu F, Endo M, Krishnan R, et al. Evaluating progress in automatic chest X-ray radiology report generation. *Patterns.* 2023;4(9):100802. https://doi.org/10.1016/j.patter.2023.100802
14. Tanno R, Barrett DGT, Sellergren A, et al. Collaboration between clinicians and vision-language models in radiology report generation. *Nat Med.* 2025;31(2):599-608. https://doi.org/10.1038/s41591-024-03302-1
15. Kim DW, Jang HY, Kim KW, Shin Y, Park SH. Design characteristics of studies reporting the performance of AI algorithms for diagnostic analysis of medical images. *Korean J Radiol.* 2019;20(3):405-10. https://doi.org/10.3348/kjr.2019.0025
16. Zech JR, Badgeley MA, Liu M, et al. Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs. *PLoS Med.* 2018;15(11):e1002683. https://doi.org/10.1371/journal.pmed.1002683
17. Seyyed-Kalantari L, Zhang H, McDermott MBA, Chen IY, Ghassemi M. Underdiagnosis bias of AI algorithms applied to chest radiographs in under-served patient populations. *Nat Med.* 2021;27(12):2176-82. https://doi.org/10.1038/s41591-021-01595-0
18. Dratsch T, Chen X, Rezazade Mehrizi M, et al. Automation bias in mammography: the impact of AI BI-RADS suggestions on reader performance. *Radiology.* 2023;307(4):e222176. https://doi.org/10.1148/radiol.222176
19. Gitonga N. Court blocks Rology operations over health data compliance failures. *The Standard.* 12 June 2026. https://standardmedia.co.ke/crime-and-justice/article/2001550172/court-blocks-rology-operations-over-health-data-compliance-failures
20. People Daily. Medical associations demand compliance in radiology reporting services. 12 June 2026. https://peopledaily.digital/news/medical-associations-demand-compliance-in-radiology-reporting-services

