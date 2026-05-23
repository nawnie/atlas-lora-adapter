# AIWF — Project Chat Map

Use this to decide which chat owns which work.

## 01 — Brand Hub Chat

Owns:

- AIWF parent identity
- brand promise
- repo routing
- visual/naming standards
- top-level README

Does not own:

- tool implementation
- workflow JSON details
- model checker logic

Primary repo:

```text
nawnie/AI-Without-Fear
```

## 02 — EnvPack / Workstation Validator Chat

Owns:

- first GitHub beta
- workstation/environment reporting
- ComfyUI diagnostic report
- PowerShell one-click run path
- markdown/json support bundle

Does not own:

- workflow generation
- custom image workflows
- Field Manual editing

Primary repo:

```text
nawnie/AIWF-EnvPack
```

## 03 — Model Checker Chat

Owns:

- model path scanning
- duplicate detection
- bad placement detection
- safetensors metadata inspection
- dry-run reports

Does not own:

- full EnvPack UI
- ComfyUI workflow design
- model downloading, except docs/scripts later

Primary location:

```text
AIWF-EnvPack/awf_model_checker/
```

## 04 — Field Manual Chat

Owns:

- book/PDF
- markdown chapter cleanup
- docs site content
- educational explanations
- glossary
- examples from the manual

Does not own:

- beta code
- unstable experiments
- ComfyUI custom node implementation

Primary repo:

```text
nawnie/AI-Field-Manual-2026
```

## 05 — Knowledge Pack / Assistant Chat

Owns:

- `ai_knowledge.json`
- RAG-ready AIWF knowledge
- failure-pattern cards
- recipes
- assistant prompts
- local helper behavior

Does not own:

- model hosting
- unrelated chatbot products
- unstable node code

Initial location:

```text
AI-Field-Manual-2026/knowledge/
```

Possible later repo:

```text
nawnie/AIWF-Knowledge-Pack
```

## 06 — Workflow Packs Chat

Owns:

- ComfyUI workflow JSONs
- workflow README files
- install notes
- model requirement docs
- screenshots
- workflow changelogs

Does not own:

- custom node source code unless required
- EnvPack diagnostics
- Field Manual writing

Primary repo:

```text
nawnie/AIWF-Workflow-Packs
```

## 07 — ComfyUI Nodes Chat

Owns:

- AIWF custom node pack
- nodes.py
- helper nodes
- tooltip nodes
- VQA helper nodes once stable
- node packaging

Does not own:

- unrelated workflow JSONs
- broad brand docs
- unstable experiments

Primary repo:

```text
nawnie/AIWF-ComfyUI-Nodes
```

## 08 — Old Photo Restore Chat

Owns:

- old-photo restore workflow
- model options for restoration
- ReActor / face restore path notes
- inpaint/upscale restore flow
- user-facing workflow README

Belongs under:

```text
AIWF-Workflow-Packs/old-photo-restore/
```

Node code, if needed, belongs under:

```text
AIWF-ComfyUI-Nodes/
```

## 09 — QwenVL / VQA / LLM Nodes Chat

Owns:

- QwenVL / VQA ComfyUI node research
- model loading behavior
- presets
- GGUF / llama.cpp constraints
- model access options
- comparison to Ollama / AnythingLLM / existing nodes

Initial location:

```text
AIWF-Labs/qwenvl-vqa/
```

Stable node location later:

```text
AIWF-ComfyUI-Nodes/
```

## 10 — AIWF Photos Chat

Owns:

- local-first Google Photos alternative concept
- person clustering
- folder/index architecture
- privacy-first photo handling
- future app planning

Primary repo later:

```text
nawnie/AIWF-Photos
```

Do not prioritize until EnvPack and core brand are stable.

## 11 — Labs / Preservation Bridge Chat

Owns:

- A1111 Preservation Bridge
- A1111 extension-to-ComfyUI analysis
- node converter experiments
- router shell prototypes
- risky or unstable experiments

Primary repo:

```text
nawnie/AIWF-Labs
```

Rule:

Labs can explore. Labs should not define public beta promises.


## Global Chat Behavior Rule

Each chat owns only its assigned lane. It may read other roadmaps only for context.

When handing off to a chat:

1. Send `SENDOFF_MASTER.md`.
2. Send that chat's handoff file.
3. Tell the chat to store only that roadmap as active memory/context.
4. Keep all other roadmaps as reference-only.

Cross-project notes must be Markdown-only and routed back to Brand Hub / Release Packaging.
