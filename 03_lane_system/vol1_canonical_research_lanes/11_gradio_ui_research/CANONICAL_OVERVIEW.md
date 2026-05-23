# Canonical Overview — Gradio UI Research

## Core position

Gradio is a Python-first web UI framework for AI demos, local tools, and lightweight data applications. Its value for AI Without Fear is not that it is the most powerful frontend technology; its value is that it lets a Python tool become a usable browser app quickly, with enough components for images, masks, video, audio, files, tables, chat, and review workflows.

## Decision model

### Use `gr.Interface` when

- one Python function maps cleanly to fixed inputs and outputs;
- the app is a demo, smoke test, benchmark, or small utility;
- the UI needs to be made quickly and does not require complex routing;
- flagging examples is useful for collecting test cases.

### Use `gr.Blocks` when

- the UI has tabs, rows, columns, accordions, settings, logs, multiple buttons, or chained events;
- one action should update several outputs;
- the app needs image masking, gallery comparison, model selectors, staged workflow control, or background logs;
- callbacks must be composed into a real tool rather than a single demo function.

### Use `gr.ChatInterface` / `gr.Chatbot` when

- the primary interaction is conversational;
- the app is a local LLM, Atlas assistant, research copilot, workflow helper, or guided tutor;
- the conversation history is part of the user experience.

## AIWF-specific stance

For AIWF, default to **Blocks** for real tools and **Interface** for smoke tests. Blocks is the best match for beginner-friendly local AI apps because it supports visible settings, logs, status panels, tabs, and multi-step workflows while staying entirely in Python.

## Recommended Gradio architecture for local AI tools

Use a three-layer split:

1. **UI layer**
   - Gradio components, layout, labels, help text, and event wiring.

2. **Service layer**
   - Python functions that call ComfyUI API, Ollama, local models, file scanners, RAG retrievers, or workflow tools.

3. **State/config layer**
   - JSON/YAML settings, model paths, launch arguments, user preferences, logs, and result manifests.

Do not put model loading, file mutation, UI layout, and business rules into one callback. That becomes impossible to debug and hard for a beginner to modify.

## Common AIWF Gradio app shells

### 1. Inpainting shell

Inputs: source image, mask/canvas image, prompt, negative prompt, model preset, denoise, seed, crop/stitch settings.
Outputs: result image, comparison gallery, workflow JSON preview, log panel.

### 2. Workflow runner shell

Inputs: workflow JSON file, image assets, model preset, seed, output folder, launch profile.
Outputs: run status, generated files, error log, missing-node/model report.

### 3. RAG research shell

Inputs: question, source selector, retrieval mode, max context, answer style.
Outputs: answer, cited chunks, retrieval diagnostics, gap notes.

### 4. Dataset QA shell

Inputs: image folder, caption folder, metadata CSV/JSONL, filters.
Outputs: image gallery, caption editor, rejected/approved status, export manifest.

### 5. Local model manager shell

Inputs: model folder, scan mode, duplicate/hash options.
Outputs: sortable table, warnings, move/copy plan, PowerShell command preview.

## State model

- **Global state** is shared between all users and is only appropriate for app-wide counters, cached model objects, or service clients.
- **Session state** is per user/browser session and should hold temporary chat history, selected files, run IDs, or UI selections.
- **Browser/local state** can preserve user preferences but should not hold secrets.

The biggest beginner mistake is accidentally putting user-specific data in global Python variables. In local single-user mode that often works; in LAN/shared mode it leaks state between users.

## Long-running generation

AI generation jobs can run for seconds to minutes. Gradio apps should expose progress and use queue-friendly design. Avoid blocking the UI without status feedback. Prefer a visible status/log output and a run manifest that records input settings, output paths, errors, and timing.

## Security and filesystem defaults

Treat Gradio as a web app, even when local. Do not expose broad filesystem paths casually. Avoid `share=True` for private model tools unless the user understands that it creates a public tunnel. Prefer explicit allowlists for files, output directories, and model paths. Never store API keys or personal tokens in examples.

## Why Gradio belongs in the AIWF archive

AIWF repeatedly needs fast, beginner-friendly UIs for local AI workflows. ComfyUI is excellent for node graphs; Gradio is excellent for task apps built around those graphs. The correct relationship is not Gradio versus ComfyUI. It is Gradio as the beginner-facing control panel and ComfyUI/Ollama/RAG scripts as back-end engines.
