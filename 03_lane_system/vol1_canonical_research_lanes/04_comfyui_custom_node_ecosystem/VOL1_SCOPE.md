# Vol. 1 Scope — ComfyUI Custom Node Ecosystem and Nodepack Evaluation

## Lane thesis

    AIWF should evaluate existing node packs before building new nodes, then classify each pack as use, wrap, document, or build.

## In scope

- nodepack coverage
- workflow generation safety
- class_type strings
- install risk
- maintenance status
- model file requirements
- ComfyUI Manager install flow

## Out of scope

- rebuilding solved node packs without a clear gap
- using deprecated IDs in new workflows
- making beginner workflows depend on unstable expert wrappers by default

## Vol. 1 success criteria

This lane is Vol. 1 balanced when a local assistant can:

- answer beginner-to-intermediate questions from this lane without confusing it with adjacent lanes;
- cite or point to the original source family/provenance path;
- retrieve exact technical names when exact names matter;
- distinguish stable principles from fast-moving implementation details;
- identify when a user needs a local schema check, install check, or source refresh before acting.
