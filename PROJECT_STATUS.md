# Project Status

Date: 2026-05-27
Status: O evaluation recorded

## Current state

The repo has moved past the earlier pre-training scaffold status. Earlier files that say no adapter had been trained reflect the May 23 upload-prep state and are now superseded by the May 27 O evaluation records.

## Current best evaluated direction

The current best evaluated Atlas adapter direction is the O mixed-schema run.

| Eval | O Result |
|---|---:|
| Compact seed cards | 65/65 |
| Targeted top-1 card | 64/65 |
| Targeted top-3 cards | 65/65 |
| Off-ramp focused | 8/8 |
| Hard ID-copy | 14/16 |

## Safe current claim

Atlas O is the best evaluated adapter direction in this repo so far under the recorded internal evaluation conditions.

## Claim boundary

Do not claim open-world generalization, universal model portability, global 4B parity with larger models, or production readiness from this run.

## Next work

The next run should focus on exact lane/card ID preservation while still answering the user request cleanly.
