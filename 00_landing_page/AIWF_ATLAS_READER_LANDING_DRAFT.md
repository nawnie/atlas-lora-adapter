# AI Without Fear — Atlas Reader LoRA Lab

Status: public-facing landing draft  
Updated: 2026-05-27

## What this is

AIWF Atlas Reader LoRA is a structured-RAG research lab.

It tests whether a small LoRA adapter can learn how to read a versioned Atlas:

```text
query
→ lane
→ card pack
→ source rules
→ answer
```

The Atlas keeps the knowledge.

The adapter target is the reading behavior.

## Current build status

```text
seed lanes: 18+
seed cards: 216+
previous adapter evaluations: recorded
O mixed-schema off-ramp evaluation: recorded
current best evaluated direction: O mixed-schema off-ramp
```

## Current result records

```text
docs/atlas/o_mixed_schema_offramp/O_MIXED_SCHEMA_OFFRAMP_REPORT.md
05_evaluation/previous_adapter_results/PREVIOUS_ADAPTER_RESULTS_FROM_8ZIP.md
```

## Boundaries

This run does not establish open-world generalization, universal adapter portability, global 4B parity with larger models, or production readiness.

## Next proof step

The next run should focus on exact lane/card ID preservation and clean answer wording while keeping the O mixed schema.
