# Handoff — ComfyUI Nodes Chat

## Chat Mission

Build the official AIWF custom node pack.

## Repo Target

```text
nawnie/AIWF-ComfyUI-Nodes
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

- AIWF custom node pack
- `nodes.py`
- `__init__.py`
- helper nodes
- tooltip/knowledge nodes
- workflow UI helper nodes
- VQA helper nodes when stable
- packaging and requirements

## Does Not Own

- workflow JSON library
- EnvPack standalone app logic
- Field Manual writing
- Labs-only experiments

## Standing Rule

All AIWF custom nodes go here unless they are experimental enough to remain in Labs.

## Existing Projects to Check

Before creating a node, check:

- ComfyUI built-in nodes
- ComfyUI custom node registry
- ComfyUI-Manager
- rgthree
- Easy-Use
- MTB
- existing VQA/QwenVL nodes
- relevant GitHub repos

## Repo Template

```text
AIWF-ComfyUI-Nodes/
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── pyproject.toml
├── __init__.py
├── nodes.py
├── web/
├── examples/
└── docs/
```

## Next GitHub-Ready Outputs

1. `README.md`
2. `__init__.py`
3. `nodes.py`
4. `requirements.txt`
5. `examples/basic_workflow.json`
6. `CHANGELOG.md`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns the official AIWF ComfyUI custom node pack.

Repo target: nawnie/AIWF-ComfyUI-Nodes

Mission: build and package AIWF custom nodes in one node pack so individual nodes can grow into a proper pack.

Do not scatter AIWF custom nodes across random repos. Do not own workflow JSON packs, EnvPack standalone diagnostics, or Field Manual writing here.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check ComfyUI built-ins, custom node registry, Manager, rgthree, Easy-Use, MTB, and existing VQA/QwenVL nodes first.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Prefer portable node design.
- Keep experimental nodes in Labs until stable.

Next outputs:
README.md, __init__.py, nodes.py, requirements.txt, examples/basic_workflow.json, CHANGELOG.md
```
