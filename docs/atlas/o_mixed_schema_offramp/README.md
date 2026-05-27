# Atlas O Mixed-Schema Off-Ramp Archive

Date: 2026-05-27

This archive records the Atlas O mixed-schema off-ramp results.

## Main Result

O is the best evaluated Atlas adapter direction in this repo so far.

It preserved the previous compact 4B result and improved the targeted retrieval evaluations:

| Eval | O Result |
|---|---:|
| Compact seed cards | 65/65 |
| Targeted top-1 card | 64/65 |
| Targeted top-3 cards | 65/65 |
| Off-ramp focused | 8/8 |
| Hard ID-copy | 14/16 |

## Interpretation

Atlas O is better aligned with the intended architecture than previous runs:

- compact-card performance did not regress;
- targeted top-1 retrieval became reliable in this eval;
- targeted top-3 distractor handling became reliable in this eval;
- the off-ramp behavior passed the focused eval;
- exact-ID/schema drift remains the main weak edge observed in this run.

## Files

```text
docs/atlas/o_mixed_schema_offramp/
├── README.md
├── O_MIXED_SCHEMA_OFFRAMP_REPORT.md
├── atlas_o_visual_summary.md
└── data/
    ├── atlas_o_eval_results.csv
    └── atlas_o_comparison_results.csv
```

## Next Research Direction

Run P as a narrow cleanup adapter:

- keep the O mixed schema;
- add 50-100 exact-ID answer examples;
- add hard negatives with similar lane/card titles;
- retrain 4B for 1 epoch;
- rerun compact, top-1, top-3, off-ramp, and hard-ID evals.

If P preserves O's targeted gains and moves hard-ID from 14/16 to 16/16, P becomes a candidate deployable Atlas adapter baseline.
