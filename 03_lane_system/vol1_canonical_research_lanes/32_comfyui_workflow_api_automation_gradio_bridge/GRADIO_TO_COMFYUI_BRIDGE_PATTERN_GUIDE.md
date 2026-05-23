# Gradio Bridge Pattern Guide

## Recommended architecture

Use Gradio as a controlled front end and ComfyUI as the execution backend.

```text
User controls -> Gradio event -> workflow contract -> API payload mutation -> ComfyUI /prompt -> status tracking -> history/output retrieval -> Gradio output component
```

## Queue design

Use Gradio queue controls to avoid overdriving a single GPU. For one local ComfyUI backend, start with conservative concurrency:

```python
with gr.Blocks() as demo:
    generate = gr.Button("Generate")
    generate.click(run_workflow, inputs=[prompt, seed], outputs=[image, log], concurrency_limit=1)

demo.queue(max_size=8)
demo.launch()
```

Use a shared `concurrency_id` when several buttons all target the same ComfyUI backend.

## State design

- Use session state for each user's current prompt ID, selected workflow, and temporary output list.
- Avoid global mutable state for per-user files or prompt IDs.
- Use browser state only for user preferences that are safe to persist locally.

## Upload design

For image workflows:

1. accept a Gradio image or file input
2. save/copy it to a controlled temporary location
3. upload it to ComfyUI with `/upload/image` or place it through the approved input route
4. mutate the LoadImage or equivalent node input to reference the uploaded file
5. queue the prompt

Never pass arbitrary user filesystem paths into the payload.

## User-facing logs

A good beginner UI shows:

- backend connection check
- queued prompt ID
- queue position when available
- current progress or polling status
- output filename
- validation errors
- missing model or missing custom node messages

The log panel is part of the product. It keeps the app from feeling frozen during long generations.
