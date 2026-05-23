# Canonical Overview — ComfyUI Custom Node Ecosystem and Nodepack Evaluation

## Core idea

    AIWF should evaluate existing node packs before building new nodes, then classify each pack as use, wrap, document, or build.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- safe_to_generate
- guarded_generate_after_schema_check
- RAG-only node
- nodepack summary
- install risk
- maintenance mode
- native core vs wrapper
- class_type verification

## Common retrieval questions

- Which node pack should I use for inpainting?
- Can this node class_type be placed in generated JSON safely?
- Should AIWF use, wrap, document, or build around this repo?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
