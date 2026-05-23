# AI Without Fear — Project Chat Distribution Roadmap


## Scope and Memory Control

Before sending any project handoff, send `SENDOFF_MASTER.md` first.

Each chat should:

- store only its assigned roadmap as active memory/context
- treat every other roadmap as read-only reference
- avoid making normal-chat suggestions for other projects
- avoid `.txt` suggestion files entirely
- use `CROSS_PROJECT_NOTE.md` in a fenced Markdown code block if a dependency must be routed
- return to its assigned lane immediately after the note

This prevents project drift across multiple AI agents and platforms.

## AI Field Guide Production Note

The Field Guide / Field Manual lane may use 8 working agents: 4 on GPT-side workflows and 4 on Grok-side workflows, with Claude used as the final editorial pass.

Volume II is parked as the future **Training AI** volume. Do not actively expand it until 3.5 training becomes practical enough to document seriously.


This roadmap is for distributing work across the individual project chats inside the GitHub project.

The goal is to stop every chat from trying to become the whole brand. Each chat should own one lane, produce GitHub-ready files, and connect back to the AIWF umbrella.

## Parent Brand Rule

**AI Without Fear / AIWF is the umbrella.**

AIWF is not one script, one ComfyUI workflow, or one PDF. It is a practical local-AI ecosystem built around this promise:

> Learn local AI. Fix your setup. Build real workflows.

Core philosophy:

> Master principles, not platforms. Tools change. Principles transfer.

## Standing Rules for Every Project Chat

1. **Do not reinvent the wheel.**
   - Before building, check whether ComfyUI, ComfyUI-Manager, ComfyUI-Doctor, MTB, Hugging Face, Civitai, GitHub repos, or existing node packs already cover the scope.
   - If something exists, decide whether to use it, wrap it, document it, or build only the missing piece.

2. **Keep each chat in its lane.**
   - Brand chat handles brand architecture.
   - EnvPack chat handles diagnostic/reporting beta.
   - Model Checker chat handles model scan/sort/report logic.
   - Workflow Pack chat handles ComfyUI workflow JSONs.
   - Field Manual chat handles docs, knowledge, and educational assets.
   - Labs chat handles unstable experiments.

3. **Write files, do not only discuss code.**
   - Each pass should produce or update actual repo-ready files when appropriate.
   - Keep GitHub load format: `README.md`, `CHANGELOG.md`, `docs/`, `examples/`, `workflows/`, `scripts/`, etc.

4. **Changelogs use days only.**
   - No timestamps.
   - Example: `## 2026-05-15`

5. **Prefer Windows PowerShell commands.**
   - Especially for ComfyUI, venv, install, patch, and troubleshooting workflows.

6. **One-click install is a first-class goal.**
   - Every public repo should move toward a simple install path:
     - `install.ps1`
     - `run.ps1`
     - clear README command
     - predictable folder layout

7. **All ComfyUI custom nodes should live under the AI Without Fear node pack.**
   - Default node-pack repo target:
     - `AIWF-ComfyUI-Nodes`
   - This makes it easy to go from one node to node packs later.

8. **Keep experimental work separate from beta work.**
   - Beta repos should be stable and narrow.
   - Labs repos can be messy and exploratory.

## Project Map

| Chat / Workstream | Repo Target | Status | Priority |
|---|---|---:|---:|
| Brand Hub | `nawnie/AI-Without-Fear` | Needed | High |
| EnvPack / Workstation Validator | `nawnie/AIWF-EnvPack` | Closest beta | Highest |
| Model Checker / Sorter | module inside `AIWF-EnvPack` first | Active | High |
| Field Manual | `nawnie/AI-Field-Manual-2026` | Content flagship | High |
| Knowledge Pack / Assistant Layer | inside Field Manual first, later separate | Prototype | Medium |
| Workflow Packs | `nawnie/AIWF-Workflow-Packs` | Active | High |
| ComfyUI Nodes | `nawnie/AIWF-ComfyUI-Nodes` | Needed | High |
| Old Photo Restore Pack | under Workflow Packs + Nodes if needed | Active | Medium |
| QwenVL / VQA / LLM Nodes | under Nodes or Labs first | Active research | Medium |
| AIWF Photos | future app repo | Concept | Later |
| Labs / Preservation Bridge | `nawnie/AIWF-Labs` | Experimental | Later |

