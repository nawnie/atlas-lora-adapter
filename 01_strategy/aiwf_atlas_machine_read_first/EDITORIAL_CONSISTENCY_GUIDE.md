# Editorial Consistency Guide for AI Systems

This adapter is optimized for machine retrieval and answer grounding. Use this guide to normalize interpretation across lanes.

## Naming

- Use **AIWF Atlas** for the archive.
- Use **lane** for a topic-specific research area.
- Use **Atlas card** for compact machine-readable facts, decisions, warnings, and QA hooks.
- Use **source payload** for original uploaded/source material preserved for provenance.
- Use **canonical lane** for edited machine-facing summaries, scopes, concept maps, QA prompts, and Atlas cards.

## Do Not Over-Read Version Labels

Version labels inside source filenames may represent source provenance, not current truth. Prefer canonical lane files and Atlas cards first, then raw source payloads for detail.

## Answering Priority

1. Identify the user task.
2. Retrieve the matching canonical lane or retrieval recipe.
3. Check source payload only when exact evidence, model names, paths, or warnings are needed.
4. Resolve conflicts using `SOURCE_PRIORITY_AND_CONFLICT_RESOLUTION.md`.
5. Answer with caveats when the archive marks an area as stale, incomplete, risky, or fast-moving.

## Style

- Prefer direct operational guidance.
- Prefer exact node/model/file/path names when available.
- Do not turn historical notes into current recommendations.
- Do not claim a feature exists unless the adapter has a canonical card or source payload for it.
- Do not present raw source notes as polished public documentation.
