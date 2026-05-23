# How To Use This Knowledge Set

## Recommended ingestion model

This archive is built for layered retrieval.

### Layer 1: Atlas cards

Index first:

- `02_RETRIEVAL_INDEX/CANONICAL_RETRIEVAL_CARDS_CURRENT.jsonl`

Use these as high-signal routing cards. They are compact and should help the AI choose the right lane quickly.

### Layer 2: Canonical lanes

Index second:

- `01_CANONICAL_RESEARCH_LANES/`

These files contain the intended synthesized Vol. 1 knowledge for each project lane. They are the best answer source when available.

### Layer 3: Source content

Index third:

- `03_SOURCE_CONTENT/`

Use source content for exact tables, old versions, historical context, provenance, and deeper evidence.

### Layer 3a: Gradio 6 handbook source pack

Index alongside source content when the question is about Gradio 6:

- `03_SOURCE_CONTENT/A_CANONICAL_SOURCE_PACKS/gradio6_rag_archive_20260521_0838/gradio6_rag_archive/`

Use `AI_GUIDANCE.md` and `RAG_INDEX.md` in that folder as routing files, then retrieve the most relevant chapter section files.

### Layer 4: Manifests and reports

Usually do not use these for normal user answers. Use them for archive integrity, deduplication history, file provenance, and maintenance.

## Chunking guidance

- Keep Atlas cards intact as single chunks.
- Chunk canonical markdown by heading, not arbitrary token count.
- Keep tables and CSV rows structurally intact.
- Preserve exact identifiers: node class names, repo names, model filenames, paths, command flags, package names.
- Do not merge unrelated lanes just because they share generic AI terms.

## Metadata to preserve

Recommended metadata fields:

- `archive_name`: AIWF_Knowledge_Adapter_VOL1
- `layer`: read_first | retrieval_index | canonical_lane | source_content | manifest | report | current_field
- `lane_id`
- `lane_title`
- `source_path`
- `content_type`
- `version_label`
- `provenance_role`: canonical | supporting | historical | audit | current_field
- `risk_level`: low | medium | high when applicable
- `needs_current_verification`: true/false

## Query routing hints

- ComfyUI node/workflow questions: route to ComfyUI lanes and node ecosystem files.
- RAG/chunking questions: route to RAG architecture lane and retrieval policy.
- Gradio app questions: route to Gradio UI research lane.
- Runtime/pip/install questions: route to Python/Pip Runtime lane and source content.
- Failure diagnosis: route to Failure Signature Atlas and relevant source details.
- Missing future topics: check expansion slots and gap audits.
