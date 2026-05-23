# Embedding and Chunking Strategy — Frontend extensions and UI controls

## Recommended chunk types

- Definition chunks for socket/datatype terms.
- Procedure chunks for implementation steps.
- Failure-signature chunks for runtime errors and migration problems.
- Source-anchor chunks for official ComfyUI docs or source references.

## Lane-specific chunking

For this lane, keep examples and warnings together so retrieval returns both the action and its risk boundary. Do not separate code snippets from the datatype or API contract they rely on.

## Metadata to preserve

- ComfyUI version/source date when known.
- Node class/type names.
- Input and output socket names.
- Required model/object types.
- Whether a claim needs web/source verification.
