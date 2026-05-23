# QA Test Prompts — Gradio UI Research

Use these prompts to test whether the RAG understands Gradio as an AIWF UI layer.

## Interface vs Blocks

1. I have one Python function that takes an image and returns a caption. Should I use Interface or Blocks?
2. I need tabs for inpaint, upscale, settings, logs, and model paths. Should I use Interface or Blocks?
3. I want a local chatbot with model selector and retrieved source chunks. Should I use ChatInterface or Blocks?

## Local AI workflow design

4. Design a beginner Gradio UI for a ComfyUI workflow runner.
5. Design a Gradio inpainting canvas app that can send masks to a backend script.
6. Design a Gradio dataset caption QA tool for LoRA training images.
7. Design a Gradio app that lets users choose an Ollama model, prompt template, and RAG source.

## Safety and operations

8. What Gradio settings are risky when exposing the app over LAN or share link?
9. How should a Gradio app avoid leaking files from the user's model folders?
10. What state should be global, session, browser-local, or stored in a config file?
11. How should long-running generation jobs report progress and errors?

## Integration

12. How should Gradio call ComfyUI without hardcoding all workflow inputs?
13. How should Gradio store run manifests so outputs can be audited later?
14. How should Gradio support one-click install and beginner settings without hiding logs?

## Bad-answer detection

Reject answers that:

- claim Gradio is only for toy demos;
- recommend `share=True` casually for private local model tools;
- put user-specific state in global variables;
- merge UI, model loading, file mutation, and business logic into one callback;
- ignore queue/progress for long-running jobs;
- suggest replacing ComfyUI graphs with Gradio instead of using Gradio as a wrapper/control panel.
