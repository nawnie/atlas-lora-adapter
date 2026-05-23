# Canonical Overview — Training, Data-Centric ML, and Volume II Research Spine

## Core idea

    Training knowledge should start with data, objective, evaluation, and failure evidence before discussing trainer buttons or model hype.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- data-centric ML
- dataset split
- leakage
- label quality
- objective function
- evaluation set
- adapter training
- LoRA rank
- overfitting
- release ethics

## Common retrieval questions

- Should this problem use prompting, RAG, LoRA, or fine-tuning?
- How do I inspect a dataset before training?
- What does overfitting look like in a small local training run?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
