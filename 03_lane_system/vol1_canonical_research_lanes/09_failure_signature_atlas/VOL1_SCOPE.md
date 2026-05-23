# Vol. 1 Scope — Failure Signature Atlas RAG

## Lane thesis

    Failures should be retrieved by symptom, log fragment, likely layer, and safe recovery path, not just by package name.

## In scope

- OOM signatures
- missing node signatures
- missing model signatures
- import/ABI errors
- CUDA/cuDNN provider issues
- workflow red-node diagnosis
- bad generation symptoms

## Out of scope

- guessing root cause from one vague symptom
- fixing by reinstalling everything first
- mixing destructive repair steps into beginner guidance

## Vol. 1 success criteria

This lane is Vol. 1 balanced when a local assistant can:

- answer beginner-to-intermediate questions from this lane without confusing it with adjacent lanes;
- cite or point to the original source family/provenance path;
- retrieve exact technical names when exact names matter;
- distinguish stable principles from fast-moving implementation details;
- identify when a user needs a local schema check, install check, or source refresh before acting.
