# Source Priority and Conflict Resolution

## Source classes

- Canonical lane files: synthesized Vol. 1 knowledge for a topic.
- Atlas cards: compact routing and answer scaffolds.
- Source content: raw or semi-raw imported research and project data.
- Manifests: file provenance, deduplication, and archive integrity.
- Reports: consolidation and maintenance history.
- expansion slots: planned work; not authoritative.

## Priority rules

1. Canonical lane files outrank raw content for normal answers.
2. Raw source content outranks canonical files when the user asks for exact provenance or a specific older version.
3. Reports/manifests outrank all content for archive-maintenance questions.
4. expansion slots are not evidence; they are project planning markers.
5. Current official docs/repositories outrank this archive for live software status.

## Staleness rules

Many topics are version-sensitive: ComfyUI nodes, Gradio APIs, Python packages, model licenses, repo maintenance status, CUDA/PyTorch compatibility, and custom-node install steps. If a recommendation depends on current state, the assistant should say so and verify externally when tools are available.
