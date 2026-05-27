# O Mixed Schema Off-Ramp Report

Date: 2026-05-27

## Summary

The O run introduced mixed-schema training that includes compact Atlas cards, targeted top-1/top-3 retrieval cards, exact-ID examples, and off-ramp behavior.

The off-ramp behavior is identified as:

```text
54_atlas_off_ramp_external_knowledge
```

Its purpose is to keep the model from forcing an Atlas answer when the provided Atlas evidence is not enough.

## Training Setup

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

## Evaluation Results

| Eval | Adapter | Pass | Avg Total Tokens | Top Failure |
|---|---|---:|---:|---|
| Compact seed cards | O | 65/65 | 651.4 | none |
| Targeted top-1 card | O | 64/65 | 423.6 | source error x1 |
| Targeted top-3 cards | O | 65/65 | 660.3 | none |
| Off-ramp focused | O | 8/8 | 421.3 | none |
| Exact ID-copy | O | 14/16 | 742.0 | schema drift x2 |

## Comparison To Previous Runs

| Test | Old Best / Relevant Baseline | O Result | Meaning |
|---|---:|---:|---|
| Compact 4B N | 65/65 | 65/65 | O preserved the previous best compact 4B result |
| Top-1 4B N | 17/65 | 64/65 | O improved the targeted retrieval shape problem |
| Top-1 0.5B J | 47/65 | 64/65 | O exceeded the earlier small-model targeted result |
| Top-3 4B N | 9/65 | 65/65 | O improved distractor-card handling |
| Exact ID-copy 4B N | 12/16 | 14/16 | O improved exactness, but this remains a weak edge |

## Decision

O is the best evaluated Atlas adapter direction in this repo so far.

Use:

- top-1 retrieval when token efficiency matters and retrieval confidence is high;
- top-3 retrieval when reliability matters more than token cost;
- off-ramp behavior when Atlas evidence is absent.

Avoid:

- raw workspace dumping as the main architecture;
- activation tokens as the primary routing mechanism;
- nearest-lane guessing when no Atlas evidence exists.

## Remaining Weakness

The main weakness observed in this run is exact schema behavior under artificial exact-ID stress.

The next training run should add examples that require the model to preserve the exact lane/card ID while still answering the user request cleanly.

## Next Action

Make a P run focused on the remaining exact-ID/schema weakness:

1. Add 50-100 exact-ID answer examples with clean final-answer wording.
2. Add hard negatives where the chosen card is correct but nearby cards share similar lane titles.
3. Keep the O mixed schema.
4. Retrain for 1 epoch on 4B.
5. Rerun compact, top-1, top-3, off-ramp, and exact-ID evals.

If P keeps O's targeted gains and moves exact-ID from 14/16 to 16/16, it becomes a candidate deployable Atlas adapter baseline.
