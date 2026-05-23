# Embedding and Chunking Strategy — AI Safety, Security, and Red Teaming

## Recommended chunk types
- `definition`: concise canonical definitions for concepts.
- `decision_rule`: if/then framework useful for routing.
- `failure_mode`: common mistakes and anti-patterns.
- `source_anchor`: source-backed fact or official documentation reference.
- `implementation_note`: concrete pattern, command family, or architecture pattern.

## Chunking rules
- Keep definitions short and independent.
- Keep decision frameworks together; do not split an if/then table across chunks.
- Preserve source URLs in the same chunk as the claim when possible.
- Mark volatile tool/version information with freshness metadata.
- Avoid embedding manifests/checksums as knowledge.

## Metadata fields
`lane_id`, `topic`, `chunk_type`, `claim_type`, `freshness`, `source_priority`, `risk_level`, `related_lanes`.
