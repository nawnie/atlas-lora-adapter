# Vol. 1 Scope — Python/Pip Runtime Dependencies and Local AI Environment Support

## Lane thesis

    Runtime failures are cluster failures, not isolated package failures; AIWF support should reason across Python, Torch, CUDA, cuDNN, ONNX, media, web server, and native build boundaries.

## In scope

- package cards
- dependency clusters
- native build failures
- CUDA/cuDNN/TensorRT/Triton maps
- Windows venv islands
- one-click installer support
- smoke-test scripts

## Out of scope

- unverified pin advice for every future package version
- blind pip upgrade-all guidance
- mixing incompatible CUDA/Torch wheel families

## Vol. 1 success criteria

This lane is Vol. 1 balanced when a local assistant can:

- answer beginner-to-intermediate questions from this lane without confusing it with adjacent lanes;
- cite or point to the original source family/provenance path;
- retrieve exact technical names when exact names matter;
- distinguish stable principles from fast-moving implementation details;
- identify when a user needs a local schema check, install check, or source refresh before acting.
