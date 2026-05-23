# Embedding and Chunking Strategy — Gradio UI Research

## Chunk types

Use typed chunks, not one flat Gradio blob.

### 1. Abstraction chunks

One chunk each for:

- `Interface`
- `Blocks`
- `ChatInterface`
- `Chatbot`
- `State`
- queue/progress
- flagging/logging
- launch/deployment/security

Recommended size: 500-900 tokens.
Metadata: `concept`, `api_surface`, `aiwf_use_case`, `risk_level`, `version_observed`.

### 2. Component chunks

Group components by workflow family:

- image/mask/gallery comparison
- video/audio
- files/folders/downloads
- tables/dataframes/JSON/code
- controls/settings/logs
- chat components

Recommended size: 400-800 tokens.
Preserve exact component names and return/input types.

### 3. Pattern chunks

Store app patterns as recipes:

- inpainting app shell
- ComfyUI workflow runner shell
- Atlas assistant shell
- dataset QA shell
- model manager shell
- video lesson generator shell

Recommended size: 600-1,000 tokens.
Metadata: `pattern_type`, `required_components`, `backend`, `failure_modes`.

### 4. Safety chunks

Keep launch, file access, share links, auth, state leakage, and secrets as separate high-priority chunks. These should retrieve for any question involving LAN, phone access, remote sharing, file upload, model folder scanning, or public demos.

### 5. Code skeleton chunks

Store code examples as small, complete patterns rather than excerpts. Include:

- minimal Interface app
- minimal Blocks app
- queue-friendly long task
- image input/output app
- chatbot/RAG shell
- settings tab pattern

Recommended size: one runnable code block per chunk with short explanation.

## Retrieval strategy

Use hybrid retrieval because Gradio queries often contain exact API names such as `Blocks`, `ChatInterface`, `State`, `queue`, `launch`, `share`, `allowed_paths`, `ImageEditor`, or `Video`. Dense-only retrieval may miss exact component/API matches.

## Metadata schema

Suggested metadata fields:

```json
{
  "lane_id": "RP11",
  "tool": "gradio",
  "doc_type": "concept|component|pattern|safety|code_skeleton|qa",
  "api_surface": "Interface|Blocks|ChatInterface|State|Component|Launch",
  "aiwf_use_case": "inpainting|rag|comfyui_runner|ollama_chat|dataset_qa|model_manager",
  "risk_level": "low|medium|high",
  "version_observed": "Gradio docs observed 2026-05"
}
```

## Do not embed blindly

Do not embed the entire Gradio API reference as one giant source. It will create shallow retrieval and bury the decision rules. Instead, embed the AIWF synthesis first and use official docs as exact references when needed.
