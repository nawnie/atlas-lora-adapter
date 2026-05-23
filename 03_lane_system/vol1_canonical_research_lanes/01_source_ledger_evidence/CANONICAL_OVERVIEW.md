# Canonical Overview — Source Ledger and Evidence Governance

## Core idea

The RAG should know why it believes a claim, where the claim came from, and when the claim must be refreshed.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- source ledger
- evidence grade
- claim lineage
- refresh queue
- canonical source
- derived card
- provenance path
- conflict note
- staleness risk

## Common retrieval questions

- Which source supports this ComfyUI node claim?
- Is this package/card source-backed or chat-derived?
- What should be refreshed before publishing?
- Which older file was consolidated into the canonical copy?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
