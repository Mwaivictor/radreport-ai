# Medical Imaging Fundamentals

Written to connect engineering ideas to what happens at the viewing box. For file-level details see the [DICOM guide](DICOM_GUIDE.md).

## An image is not an examination

A clinician never reports "an image". They report an **examination**: the views taken, the technique, the indication, the comparison, and whether the study is adequate.

| Level | Plain meaning | Chest X-ray | CT brain |
|---|---|---|---|
| Patient | The person | One person | One person |
| Study | One examination | PA and lateral done today | Head CT today |
| Series | One acquisition set | One view or set | Non-contrast axial, bone reconstruction |
| Instance | One image | One radiograph | One slice |

This hierarchy matters for machine learning. Splitting data by image leaks one patient into both training and test sets. It is like setting an exam and marking a student on the same questions they revised from.

## How each modality makes its signal

**X-ray.** Projection. A 3D chest is collapsed to 2D, so structures overlap. Pixel values reflect attenuation along a path, and do not have a universal unit. Sensitive to exposure, rotation, inspiration and projection.

**CT.** Reconstructed cross-sections. Pixels are Hounsfield units, a calibrated physical scale in which water is 0 and air is about −1000. Slices form a volume with real-world spacing.

**MRI.** Signal depends on tissue properties and sequence. There is no universal unit: a value in one scanner's T1 image cannot be compared directly with another's.

| Sequence | Useful for |
|---|---|
| T1 | Anatomy; post-contrast enhancement |
| T2 | Fluid, oedema |
| FLAIR | T2 with CSF suppressed; periventricular lesions |
| DWI | Restricted diffusion, such as acute infarct |
| ADC | Calculated map that confirms true restriction |
| T1 post-contrast | Blood-brain barrier breakdown, enhancing tumour |

## Key technical ideas

**Orientation.** X-ray: PA vs AP. Radiological display shows the patient's left on the viewer's right. Getting laterality wrong in a report can lead to a wrong-side procedure, so the system checks it explicitly.

**Pixel spacing.** The physical size of a pixel. Without it, measurements are meaningless. A system must never invent a measurement from an image with unknown spacing.

**Pixel representation and bit depth.** Medical images often store 12–16 bits per pixel. A standard PNG or JPEG usually has 8. Converting loses information that may matter for subtle findings.

**Windowing.** Selecting which values to show. A CT brain viewed in a stroke, subdural and bone window shows different things. The value range is far wider than a screen or the eye can use. For X-ray, DICOM tags may carry a window or a lookup table.

**Photometric interpretation.** Tells you whether high values are bright (`MONOCHROME2`) or dark (`MONOCHROME1`). Getting this wrong inverts the image. A model that has never seen inverted images may produce confident nonsense.

**Slice thickness.** Thick CT slices average tissue together and can hide small lesions.

## Common file formats

| Format | Use | Keeps metadata? | Clinical? |
|---|---|---|---|
| DICOM | Clinical standard | Fully | Yes |
| NIfTI | Neuroimaging research volumes | Geometry only | No |
| NRRD | Research volumes | Geometry | No |
| PNG | Lossless 2D; usually 8 or 16 bit | No | No |
| JPEG | Lossy 2D; 8 bit | No | No |

## Clinical pitfalls for AI

- **Portable AP films** are often the sickest patients, and magnify the heart. A model may learn "portable = sick".
- **Lines and tubes** can act as a shortcut for disease.
- **Hospital markers** may let a model recognise the site [B2].
- **Different exposure** in older analogue-digitised systems changes appearance.
- **Rotation and poor inspiration** mimic disease.
- **Local case mix.** TB, HIV-related disease and rheumatic heart disease may be far more common in Kenya than in US training data.
- **Children** differ in anatomy: the thymus, heart proportions and disease patterns are different.

## Tools

| Tool | Use | Licence (GitHub metadata) |
|---|---|---|
| pydicom | Read and write DICOM | Custom, read before use |
| SimpleITK | Volumes, resampling, geometry | Apache-2.0 |
| NiBabel | NIfTI | Custom, read before use |
| MONAI | Medical imaging deep learning | Apache-2.0 |
| OHIF | Web DICOM viewer | MIT |

## Check your understanding

1. Why can a very high AUC on one image split be misleading?
2. Why does cardiomegaly on an AP film need caution?
3. What should the system do if pixel spacing is absent and a measurement is requested? (Answer: refuse, and say why.)
