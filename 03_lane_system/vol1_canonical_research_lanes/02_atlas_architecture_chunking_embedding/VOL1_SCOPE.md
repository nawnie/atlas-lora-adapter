# Vol. 1 Scope — RAG Architecture, Chunking, and Embedding Strategy

## Lane thesis

    AIWF retrieval should be typed and metadata-rich before it is embedded; dense vectors alone are not enough for code, node names, errors, and package IDs.

## In scope

- typed chunk taxonomy
- metadata contract
- hybrid retrieval policy
- JSONL cards
- CSV record loading
- chunk quality QA
- RAG loader order

## Out of scope

- blind folder embedding as the only strategy
- mixing source manifests with semantic cards without metadata
- flattening structured CSVs into anonymous prose

## Vol. 1 success criteria

This lane is Vol. 1 balanced when a local assistant can:

- answer beginner-to-intermediate questions from this lane without confusing it with adjacent lanes;
- cite or point to the original source family/provenance path;
- retrieve exact technical names when exact names matter;
- distinguish stable principles from fast-moving implementation details;
- identify when a user needs a local schema check, install check, or source refresh before acting.
