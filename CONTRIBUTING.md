# Contributing

Thank you for helping. This is a research project in a safety-sensitive field, so the rules are stricter than in most repositories.

## Rules that apply to every contribution

- **No patient data.** No images, reports, identifiers or stories that could identify someone, including examples in issues.
- **No restricted data.** Nothing from MIMIC, VinDr, CheXpert, PadChest or similar, including thumbnails, sample reports or per-image scores.
- **No secrets.** No keys, tokens, IP addresses or server details.
- **No invented numbers.** Every performance figure or dataset fact needs a source. Mark what you could not verify.
- **No clinical claims** beyond the evidence. This is a research prototype.

## How to contribute

1. Open an issue before large work.
2. Branch from `main`.
3. Keep changes small, with tests for code that touches data handling, findings logic or QA rules.
4. Run `python tools/check_citations.py` if you edit references.
5. Open a pull request saying what changed and why, and the clinical or scientific effect.

## Clinical and reporting changes

Changes to templates, finding states, thresholds or safety text need review by a qualified clinician. Radiologists are especially welcome as reviewers.

## Style

- Python: type hints, small functions, tests.
- Docs: plain language, and connect technical ideas to clinical practice.
- Note licence and lineage for any new dependency, dataset or weight.

## Licence

By contributing, you agree your code is licensed under Apache-2.0 and your documentation under CC BY 4.0.

## Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
