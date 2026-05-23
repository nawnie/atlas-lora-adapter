# Training Example Types

## 1. Lane routing

The model learns to classify a user question into a primary lane and optional secondary lanes.

## 2. Answer from context

The model learns to answer from retrieved evidence rather than memory.

## 3. Conflict resolution

The model learns to prefer higher-priority or newer sources when retrieved context conflicts.

## 4. Insufficient context

The model learns to say what is missing instead of inventing unsupported details.

## 5. Exactness guard

The model learns not to invent exact commands, file paths, package names, API endpoints, node names, model files, or citations.

## 6. Freshness check

The model learns to flag volatile claims that require current verification.

## 7. Answer-format selection

The model learns whether the response should be a diagnostic tree, roadmap, audit, checklist, evidence map, explanation, or boundary/refusal.

## 8. Multi-RAG generalization

The model learns the reading protocol across more than one Atlas-style corpus so it does not overfit to AIWF-only terms.
