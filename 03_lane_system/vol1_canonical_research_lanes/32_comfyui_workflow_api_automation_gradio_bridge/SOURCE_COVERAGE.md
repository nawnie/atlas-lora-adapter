# Source Coverage — ComfyUI Workflow API Automation and Gradio Bridge Patterns

## Covered by official sources

- ComfyUI server route behavior and route names
- ComfyUI workflow JSON schema
- ComfyUI API prompt example script
- ComfyUI Cloud API endpoint distinction and async job pattern
- Gradio Blocks queue controls
- Gradio queuing and concurrency controls
- Gradio state classes
- Gradio file upload event listeners

## Confidence

The core behavior is `official_docs_verified` or `official_repo_verified`. Third-party examples should be used only as supplemental implementation references.

## Recheck triggers

Recheck sources when:

- ComfyUI changes local route names or API prompt format
- ComfyUI Desktop changes API export behavior
- Gradio changes queue or state APIs
- a hosted ComfyUI platform is used instead of local ComfyUI
