# Storage Strategy

## Principle

Keep only what you are using. Most public data lives elsewhere and is pulled selectively.

## Sizes against capacity

| Dataset | Size | Fits 75 GB disk? |
|---|---|---|
| Naija-CXR | 389.3 MB | Yes |
| BraTS-Africa | 3.7 GB | Yes |
| TotalSegmentator | 23.6 GB | Barely, not recommended |
| AMOS | 24.2 GB | Barely, not recommended |
| UCSF-PDGM | ~142 GB | No |
| CheXpert | ~440 GB (secondary) | No |
| MIMIC-CXR-JPG | ~558 GB (secondary) | No |
| PadChest | 1.02 TB | No |
| MIMIC-CXR DICOM | ~4.6 TB (secondary) | No |
| CT-RATE | 21.3 TB | No |

Actual free space on the VPS is unknown until an audit runs, and the disk is shared with other services.

## Tiers

| Tier | Holds | Where |
|---|---|---|
| Hot | Current derived subset, manifests | Local SSD or GPU node storage |
| Warm | Selected raw subset | Encrypted object storage |
| Metadata | Registry, experiments, documents | Git and Postgres |
| Cold | Result archives | Object storage |
| Never here | Kenyan patient data | Stays in Kenya, on an approved system |

Backblaze B2 is listed at $6.95 per TB per 30 days, with the first 10 GB free and egress free up to three times average monthly storage (secondary, 2026). Check the current rate.

## Subset approach

For the first baseline, aim for tens of thousands of downsampled images, not the full set.

- Frontal views only.
- Long side around 512 px, for storage; originals remain retrievable.
- Stored as compressed archive.
- Rough arithmetic: 50,000 images × ~100 KB each ≈ 5 GB. This is an assumption to confirm once real files are sampled.

## Rules

1. **Encrypt credentialed data at rest**, with keys held by the credentialed person.
2. **No restricted data in Git**, including small samples and thumbnails.
3. Use `.gitignore` for `data/`, plus a pre-commit check.
4. Do not let the VPS disk go above 80%. Existing services depend on it.
5. Delete working copies when done, and log the deletion.
6. Follow dataset rules on where data may be stored. Confirm before putting credentialed data in any third-party bucket.

## Directory layout

```text
data/                     (gitignored)
  raw/<dataset>/<version>/      read-only
  derived/<dataset>/<pipeline>/
  results/<experiment_id>/
registry/                 (tracked)
  datasets.yaml
  terms/                  dated copies of terms where redistribution allows
```

## Monitoring

Weekly: disk use, object-store bill, and files older than 30 days in working areas.
