# ComfyUI Workflow API Automation and Gradio Bridge Patterns

This lane teaches an AI assistant how to help users run ComfyUI workflows from code and from simple application UIs such as Gradio.

The lane focuses on the practical boundary between ComfyUI as a visual workflow editor and ComfyUI as a local execution server. It covers prompt submission, API-format JSON, queue handling, output retrieval, image upload, progress reporting, Gradio queue control, session state, and safe error surfacing.

## Canonical use

Use this lane when the user asks how to:

- run ComfyUI from Python, Gradio, or another application
- convert a workflow into an API payload
- expose a few workflow settings as app controls
- poll a queued job and fetch outputs
- upload input images into a ComfyUI workflow
- build a local Gradio UI over ComfyUI
- handle queue, progress, errors, and session state
- distinguish local ComfyUI API from ComfyUI Cloud API

## Source confidence

This lane is based on official ComfyUI documentation, the official ComfyUI script example, and official Gradio documentation. It should be treated as fast-moving implementation knowledge and rechecked when ComfyUI or Gradio changes major versions.
