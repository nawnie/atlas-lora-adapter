# Embedding and Chunking Strategy — ComfyUI Workflow API Automation and Gradio Bridge Patterns

## Chunk as procedures, not broad essays

This lane should be chunked into small task procedures because users usually ask how to do one concrete action:

- queue a prompt
- edit a prompt field
- upload an image
- fetch outputs
- show progress
- build a Gradio wrapper
- debug a validation error

## Required co-retrieval

When answering from this lane, retrieve together:

1. the canonical overview
2. the relevant Atlas card
3. source anchors
4. the API automation pattern guide
5. the Gradio bridge pattern guide if the user mentions UI/app/front end

## Preserve exact strings

Endpoint names, JSON keys, and ComfyUI node keys are high-precision tokens. Do not paraphrase these:

- `/prompt`
- `/history/{prompt_id}`
- `/view`
- `/upload/image`
- `/queue`
- `/object_info`
- `class_type`
- `inputs`
- `prompt_id`

## Freshness policy

Treat this lane as fast-moving. Recheck official ComfyUI and Gradio docs when giving release-sensitive implementation advice.
