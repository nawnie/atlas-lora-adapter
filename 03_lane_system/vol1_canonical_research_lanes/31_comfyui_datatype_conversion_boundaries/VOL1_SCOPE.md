# Scope — ComfyUI Datatype Conversion and Boundary Design

## In scope

- Built-in datatype roles: `IMAGE`, `LATENT`, `MASK`, `AUDIO`, `MODEL`, `CLIP`, `VAE`, `CONDITIONING`, `NOISE`, `SAMPLER`, `SIGMAS`, and `GUIDER`.
- Practical conversion boundaries, especially VAE Encode and VAE Decode.
- Safe node I/O changes using `INPUT_TYPES`, `RETURN_TYPES`, and correct return tuples.
- Shape and channel-order differences between image tensors, mask tensors, and latent dictionaries.
- Router/switch nodes that use lazy evaluation or V3 `MultiType`/`MatchType` patterns.
- Decision rules for when to build a new node instead of mutating an existing node.

## Out of scope

- Claiming that arbitrary pixel-space image processing can be performed directly on latents.
- Treating socket label changes as sufficient without changing the function body.
- Recommending wildcard or generic sockets without validation and failure messaging.
- Exact implementation details for every custom node pack.
