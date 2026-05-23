# Concept Map — Gradio UI Research

## Top-level concepts

- Gradio
  - Interface
- single function wrapper
- simple demos
- flagging
- examples
  - Blocks
- layout
- components
- events
- chained callbacks
- tabs/settings/log panels
  - ChatInterface / Chatbot
- message history
- streaming responses
- Atlas assistants
- local LLM shells
  - Components
- Image / ImageEditor / Gallery / ImageSlider
- Video / Audio
- File / UploadButton / FileExplorer
- Dataframe / JSON / Code
- Markdown / Textbox / Dropdown / Slider / Checkbox
  - Events
- click
- change
- submit
- load
- select
- clear/retry/undo/edit for chat-style interactions
  - State
- global state
- session state
- browser state
- model cache
- settings JSON
  - Runtime
- queue
- progress
- launch
- local host
- LAN access
- share links
- auth
- allowed paths / file access boundaries
  - Data capture
- flagging
- logs
- run manifests
- QA datasets
  - Integration targets
- ComfyUI API
- Ollama
- llama.cpp/vLLM backends
- RAG retrievers
- model scanners
- dataset/caption tools

## AIWF relationships

- Gradio + ComfyUI
  - Gradio provides beginner task UI.
  - ComfyUI provides graph execution engine.
  - Workflow JSON remains source of truth for node graphs.

- Gradio + Ollama/local LLM
  - Gradio provides model selector, chat panel, prompt settings, and logs.
  - Ollama provides model loading and generation endpoint.

- Gradio + RAG
  - Gradio provides source selector, query UI, retrieved chunk viewer, and feedback/flagging.
  - Retriever/vector DB provides evidence.

- Gradio + dataset tools
  - Gradio provides image/caption review UI.
  - Python scripts provide validation, transforms, and export.

## Failure relationships

- Global mutable state -> cross-user leakage.
- Long callback with no queue/progress -> app appears frozen.
- Broad file serving -> accidental exposure of private files.
- One giant callback -> impossible debugging.
- `share=True` without warning -> private local tool becomes internet-accessible.
- Component output mismatch -> confusing runtime errors.
- Returning unplayable video codec -> browser output fails or converts unexpectedly.
