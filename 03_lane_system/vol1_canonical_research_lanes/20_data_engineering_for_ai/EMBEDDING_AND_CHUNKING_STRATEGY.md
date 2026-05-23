# Embedding and Chunking Strategy — Data Engineering for AI

## Recommended Chunk Types
- `definition_chunk`: core definition and scope.
- `landscape_chunk`: 2026 state-of-the-art / market landscape.
- `decision_chunk`: decision framework bullets.
- `key_fact_chunk`: atomic facts from the Key Facts section.
- `anti_pattern_chunk`: anti-patterns, risks, and mitigations.
- `cross_topic_chunk`: cross-topic hooks.

## Chunking Rules
- Preserve topic number `20` and slug `20_data_engineering_for_ai` in metadata.
- Keep numbered key facts as separate retrievable atoms when possible.
- Do not merge vendor/model claims across topics unless a conflict-resolution pass validates them.
- Treat model/version/date claims as refreshable snapshots.
- Keep source path and section heading in metadata.

## Metadata Fields
`topic_id`, `topic_slug`, `lane_id`, `source_path`, `section`, `claim_type`, `refresh_needed`, `cross_topic_hooks`.
