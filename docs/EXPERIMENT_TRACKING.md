# Experiment Tracking

An unlogged experiment is like an undocumented patient review: it may have happened, but no one can rely on it.

## Tool choice

**Start with MLflow running locally**, with a file or SQLite backend. It is free, needs no account, and does not send data to a third party. Metadata can move to PostgreSQL later. Avoid hosted trackers for anything derived from credentialed data, unless the terms are checked.

## Record for every run

| Group | Fields |
|---|---|
| Identity | `experiment_id`, `run_id`, date, person |
| Hypothesis | What you expect, stated first |
| Code | Git commit, dirty flag |
| Environment | Python and package lock, hardware |
| Data | `dataset_id`, version, manifest hash, split file hash |
| Preprocessing | Pipeline version |
| Model | Name, version, weights checksum, source |
| **Lineage** | Training datasets, licences, `product_use` status |
| Parameters | Thresholds, seeds, batch size |
| Results | Metrics with intervals, per finding and subgroup |
| Artefacts | Curves, error tables. No restricted images |
| Conclusion | What it means, in plain words |

## Lineage record

```yaml
model_id: baseline-densenet-0.1.0
weights: densenet121-res224-all
source: torchxrayvision
training_data: [to confirm from source]
code_licence: see upstream LICENSE
weights_licence: not stated upstream
research_use: yes
publication: yes
product_use: unclear
clinical_use: no
```

## Naming

```text
exp-0001-baseline-rsna-independent
exp-0002-calibration-valset
```

## Layout

```text
experiments/
  exp-0001-.../
    README.md          hypothesis, how to run, conclusion
    config.yaml
    results.json       aggregate only
```

Aggregate results may be committed if the dataset terms allow. Per-image scores for restricted data stay private. Check the rules for sharing derived data first.

## Rules

1. Write the hypothesis before running.
2. Never overwrite a run. Add a new one.
3. Failed experiments are kept.
4. Evaluate the test set once. Log every look.
5. A published figure must trace back to a run ID.
