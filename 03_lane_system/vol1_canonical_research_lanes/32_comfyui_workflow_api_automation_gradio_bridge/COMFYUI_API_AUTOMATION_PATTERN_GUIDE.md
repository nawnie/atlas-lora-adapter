# API Automation Pattern Guide

## Core local execution flow

1. Prepare an API-format prompt payload.
2. Mutate only approved inputs by node ID and input key.
3. Submit the payload to local ComfyUI with `POST /prompt`.
4. Read the returned `prompt_id`.
5. Track status through WebSocket or by polling `/history/{prompt_id}` and `/queue`.
6. Retrieve generated files with `/view` after the output appears in history.
7. Surface validation errors and `node_errors` directly in the user-facing log.

## Safe payload mutation

Good app controls mutate known fields:

```python
prompt["6"]["inputs"]["text"] = positive_prompt
prompt["7"]["inputs"]["text"] = negative_prompt
prompt["3"]["inputs"]["seed"] = seed
prompt["5"]["inputs"]["width"] = width
prompt["5"]["inputs"]["height"] = height
```

Bad app controls allow arbitrary node deletion, arbitrary class changes, unvalidated file paths, or unchecked model names.

## Workflow contract

For a stable app, create a workflow contract:

```json
{
  "workflow_name": "sdxl_inpaint_basic",
  "api_payload_file": "workflows/sdxl_inpaint_basic_api.json",
  "allowed_inputs": [
    {"node_id": "6", "input": "text", "ui_name": "positive_prompt"},
    {"node_id": "7", "input": "text", "ui_name": "negative_prompt"},
    {"node_id": "3", "input": "seed", "ui_name": "seed"}
  ],
  "expected_outputs": [
    {"node_id": "9", "type": "image"}
  ]
}
```

The assistant should recommend workflow contracts when a user wants to turn workflows into repeatable apps.

## Error handling

If `/prompt` returns validation errors, do not pretend the job is queued. Show the error, node-level details, and the most likely fix:

- missing custom node
- missing model file
- invalid input type
- bad filename
- workflow not in API format
- stale node ID after editing the workflow
