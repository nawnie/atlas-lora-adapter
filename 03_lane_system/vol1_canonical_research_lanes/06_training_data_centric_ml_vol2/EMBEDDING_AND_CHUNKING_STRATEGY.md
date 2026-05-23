# Embedding and Chunking Strategy — Training, Data-Centric ML, and Volume II Research Spine

## Chunking rule

Chunk by curriculum concept and lab step. Preserve prerequisites, failure signatures, evaluation artifacts, and hardware tier metadata.

## Required metadata fields

- `lane_id`: `RP06`
- `lane_title`: `Training, Data-Centric ML, and Volume II Research Spine`
- `source_family`
- `source_path`
- `doc_role`: concept_card, source_note, package_card, node_card, failure_card, manifest, code, qa_prompt
- `stability`: stable_principle, fast_moving_detail, local_schema_required, source_refresh_required
- `action_policy`: use, wrap, document, build, verify_first
- `retrieval_keys`: exact names, package names, node class types, failure strings, workflow names

## Retrieval strategy

Use hybrid retrieval for this lane. Dense retrieval should catch concepts and explanations; keyword/sparse retrieval should catch exact names, errors, package IDs, node class types, paths, and model filenames.

## What not to embed as normal prose

- duplicate maps unless auditing;
- raw manifests unless the query is about archive structure;
- generated report counts without their source path;
- old version labels as current truth;
- code files without code-aware chunking.

## QA retrieval checks

A good retrieval result should include at least one conceptual chunk and one provenance chunk when the user asks for a technical or operational decision.