## Release Sequence

### Phase 0 — Alignment

Create this shared structure in every chat:

- What this chat owns
- What this chat does not own
- Current repo target
- Current beta target
- Known dependencies
- Existing projects to check before building
- Next three file outputs

### Phase 1 — Brand Hub

Repo:

```text
nawnie/AI-Without-Fear
```

Ship:

```text
README.md
BRAND.md
ROADMAP.md
REPOS.md
CHANGELOG.md
```

Purpose:

The landing repo explains AIWF and routes people to the correct child repo.

### Phase 2 — First Beta: EnvPack

Repo:

```text
nawnie/AIWF-EnvPack
```

Beta target:

```text
v0.1-beta
```

Scope:

Report only. No auto-fix in v0.1.

Minimum beta features:

- System summary
- GPU / VRAM report
- Python / venv report
- Torch / CUDA report
- ComfyUI path detection
- `custom_nodes` inventory
- `extra_model_paths.yaml` reader
- recent `comfyui.log` tail
- model folder sanity report
- duplicate model scan
- Markdown report export
- JSON report export
- PowerShell run script

### Phase 3 — Model Checker Module

Keep inside `AIWF-EnvPack` at first.

Scope:

- detect model types
- detect bad placement
- detect duplicates
- inspect safetensors headers
- dry-run report
- optional move/copy only after beta

Do not turn it into a separate repo until the EnvPack repo is stable.

### Phase 4 — Field Manual + Knowledge Pack

Repo:

```text
nawnie/AI-Field-Manual-2026
```

Scope:

- PDF
- markdown chapters
- assets
- knowledge pack
- examples
- citation/credits
- release notes

This is the proof-of-knowledge repo and should link back to AIWF tools.

### Phase 5 — Workflow Packs

Repo:

```text
nawnie/AIWF-Workflow-Packs
```

Scope:

- ComfyUI workflow JSONs
- screenshots
- install notes
- model requirements
- troubleshooting
- workflow changelogs

Each workflow gets its own folder and README.

### Phase 6 — ComfyUI Nodes

Repo:

```text
nawnie/AIWF-ComfyUI-Nodes
```

Scope:

- AWF helper nodes
- tooltip/knowledge nodes
- workflow UI helper nodes
- diagnostic display nodes
- VQA helper nodes if stable

Rule:

Do not scatter AIWF nodes across random repos. All custom nodes should land here unless they are still in Labs.

### Phase 7 — Labs

Repo:

```text
nawnie/AIWF-Labs
```

Scope:

- A1111 Preservation Bridge
- node converter experiments
- experimental LLM nodes
- unstable router/subgraph experiments
- proof-of-concept code

Labs can be messy. Public beta repos should not be.

## Shared Folder Convention

For GitHub repos:

```text
README.md
CHANGELOG.md
LICENSE
docs/
examples/
scripts/
tests/
```

For ComfyUI workflow packs:

```text
README.md
CHANGELOG.md
workflow.json
models_needed.md
install_notes.md
known_issues.md
screenshots/
```

For node packs:

```text
README.md
CHANGELOG.md
pyproject.toml
requirements.txt
__init__.py
nodes.py
docs/
examples/
web/
```

## Immediate Next Moves

1. Use the handoff files in `CHAT_HANDOFFS/` to seed each project chat.
2. Keep the active beta chat focused on `AIWF-EnvPack`.
3. Combine projects only after each chat produces clean repo-ready files.
4. Do not let workflow JSON work block EnvPack beta.
5. Do not let Labs experiments contaminate beta releases.
