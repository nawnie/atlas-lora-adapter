# Canonical Overview — RAG Architecture, Chunking, and Embedding Strategy

## Core idea

    AIWF retrieval should be typed and metadata-rich before it is embedded; dense vectors alone are not enough for code, node names, errors, and package IDs.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- semantic markdown
- structured rows
- json records
- code-aware chunks
- metadata-only files
- hybrid retrieval
- reranking
- heading path
- chunk intent
- retrieval test prompt

## Common retrieval questions

- How should I chunk package cards?
- Should CSV files be embedded as prose or records?
- What metadata should survive into AnythingLLM or a vector DB?
- Why did dense retrieval miss an exact node class name?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
