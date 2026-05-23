# Machine Use Master Index

Start here when using the AIWF Atlas as a retrieval corpus.

## Primary Control Files

- `00_AI_READ_FIRST/SYSTEM_PROMPT_FOR_AI_ASSISTANTS.md` — base behavior contract.
- `00_AI_READ_FIRST/ATLAS_OPERATING_CONTRACT.md` — operating rules and non-goals.
- `00_AI_READ_FIRST/RETRIEVAL_POLICY.md` — retrieval order and fallback behavior.
- `00_AI_READ_FIRST/SOURCE_PRIORITY_AND_CONFLICT_RESOLUTION.md` — how to resolve conflicts.
- `00_AI_READ_FIRST/CONFIDENCE_AND_ANSWER_GATING.md` — when to answer, qualify, or refuse certainty.
- `00_AI_READ_FIRST/EDITORIAL_CONSISTENCY_GUIDE.md` — normalization rules added in the editorial pass.

## Retrieval Layers

- `01_CANONICAL_RESEARCH_LANES/` — edited topic lanes; retrieve these first.
- `02_RETRIEVAL_INDEX/` — global card/index files; use for compact lookup.
- `03_SOURCE_CONTENT/` — original source payloads; use for evidence and deeper detail.
- `03_SOURCE_CONTENT/A_CANONICAL_SOURCE_PACKS/gradio6_rag_archive_20260521_0838/gradio6_rag_archive/` — Gradio 6 handbook source pack; use for Gradio-specific build, migration, deployment, and operations questions.
- `12_RETRIEVAL_RECIPES/` — task-specific retrieval strategies.
- `15_ANSWER_TEMPLATES/` — output templates for recurring answer types.

## Avoid Loading First

Do not prioritize old manifests, reports, or change history for normal user answers. Those are provenance/control files, not topical knowledge.
