# Infrastructure and Costs

Prices are public list prices seen in secondary sources in 2026. They change often. Check them before you buy.

## What exists

| Resource | Advertised spec | Verified? |
|---|---|---|
| Laptop | 16 GB RAM, integrated graphics, no discrete GPU | As stated by owner |
| Small VPS | 4 vCPU, 8 GB RAM, 75 GB NVMe, EU region | **No. Audit not run** |

Assume the VPS has no GPU unless an audit shows one. It is shared with other services, which take priority.

## What each can do

| Task | Laptop | VPS | External GPU |
|---|---|---|---|
| Documents, Git | Yes | Yes | |
| Dataset metadata work | Yes | Yes | |
| Pretrained DenseNet inference | Yes, slow on large sets | Yes, small batches only, off-peak | Faster |
| Calibration, small heads | Yes | No | Optional |
| Fine-tuning | No | No | Yes |
| Vision-language inference, such as a 7B-parameter MAIRA-2 | Not practical | No | Yes |
| CT or MRI training | No | No | Yes |
| Hosting a small research demo | Local | After audit, in isolation | |

## GPU options

| Option | Reported price | Use | Caution |
|---|---|---|---|
| Kaggle notebooks | Free, around 30 h per week of quota, about 9 h per session; varies | Learning and open data | Data terms; session limits |
| RunPod Community RTX 4090 | About $0.34/h | Open data only | Third-party hosts. **No credentialed data** |
| RunPod Secure RTX 4090 | About $0.74–0.89/h | Fine-tuning | Confirm suitability for credentialed data |
| RunPod A100 | About $1.19–1.79/h, varying by source and tier | Larger models | |
| Major cloud | Check quotes | Credentialed data under contract | Costlier |

## Illustrative monthly cost

Arithmetic from the prices above, with assumed usage. Not a quote.

| Stage | Compute | Storage | Approx. month |
|---|---|---|---|
| Weeks 1–3 | Laptop plus Kaggle: $0 | Up to 10 GB free | **$0** plus existing VPS |
| Week 4 and comparator | 20 h Secure 4090 × $0.89 = $18 | 100 GB ≈ $0.70 | **About $19** |
| Fine-tuning month | 80 h × $0.89 = $71 | 500 GB ≈ $3.50 | **About $75** |

## Larger costs not covered above

These dominate real budgets. All need quotes.

| Item | Note |
|---|---|
| Radiologist time for annotation and review | The largest research cost. Pay fairly |
| Legal opinion | Essential |
| Ethics and NACOSTI fees | Confirm |
| Digital Health Agency fees | Data use from KES 5,000 to 1% of budget; certification fees in LN 76 Second Schedule |
| PPB registration | Reported at $250–$2,500 by category and origin (secondary, confirm) |
| Secure computer in Kenya | Facility-controlled |
| Cyber-security assessment | Needed for certification |
| Statistician | For study design |

## Avoiding overspend

- Run overnight on free tiers first.
- Stop GPU instances.
- Downsample.
- Do not start training before evaluating.

## Research funding

Look for clinical AI and global health grants once the first external validation exists. A credible preprint will help more than a demonstration.
