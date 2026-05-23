# Vol. 1 Scope — Workflow Pattern Library RAG

## Lane thesis

    Reusable workflow patterns should be stored as task graphs with required nodes/assets, not as giant one-off JSON blobs.

## In scope

- pattern cards
- workflow graph motifs
- router shell design
- model-loader patterns
- inpaint/upscale/video patterns
- subgraph/componentization policy
- QA smoke tests

## Out of scope

- stapling unrelated workflows together without routing logic
- assuming JSON can be generated safely without object_info
- hiding required user inputs deep in the graph

## Vol. 1 success criteria

This lane is Vol. 1 balanced when a local assistant can:

- answer beginner-to-intermediate questions from this lane without confusing it with adjacent lanes;
- cite or point to the original source family/provenance path;
- retrieve exact technical names when exact names matter;
- distinguish stable principles from fast-moving implementation details;
- identify when a user needs a local schema check, install check, or source refresh before acting.
