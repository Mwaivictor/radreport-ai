# Dataset Catalog

Checked 2026-11-06. Blank facts are written as "not stated" and never estimated. **Terms change, so re-read each licence before use and record the date.** Nothing here is legal advice.

## How to read this

- A dataset being "public" does not mean you may use it for anything. Three questions are separate: can I download it, can I do research with it, can I use what I build from it in a product?
- "Commercial" below means use in a product or service, including models trained on the data. For credentialed data this is a legal question, not just a technical one.

## Decision

| Role | Dataset | Why |
|---|---|---|
| Open data, usable straight away | **RSNA Pneumonia** and **NIH ChestX-ray14** subset | Open access. Enough for pipeline work |
| Primary research set | **MIMIC-CXR-JPG + MIMIC-CXR reports** | Images, reports, patient IDs and rule-based labels. Credentialing takes time |
| External test, international | **VinDr-CXR** | Radiologist labels, boxes, a non-Western population |
| External test, African | **Naija-CXR** | The only African CXR-with-report dataset found. Terms must be clarified first |
| Paediatric exploration only | **VinDr-PCXR** | Shows how adult models fail on children |

## Chest X-ray: comparison

| Dataset | Images | Patients | Reports | Labels | Geography | Access | Size | Commercial use |
|---|---|---|---|---|---|---|---|---|
| MIMIC-CXR v2.1.0 [D1] | 377,110 | Not stated on page | Yes, free text | None in base set | USA, Boston | Credentialed, CITI, DUA | ~4.6 TB (secondary) | Licence limits use to "scientific research". Assume no product use without advice |
| MIMIC-CXR-JPG v2.1.0 [D2] | 377,110 (v2.0.0 text) | Not stated | No, use MIMIC-CXR | CheXpert and NegBio, rule-based | USA | Credentialed, CITI, DUA | ~558 GB (secondary) | As above |
| CheXpert [D3] | 224,316 | 65,240 | Yes, per AIMI page; see CheXpert Plus [D4] | 14 observations, rule-based, with uncertainty | USA, Stanford | Stanford AIMI registration | ~440 GB (secondary) | **Unverified**, terms not readable. AIMI has a separate commercial page |
| VinDr-CXR v1.0.0 [D5] | 18,000 (15,000 train, 3,000 test) | Not stated | No | Radiologists: 3 per train image, 5-reader consensus for test; 22 local, 6 global labels | Vietnam | Credentialed, CITI, DUA | Not stated | As MIMIC: research |
| VinDr-PCXR v1.0.0 [D6] | 9,125 PA (7,728 train, 1,397 test) | Not stated | No | 36 local, 15 global; radiologist-annotated | Vietnam, under 10 years | Registered user, DUA | Not stated | PhysioNet Restricted licence; read terms |
| NIH ChestX-ray14 [D7] | 112,120 | 30,805 | No | 14 labels from report NLP | USA | Open | Not verified | Sources conflict. NIH page not read |
| PadChest [D8] | Over 160,000 | About 67,000 | Yes, Spanish | 174 findings, 19 diagnoses, 104 locations; 27% manual, rest automated | Spain | Form request, research agreement | 1.02 TB | Read agreement. Terms not viewed |
| RSNA Pneumonia [D9] | 30,000 frontal; 26,684 train and 3,000 test in stage 2 (secondary) | Derived from NIH | No | Boxes for opacity that may represent pneumonia, radiologists | USA (NIH source) | Open, RSNA or Kaggle | Not verified | RSNA page permits commercial and non-commercial use with attribution (secondary). Attribution terms not read |
| Naija-CXR v1.1 [D10] | **Not stated** | Not stated | Yes, free text | Radiologist annotations, schema not described | Nigeria, Dutse | Open, Zenodo | 389.3 MB | **Conflict:** CC BY 4.0 licence but page says "exclusively for non-commercial" use. Treat as non-commercial |

## Dataset notes: chest X-ray

**MIMIC-CXR.** *Can establish:* performance on a large US hospital population, and the link between images and reports. *Cannot establish:* outpatient or African performance. Labels come from report text, not independent image review, so a model learns what radiologists tended to write. Page figures differ slightly between versions: 227,835 studies on MIMIC-CXR, and 227,827 labelled studies on MIMIC-CXR-JPG.

