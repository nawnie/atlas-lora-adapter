# Embedding and Chunking Strategy — ComfyUI Datatype Boundaries

## Chunk as code-safe units

Keep code examples intact. Do not split the class definition away from its `INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION`, and execution method.

## High-value chunks

- `IMAGE` vs `LATENT` comparison
- VAE boundary rules
- safe `IMAGE` to `LATENT` node conversion checklist
- mask shape normalization guidance
- V3 `MultiType` and `MatchType` routing notes
- failure signatures for wrong socket changes

## Metadata to preserve

- datatype names in uppercase
- tensor shapes
- source IDs
- workflow role: pixel-space, latent-space, model-object, conditioning-object, sampling-object
- risk level: low, medium, high
- answer template: explanation, code patch, workflow rewrite, debugging triage

## Retrieval warning

Do not answer datatype conversion questions from old workflow JSON alone. Retrieve the official datatype contract and the custom node property contract first.
