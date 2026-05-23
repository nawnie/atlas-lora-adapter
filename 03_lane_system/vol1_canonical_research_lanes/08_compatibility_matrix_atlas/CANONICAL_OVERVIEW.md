# Canonical Overview — Compatibility Matrix RAG

## Core idea

The assistant should answer “will this work together?” before it answers “how do I install it?”

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- compatibility edge
- requirement node
- model path
- VRAM tier
- CUDA family
- workflow asset contract
- node class requirement
- license caveat
- risk tier

## Common retrieval questions

- Can this workflow run on 8 GB VRAM?
- Which models must be downloaded for this nodepack?
- Does this package belong in the shared ComfyUI venv or an isolated venv?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
