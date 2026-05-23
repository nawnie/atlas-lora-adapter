# Decision Log

## Decision 001 — Separate repo for Atlas Reader LoRA

Date: 2026-05-22

Decision:

Create a dedicated repo for the Atlas Reader LoRA instead of burying it inside the AIWF Atlas.

Reason:

The adapter is a reusable research track. It should be testable against multiple corpora and model families.

## Decision 002 — Train behavior, not facts

Date: 2026-05-22

Decision:

Training examples should teach source hierarchy, lane routing, answer discipline, exactness, and uncertainty handling.

Do not train raw Atlas dumps.

Reason:

Facts become stale. Reading behavior is reusable.

## Decision 003 — Preserve failed experiments

Date: 2026-05-22

Decision:

Even failed adapter experiments should be documented.

Reason:

Negative results can show whether the issue is adapter design, dataset quality, model capacity, retrieval quality, or the Atlas structure itself.
