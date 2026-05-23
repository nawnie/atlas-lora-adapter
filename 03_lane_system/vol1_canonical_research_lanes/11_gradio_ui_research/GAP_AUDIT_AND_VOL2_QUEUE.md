# Gap Audit and Vol. 2 Queue — Gradio UI Research

## Vol. 1 completed

- Added Gradio as a distinct AIWF research lane.
- Defined Interface vs Blocks vs ChatInterface decision rules.
- Added AIWF app patterns for inpainting, workflow running, RAG, dataset QA, and model management.
- Added state, queue, filesystem, share-link, and beginner-UX warnings.
- Added Atlas cards and QA prompts.

## Vol. 2 research queue

1. **Hands-on app templates**
   - `template_blocks_inpaint_app.py`
   - `template_blocks_comfyui_runner.py`
   - `template_chat_rag_app.py`
   - `template_dataset_caption_qa.py`
   - `template_model_folder_inspector.py`

2. **Security hardening pass**
   - exact `launch()` parameters
   - LAN vs localhost settings
   - auth options
   - file access allowlists
   - safe output directories

3. **Version-specific API audit**
   - Gradio 5.x stable behavior
   - Gradio 6.x/main behavior if needed
   - deprecated parameters and migration notes

4. **ComfyUI bridge implementation**
   - call ComfyUI `/prompt` API
   - discover workflow inputs
   - map Gradio controls to workflow JSON fields
   - display queue/run status
   - collect outputs

5. **Ollama/RAG bridge implementation**
   - model selector
   - context window selector
   - retrieval source selector
   - cite retrieved chunks
   - save flagged conversations

6. **Phone-friendly UI patterns**
   - mobile layout constraints
   - large buttons
   - small-screen settings collapse
   - LAN setup instructions

7. **Custom component research**
   - whether ImageEditor is enough for mask painting
   - when a custom canvas component is needed
   - compare Gradio built-ins to React canvas for advanced inpainting

## Open questions

- Should AIWF standardize on Gradio for all beginner app shells, or use Gradio for prototypes and a separate launcher for production?
- Should each AIWF Gradio app run in its own venv to avoid dependency conflicts?
- What is the cleanest plugin/addon model for Gradio apps similar to A1111/ComfyUI extensions?
- How much app state should be stored in JSON files versus Gradio session state?
