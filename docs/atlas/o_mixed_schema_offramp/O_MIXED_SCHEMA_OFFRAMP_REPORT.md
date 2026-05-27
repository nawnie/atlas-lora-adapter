# O Mixed Schema Off-Ramp Report

Date: 2026-05-27

## Short Answer

A dedicated off-ramp lane had not been built before this run. Earlier work had related freshness guidance in `53_claim_freshness_verification`, but not an active lane whose whole job was:

> Atlas does not contain this; use pretrained knowledge for stable facts, web/current sources for volatile facts, or user-provided files for private facts.

That off-ramp is now built as:

```text
03_lane_system/lanes/54_atlas_off_ramp_external_knowledge
```

The O adapter was trained with that off-ramp behavior mixed into the same message-schema training set as compact Atlas cards, targeted top-1/top-3 retrieval cards, and hard ID-copy examples.

## What Changed

### New Lane

```text
54_atlas_off_ramp_external_knowledge
```

Includes 12 seed cards covering:

- pretrained fallback;
- web/current fallback;
- user-source fallback;
- citation laundering;
- forced nearest-lane answers;
- answer patterns.

### New Dataset Builder

```text
scripts/build_o_mixed_schema_training_records.py
```

### New Training Data

| File | Count | Purpose |
|---|---:|---|
| `04_training_data/atlas_o_mixed_train.jsonl` | 683 | Mixed compact, targeted, hard, and off-ramp training |
| `04_training_data/atlas_o_mixed_eval.jsonl` | 129 | Mixed held-out eval |
| `04_training_data/atlas_o_offramp_eval.jsonl` | 8 | Focused off-ramp eval |

### New Trained Adapter

```text
06_experiments/runs/O_mixed_schema_offramp_4b_r16_lr0001_1epoch/adapter
```

## Training Result

| Item | Value |
|---|---|
| Base model | `Qwen/Qwen1.5-4B-Chat` |
| LoRA | r16 alpha32 dropout0.05 |
| Epochs | 1 |
| Optimizer steps | 86 |
| Train records | 683 |
| Eval records | 129 |
| Train runtime | 489.9s |
| Train loss | 1.4640 |
| Eval loss | 0.8271 |
| Eval token accuracy | 0.8342 |

Training was stable. VRAM got tight during the training run, with a spot-check near 15.95 GB of 16.38 GB used, but there was no crash or OOM. Evaluation runs stayed much lighter at roughly 4.4-4.6 GB VRAM.

## Evaluation Results

| Eval | Adapter | Pass | Avg Total Tokens | Top Failure |
|---|---|---:|---:|---|
| Compact seed cards | O | 65/65 | 651.4 | none |
| Targeted top-1 card | O | 64/65 | 423.6 | hallucinated_source x1 |
| Targeted top-3 cards | O | 65/65 | 660.3 | none |
| Off-ramp focused | O | 8/8 | 421.3 | none |
| Hard ID-copy | O | 14/16 | 742.0 | schema_drift x2 |

## Comparison To Previous Runs

| Test | Old Best / Relevant Baseline | O Result | Meaning |
|---|---:|---:|---|
| Compact 4B N | 65/65 | 65/65 | O preserved the compact champion behavior |
| Top-1 4B N | 17/65 | 64/65 | O fixed the targeted retrieval shape problem |
| Top-1 0.5B J | 47/65 | 64/65 | O beats the old small-model targeted result |
| Top-3 4B N | 9/65 | 65/65 | O fixed distractor-card handling |
| Hard ID-copy 4B N | 12/16 | 14/16 | O improved exactness, but this remains the weak edge |

## Decision

O is the current best Atlas adapter direction.

Use:

- top-1 retrieval when token efficiency matters and retrieval confidence is high;
- top-3 retrieval when reliability matters more than token cost;
- lane 54 off-ramp when Atlas evidence is absent instead of forcing a trigger word or inventing an Atlas answer.

Do not use:

- raw workspace dumping as the main architecture;
- activation tokens as the primary routing mechanism;
- nearest-lane guessing when no Atlas evidence exists.

## Remaining Weakness

The only meaningful weakness left in this run is exact schema behavior under artificial exact-ID stress. The two hard-ID misses copied the correct lane and card IDs, but drifted into generated test-language instead of answering the task cleanly.

Next training run should add more examples that say:

- preserve the exact lane/card ID;
- still answer the user request;
- never echo the synthetic test instruction as the answer;
- never produce generated exact-ID copy boilerplate.

## Next Action

Make a P run focused only on the remaining weakness:

1. Add 50-100 exact-ID answer examples with clean final-answer wording.
2. Add hard negatives where the chosen card is correct but nearby cards share similar lane titles.
3. Keep the O mixed schema.
4. Retrain for 1 epoch on 4B.
5. Rerun compact, top-1, top-3, off-ramp, and hard-ID evals.

If P keeps O's targeted gains and moves hard-ID from 14/16 to 16/16, it becomes the deployable Atlas adapter baseline.
