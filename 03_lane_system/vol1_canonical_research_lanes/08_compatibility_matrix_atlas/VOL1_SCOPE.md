# Vol. 1 Scope — Compatibility Matrix RAG

## Lane thesis

The assistant should answer “will this work together?” before it answers “how do I install it?”

## In scope

- hardware/software compatibility
- model asset placement
- nodepack requirements
- Python/CUDA/Torch compatibility
- workflow missing asset detection
- commercial/license caveats

## Out of scope

- assuming all models fit all hardware
- installing every nodepack in one environment without risk separation
- ignoring model license when building public workflows

## Vol. 1 success criteria

This lane is Vol. 1 balanced when a local assistant can:

- answer beginner-to-intermediate questions from this lane without confusing it with adjacent lanes;
- cite or point to the original source family/provenance path;
- retrieve exact technical names when exact names matter;
- distinguish stable principles from fast-moving implementation details;
- identify when a user needs a local schema check, install check, or source refresh before acting.
