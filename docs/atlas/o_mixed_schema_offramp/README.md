# Atlas O Mixed-Schema Off-Ramp Archive

Date: 2026-05-27

This archive is a repo-ready package for the Atlas O mixed-schema off-ramp results.

## Main Result

O is the current best Atlas adapter direction.

It preserved the compact 4B champion behavior and fixed the previous targeted retrieval failures:

| Eval | O Result |
|---|---:|
| Compact seed cards | 65/65 |
| Targeted top-1 card | 64/65 |
| Targeted top-3 cards | 65/65 |
| Off-ramp focused | 8/8 |
| Hard ID-copy | 14/16 |

## Interpretation

Atlas O appears to be the first adapter that is architecturally correct rather than merely benchmark-lucky:

- compact-card performance did not regress;
- targeted top-1 retrieval became reliable;
- targeted top-3 distractor handling became reliable;
- the off-ramp behavior works in focused eval;
- exact-ID/schema drift remains the only meaningful weak edge.

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

Binary chart images and raw result archives were generated locally but were not uploaded through the connector commit path in this pass.

## Next Research Direction

Run P as a narrow cleanup adapter:

- keep the O mixed schema;
- add 50-100 exact-ID answer examples;
- add hard negatives with similar lane/card titles;
- retrain 4B for 1 epoch;
- rerun compact, top-1, top-3, off-ramp, and hard-ID evals.

If P preserves O's targeted gains and moves hard-ID from 14/16 to 16/16, P becomes the deployable Atlas adapter baseline.
