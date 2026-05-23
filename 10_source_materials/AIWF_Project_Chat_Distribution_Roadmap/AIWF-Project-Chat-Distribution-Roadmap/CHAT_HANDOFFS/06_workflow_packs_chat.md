# Handoff — Workflow Packs Chat

## Chat Mission

Package AIWF ComfyUI workflow JSONs into clean, installable workflow packs.

## Repo Target

```text
nawnie/AIWF-Workflow-Packs
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

- workflow JSONs
- workflow READMEs
- model requirement docs
- screenshots
- install notes
- known issues
- workflow changelogs
- subgraph/router workflow packaging

## Does Not Own

- EnvPack diagnostics
- Field Manual writing
- custom node source code, unless handed off to node chat
- unstable experiments that belong in Labs

## Existing Projects to Check

Before building a workflow, check:

- ComfyUI built-in nodes
- ComfyUI-Manager
- rgthree
- ComfyUI-Easy-Use
- VideoHelperSuite
- ReActor
- ComfyUI inpaint crop/stitch alternatives
- relevant GitHub workflow repos
- Civitai workflows

## Folder Template

```text
workflow-name/
├── README.md
├── CHANGELOG.md
├── workflow.json
├── models_needed.md
├── install_notes.md
├── known_issues.md
└── screenshots/
```

## Next GitHub-Ready Outputs

1. repo `README.md`
2. `old-photo-restore/README.md`
3. `old-photo-restore/workflow.json`
4. `router-shells/README.md`
5. `CHANGELOG.md`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns AIWF Workflow Packs.

Repo target: nawnie/AIWF-Workflow-Packs

Mission: package ComfyUI workflow JSONs into clean workflow packs with README files, model requirements, install notes, screenshots, known issues, and changelogs.

Do not implement EnvPack diagnostics, Field Manual content, or custom node source code here unless handing it off to AIWF-ComfyUI-Nodes.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check ComfyUI built-ins, Manager, rgthree, Easy-Use, VideoHelperSuite, ReActor, GitHub, and Civitai workflows before building.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Prefer PowerShell install notes.
- Keep workflows portable and avoid hardcoded local paths.

Next outputs:
repo README.md, old-photo-restore/README.md, old-photo-restore/workflow.json, router-shells/README.md, CHANGELOG.md
```
