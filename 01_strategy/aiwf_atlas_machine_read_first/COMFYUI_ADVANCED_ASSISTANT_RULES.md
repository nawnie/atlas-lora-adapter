# ComfyUI Advanced Assistant Rules

Use these rules before modifying or advising on ComfyUI workflows or custom nodes.

## First principle

A ComfyUI node socket type is a contract. Do not tell the user to change `IMAGE` to `LATENT` unless the function body also changes to handle the latent data structure.

## IMAGE / LATENT / MASK rule

- `IMAGE`: tensor `[B,H,W,C]`, pixel-space, RGB/channel-last.
- `LATENT`: dictionary with `samples` tensor `[B,C,H,W]`, latent-space, channel-first.
- `MASK`: single-channel tensor commonly shaped `[B,H,W]`, but custom nodes should inspect and normalize shape.
- Pixel operations require `IMAGE`.
- Denoising-space operations require `LATENT`.
- Mask operations require explicit shape and scale handling.
- If crossing spaces, use explicit VAE Encode / VAE Decode nodes or a custom node that explicitly accepts a `VAE` and performs the conversion.

## Before giving code

Ask internally:

1. What datatype enters the node?
2. What datatype leaves the node?
3. Does the computation assume PIL/OpenCV/RGB pixels?
4. Does the computation assume latent `samples`?
5. Are shapes preserved?
6. Does `RETURN_TYPES` match the actual returned Python object?
7. Should this be a separate node instead of mutating the old one?
8. Does the change break saved workflow JSON or downstream sockets?

## Source priority

Use `31_comfyui_datatype_conversion_boundaries` for datatype conversion and boundary questions. Use `26` for socket contracts, `27` for node authoring, `28` for workflow/subgraph/API, `29` for frontend/UI, and `30` for troubleshooting/packaging.

## Workflow API and Gradio bridge rules

- Always distinguish UI workflow JSON from API prompt JSON before giving automation code.
- For local ComfyUI, prefer local route names such as `/prompt`, `/history/{prompt_id}`, `/view`, `/upload/image`, `/queue`, and `/object_info`.
- For ComfyUI Cloud, explicitly say the endpoint and authentication model differs from local ComfyUI.
- When building Gradio apps over ComfyUI, expose a small workflow contract instead of exposing arbitrary node mutation.
- Use Gradio queue and concurrency controls for GPU-bound work; default to one active generation per local backend unless the backend is intentionally configured for parallel jobs.
- Keep per-user prompt IDs, files, and output lists in session state rather than shared global state.
- Surface ComfyUI validation errors and node errors in the UI log instead of hiding them.


## Advanced workflow design rules

- For giant workflows, recommend modular boundaries before adding more custom nodes.
- Use subgraphs when a section is reusable and has stable typed inputs/outputs.
- Use workflow templates for learning examples and one-click starting points.
- Use subgraph blueprints when reusable modules should ship with a node pack.
- Use Switch for simple typed selection and Soft Switch or lazy custom switches when unused branches should not evaluate.
- Do not treat bypass/mute as the same thing as runtime routing.
- For Gradio/API control, treat the workflow as a versioned app contract with stable node IDs and output nodes.
