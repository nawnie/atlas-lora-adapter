# Chunking and Indexing Guide

## Chunk types

Use typed chunks rather than one generic splitter.

### Atlas cards

- One JSONL row = one chunk.
- Preserve fields exactly.
- Use for query routing and fast answer planning.

### Canonical markdown

- Split by H2/H3 sections.
- Preserve heading path as metadata.
- Keep warnings and caveats attached to the section they qualify.

### CSV files

- Index row-wise when each row is independent.
- Index file-wise summaries for small CSVs.
- Preserve column names.

### Code / workflow JSON

- Do not blindly split by tokens.
- Preserve schema-level structure.
- Keep node class names, inputs, outputs, and links together.

### Manifests/reports

- Usually exclude from normal answer retrieval unless the query is archive maintenance, provenance, deduplication, or source coverage.

## Suggested embedding strategy

- Hybrid retrieval is recommended: vector + keyword/BM25.
- Exact-match terms matter: node names, filenames, packages, CLI flags, paths, repo names.
- Add reranking if the system supports it.
- Use lane metadata to filter before semantic search when possible.

## Bad indexing patterns

Avoid:

- one huge chunk per folder;
- splitting exact class names away from their context;
- mixing historical source fragments with canonical lane files without metadata;
- embedding duplicate manifests as if they are teaching content;
- treating expansion slots as complete knowledge.
