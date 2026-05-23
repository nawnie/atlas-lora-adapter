# Vol. 1 Scope — ComfyUI Core API, Workflow JSON, and Subgraph Research

## Lane thesis

    Workflow JSON generation must be schema-first: object_info/socket names and link topology are more reliable than remembered node labels.

## In scope

- object_info capture
- workflow JSON validation
- link/socket source-of-truth policy
- subgraph and partial execution patterns
- schema capture scripts
- partner-node boundaries

## Out of scope

- guessing node socket names
- generating custom-node workflows without local schema confirmation
- treating display names as class_type strings

## Vol. 1 success criteria

This lane is Vol. 1 balanced when a local assistant can:

- answer beginner-to-intermediate questions from this lane without confusing it with adjacent lanes;
- cite or point to the original source family/provenance path;
- retrieve exact technical names when exact names matter;
- distinguish stable principles from fast-moving implementation details;
- identify when a user needs a local schema check, install check, or source refresh before acting.
