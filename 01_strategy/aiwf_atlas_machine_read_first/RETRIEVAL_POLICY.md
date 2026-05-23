# Retrieval Policy

## Priority order

1. `00_AI_READ_FIRST/` for assistant behavior and archive rules.
2. `02_RETRIEVAL_INDEX/` for fast routing and high-signal cards.
3. `01_CANONICAL_RESEARCH_LANES/` for synthesized answers.
4. `03_SOURCE_CONTENT/` for exact details and provenance.
5. `04_MANIFESTS/` and `05_REPORTS/` for audit-only questions.
6. `07_EXPANSION_QUEUE/` for planned but incomplete topics.

## Conflict handling

When two chunks disagree:

- Prefer canonical lane over raw source notes.
- Prefer newer consolidated research over older source-pack fragments.
- Prefer primary-source-backed claims over unsourced commentary.
- Preserve warnings and caveats even when inconvenient.
- If the user needs current repo/API/software status, state that it must be verified against current official sources.

## Retrieval failure handling

If retrieval does not find a useful answer:

- Say the archive does not contain enough information.
- Name the nearest lane or planned topic that should cover it.
- Suggest a new Atlas card or source type to add.
- Do not hallucinate exact commands, paths, node names, or model files.

## Answer patterns

Use the archive differently by user need:

- Concept question: answer from canonical overview and concept map.
- Build question: answer from workflow patterns, implementation notes, and source files.
- Debug question: answer from failure signatures, runtime lanes, and exact logs when provided.
- Research continuation: update gap audits, lane manifests, Atlas cards, and source coverage.
- Data/embedding question: use metadata contracts, chunking strategy, and retrieval index guidance.
