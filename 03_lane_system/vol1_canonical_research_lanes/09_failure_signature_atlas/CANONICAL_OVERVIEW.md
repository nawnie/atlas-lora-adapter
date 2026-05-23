# Canonical Overview — Failure Signature Atlas RAG

## Core idea

    Failures should be retrieved by symptom, log fragment, likely layer, and safe recovery path, not just by package name.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- symptom
- log fragment
- likely layer
- confidence
- first safe test
- recovery ladder
- do-not-do step
- escalation artifact
- support report

## Common retrieval questions

- What does this traceback usually mean?
- Why are my nodes red?
- What log should I paste for help?
- How do I recover from CUDA/cuDNN mismatch safely?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
