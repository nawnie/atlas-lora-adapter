# Canonical Overview — ComfyUI Core API, Workflow JSON, and Subgraph Research

## Core idea

    Workflow JSON generation must be schema-first: object_info/socket names and link topology are more reliable than remembered node labels.

## Operational model

The lane should be used as a decision layer, not just a library of facts. The assistant should first identify the user's task, then retrieve the relevant concept card, then check the source/provenance folder, then produce an action with a safety or validation step when needed.

## Main concepts

- object_info
- class_type
- input socket
- output socket
- links array
- node widgets_values
- subgraph
- partial execution
- schema capture
- workflow manifest

## Common retrieval questions

- How do I verify a ComfyUI workflow JSON before giving it to a user?
- Which fields are source of truth in workflow JSON?
- How should subgraphs be represented for a beginner UI?

## Practical AIWF decision posture

- **Use** existing projects when they already solve the problem cleanly.
- **Wrap** existing projects when AIWF can make them safer, clearer, or easier for beginners.
- **Document** existing behavior when the main value is explanation and failure prevention.
- **Build** only when a real gap remains after repo/package/workflow evaluation.

## Stable vs fast-moving knowledge

    Stable: concepts, failure categories, task boundaries, metadata requirements, and validation habits.
    Fast-moving: package versions, ComfyUI node schemas, model file names, API-only vs open-weight model status, install commands, and repo maintenance status.
