# Atlas O Visual Summary

Date: 2026-05-27

## Main read

Atlas O preserves the compact-card champion behavior and fixes the previous targeted-retrieval weakness.

The key result is not just that compact seed cards stayed at **65/65**. The real breakthrough is:

- Top-1 4B improved from **17/65** to **64/65**.
- Top-3 4B improved from **9/65** to **65/65**.
- Off-ramp focused eval scored **8/8**.
- Hard ID-copy improved from **12/16** to **14/16**, but remains the weak edge.

## Chart files

Chart images were generated locally in the archive package:

- `assets/atlas_o_eval_pass_rates.png`
- `assets/atlas_o_previous_vs_o.png`
- `assets/atlas_o_avg_tokens.png`

They were not uploaded through the connector commit path in this pass.

## Best caption

> Atlas O is the first adapter that looks architecturally correct rather than merely benchmark-lucky: it preserves compact-card performance, repairs targeted retrieval behavior, handles distractor cards, and adds an off-ramp path when Atlas evidence is absent.
