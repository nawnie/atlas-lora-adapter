# Vol. 1 Scope — Gradio UI Research

## In scope

1. **Core Gradio abstractions**
   - `gr.Interface` for simple function-to-UI demos.
   - `gr.Blocks` for custom layouts, event chains, tabs, and multi-step tools.
   - `gr.ChatInterface` and `gr.Chatbot` for LLM/chat workflows.

2. **Component strategy**
   - image upload/edit/display
   - video upload/display
   - audio input/output
   - file upload/download
   - dataframe/table review
   - gallery and comparison displays
   - sliders, dropdowns, checkboxes, radios, buttons
   - logs, markdown, warnings, status outputs

3. **AIWF app patterns**
   - inpainting UI shell
   - RAG research assistant shell
   - ComfyUI workflow runner shell
   - Ollama/local LLM selector shell
   - model-folder inspector shell
   - dataset QA/caption review shell
   - video pipeline lesson builder shell

4. **Operational design**
   - queueing for long tasks
   - separating UI callbacks from model/service logic
   - safe launch defaults
   - LAN/phone access
   - user-configurable settings tabs
   - restart/relaunch patterns for backend settings changes
   - logging and flagging review data

5. **RAG guidance**
   - chunk Gradio docs by abstraction, component, event pattern, and deployment/security warning.
   - preserve version metadata because Gradio changes quickly.

## Out of scope for Vol. 1

- Complete Gradio API reference duplication.
- Custom Gradio component development in Svelte/JS.
- Hugging Face Spaces deployment as the primary target.
- Full React/Electron production app architecture.
- Cloud auth, enterprise SSO, Kubernetes, or multi-tenant hosting.

## Vol. 1 success criteria

This lane is Vol. 1-ready when the RAG can answer:

- Should this app use Interface, Blocks, or ChatInterface?
- How should an AIWF Gradio app handle long-running model generation?
- How should image/video/file components be wired for AI workflows?
- What are the common state and filesystem safety mistakes?
- How should Gradio fit beside ComfyUI, Ollama, and workflow JSON tools?
