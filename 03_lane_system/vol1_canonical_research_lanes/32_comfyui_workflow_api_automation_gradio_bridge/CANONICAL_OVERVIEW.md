# Canonical Overview — ComfyUI Workflow API Automation and Gradio Bridge Patterns

ComfyUI can be used as more than a canvas. The local server exposes routes that the frontend itself uses to submit work, inspect queue state, retrieve history, upload images, and fetch outputs. The practical automation pattern is:

1. Build and test a workflow visually.
2. Export or construct the workflow in API prompt format.
3. Mutate only the user-facing inputs the app is allowed to control.
4. Submit to the local queue.
5. Track progress with WebSocket or polling.
6. Retrieve outputs from history and `/view`.
7. Surface errors and node validation messages to the user.

## Workflow JSON vs API prompt JSON

ComfyUI workflow JSON is the UI graph serialization governed by the workflow JSON schema. API prompt JSON is the execution payload style used by the API examples: node IDs are keys and each node contains `class_type` and `inputs`. This distinction matters because UI state, canvas positions, groups, and links are not the same thing as the minimal execution graph.

## Local API pattern

The local route pattern centers on `/prompt`. The server validates a prompt and queues it. A successful response includes a `prompt_id` and queue number. A failed response includes an error and node-level validation details. After completion, `/history/{prompt_id}` can be used to inspect outputs, and `/view` can fetch generated files.

## Gradio bridge pattern

A Gradio bridge should not expose the whole workflow. It should expose a small contract:

- prompt text
- negative prompt
- seed or randomize seed
- dimensions or preset selector
- input image/mask where needed
- output preview
- log/status panel
- advanced settings behind a foldout

The Gradio app owns the user experience. ComfyUI owns the graph execution. The bridge translates UI controls into node input mutations and translates ComfyUI responses into readable status, errors, and outputs.

## Queue and state rule

GPU work must be queued deliberately. Gradio supports queue control and concurrency limits; ComfyUI also has its own execution queue. For a single local GPU, default to one active generation path unless the backend is intentionally designed for parallel workloads.

## Security rule

Do not expose raw ComfyUI endpoints directly to untrusted users. Put a controlled app layer in front of it, validate file uploads and workflow selection, restrict exposed parameters, and avoid arbitrary path writes.
