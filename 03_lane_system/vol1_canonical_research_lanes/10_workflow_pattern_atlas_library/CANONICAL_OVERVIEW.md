# Canonical Overview — Workflow Pattern Library RAG

## Core idea

    Reusable workflow patterns should be stored as task graphs with required nodes/assets, not as giant one-off JSON blobs.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- pattern card
- input contract
- processing stage
- output selector
- router shell
- subgraph
- node requirement
- asset requirement
- smoke test
- beginner control panel

## Common retrieval questions

- What is the best graph pattern for auto-inpaint?
- How do I combine restore, pose, and inpaint without making a broken monster workflow?
- Which inputs belong in a master control panel?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
