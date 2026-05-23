# Concept Map — ComfyUI Workflow API Automation and Gradio Bridge Patterns

## Core entities

- `workflow_json`: UI graph serialization with canvas/layout state and graph metadata
- `api_prompt_json`: executable prompt payload keyed by node ID with `class_type` and `inputs`
- `node_id`: stable identifier used to mutate specific inputs in an API payload
- `class_type`: node implementation name used by ComfyUI execution
- `prompt_id`: job identifier returned after queue submission
- `history`: completed or recorded job output metadata
- `view`: file retrieval route for generated outputs
- `upload`: input file transfer step before image/mask workflows
- `gradio_state`: session or browser state used to track prompt IDs and temporary paths

## Relationships

- Gradio UI controls mutate selected `api_prompt_json` inputs.
- `/prompt` validates and queues the payload.
- Queue status and WebSocket messages inform progress UI.
- `/history/{prompt_id}` maps completed work to output files.
- `/view` fetches output files for display or download.
- `/upload/image` places user-provided images into ComfyUI-controlled storage for input nodes.
- `/object_info` helps an app inspect node classes and input contracts.

## Common confusion points

- Normal workflow save is not always the same as API export.
- Cloud API examples use cloud endpoints and API keys; local API examples normally use `127.0.0.1:8188` and local routes.
- Batch size inside a workflow is not the same as submitting multiple jobs.
- A user-facing app should not expose arbitrary node IDs unless it is an expert tool.