**CheXpert.** Introduced uncertainty labels, useful for understanding that labels are not ground truth. Current terms could not be read from the AIMI page.

**VinDr-CXR.** The strongest open test design here: independent readers on images rather than parsed reports. The population is Vietnamese. It is not a proxy for African patients.

**NIH ChestX-ray14.** Labels come from NLP on reports, and are known to be noisy. Use for pipeline development, not for strong accuracy claims.

**RSNA Pneumonia.** Labels describe **opacity that may represent pneumonia**, not confirmed pneumonia. It is drawn from NIH data, so it is not independent of any model trained on NIH images.

**Naija-CXR.** The most important find, and the least characterised. The image count is not stated on the page. At 389 MB it is likely small. The page refers to "Nigerian institutions", but the listed institutions and the file name point to a single teaching hospital in Dutse. Contact the authors to clarify terms before any product-related use. This dataset was not on the original project list.

**VinDr-PCXR.** The page contradicts itself: it describes a paediatric dataset and also says the data contains only adult CXRs. Treat that sentence as an error to confirm. Note it is for children under 10 only.

## CT

| Dataset | Content | Annotations | Reports | Format | Size | Licence | Commercial |
|---|---|---|---|---|---|---|---|
| CT-RATE [D11] | 25,692 non-contrast chest CT, 50,188 with reconstructions; 21,304 patients | Multi-abnormality labels | Yes | NIfTI | 21.3 TB | CC BY-NC-SA 4.0, gated | Needs prior permission. No redistribution |
| RSNA ICH [D12] | 874,035 images in 25,312 exams | 60 volunteer annotators | No | DICOM | Not verified | Non-commercial (secondary) | Reported non-commercial |
| CQ500 [D13] | 491 scans (from memory, not confirmed) | Radiologist reads | No | DICOM | Unverified | **Unverified**, site unreachable | Unverified |
| MosMedData [D14] | 1,110 chest CT, 50 with masks; Moscow, 2020 | COVID severity | No | NIfTI | Not verified | CC BY-NC-ND, version conflicts between 3.0 and 4.0 | Non-commercial |
| AMOS v2 [D15] | 500 CT, 100 MRI | 15 abdominal organs | No | NIfTI | 24.2 GB | CC BY 4.0 | Permitted, with attribution |
| TotalSegmentator v2.0.1 [D16] | 1,228 CT | 117 structures | No | NIfTI | 23.6 GB | CC BY 4.0 | Permitted, with attribution |

## MRI

| Dataset | Content | Annotations | Format | Size | Licence | Notes |
|---|---|---|---|---|---|---|
| IXI | Nearly 600 healthy subjects; T1, T2, PD, MRA, DWI; 3 London sites | None | NIfTI | Not stated | CC BY-SA 3.0 | Derivative sharing terms apply |
| BraTS (adult) | Challenge data | Tumour subregions | NIfTI | Varies | Check per-year terms | Not reviewed in detail |
| BraTS-Africa [D18] | 146 cases, 1.5T, Nigerian centres | Expert tumour subregions | NIfTI | 3.7 GB | CC BY 4.0 for processed data. Unprocessed data under NIH controlled access | Some downloads paused pending a new access method |
| OASIS | Neuroimaging cohorts | Varies | Varies | Not checked | **Unverified**, site unreachable | Has a data use process |
| UCSF-PDGM [D17] | 495 patients, adult glioma, 3T | Tumour segmentation | NIfTI | ~142 GB | CC BY 4.0 | Single centre, single vendor |

## Licence quick reference

| You want to… | Usable now | Needs care | Do not assume |
|---|---|---|---|
| Learn and run pipelines | RSNA, NIH, Naija-CXR | | |
| Publish a paper | All, under their terms | PhysioNet: code must be shared openly | |
| Train a model for a product | AMOS, TotalSegmentator, UCSF-PDGM, BraTS-Africa processed (other modalities) | RSNA Pneumonia, once attribution terms are read | MIMIC, VinDr, CheXpert, PadChest, Naija-CXR, CT-RATE, RSNA ICH, MosMed |

**No large, reports-included CXR dataset was found with clearly product-compatible terms.** This is a strategic constraint. See [Model research](MODEL_RESEARCH.md).

## What every public dataset cannot tell you

None establish performance in Kenyan facilities, on Kenyan equipment, or with the local case mix, including TB and HIV-related disease. Only an ethically approved local study can do that.
