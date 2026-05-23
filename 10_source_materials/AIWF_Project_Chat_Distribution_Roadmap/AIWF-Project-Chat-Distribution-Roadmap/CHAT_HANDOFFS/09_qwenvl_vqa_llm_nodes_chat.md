# Handoff — QwenVL / VQA / LLM Nodes Chat

## Chat Mission

Research and stabilize the AIWF path for QwenVL/VQA/LLM use inside ComfyUI.

## Initial Location

```text
AIWF-Labs/qwenvl-vqa/
```

## Stable Node Location Later

```text
AIWF-ComfyUI-Nodes/
```

## Scope Firewall / Memory Rule

This chat owns only this roadmap.

- Store **this chat's assigned roadmap** as the active working memory/context for this chat.
- Treat all other project roadmaps as **read-only reference** only.
- Do **not** begin work on another project's files, repo, roadmap, features, or implementation unless the Brand Hub explicitly reassigns scope.
- Do **not** casually suggest changes for other projects in normal chat, `.txt` files, or side notes.
- If a cross-project dependency or concern is unavoidable, write it only as a Markdown handoff note in a fenced code block, titled `CROSS_PROJECT_NOTE.md`, and send it back to Brand Hub / Release Packaging for routing.
- When uncertain, stay in lane and produce the next GitHub-ready file for this project.

## Owns

- QwenVL / VQA node research
- GGUF loading behavior
- llama.cpp constraints
- model preset design
- VQA model access options
- local LLM callback strategy
- comparison to Ollama / AnythingLLM / existing ComfyUI LLM nodes

## Does Not Own

- EnvPack beta
- Field Manual content
- broad AI assistant product
- unstable code in public node pack

## Existing Projects to Check

Before building:

- ComfyUI LLM nodes
- Ollama nodes
- llama-cpp-python behavior
- Qwen2.5-VL GGUF support
- Hugging Face model cards
- existing VQA nodes
- AnythingLLM/OpenWebUI integrations

## Key Concern

Model loading must be handled correctly. Avoid repeatedly loading large models per node execution if a reusable backend/session can be used.

## Next GitHub-Ready Outputs

1. `AIWF-Labs/qwenvl-vqa/README.md`
2. `research/existing_nodes.md`
3. `presets/qwenvl_presets.json`
4. `docs/model_loading_notes.md`
5. decision: Labs only or promote to `AIWF-ComfyUI-Nodes`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns QwenVL / VQA / LLM node research.

Initial location: AIWF-Labs/qwenvl-vqa/
Stable node location later: AIWF-ComfyUI-Nodes/

Mission: evaluate existing ComfyUI LLM/VQA/QwenVL options, decide whether to use, wrap, or build missing pieces, and design model-loading-safe presets and node behavior.

Do not push unstable code into the public node pack. Do not own EnvPack, Field Manual, or workflow packs.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check ComfyUI LLM nodes, Ollama nodes, llama-cpp-python, Qwen2.5-VL GGUF support, Hugging Face, AnythingLLM, and OpenWebUI.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Model loading behavior is the main risk.
- Prefer PowerShell setup notes for Windows.

Next outputs:
README.md, research/existing_nodes.md, presets/qwenvl_presets.json, docs/model_loading_notes.md, promotion decision
```
