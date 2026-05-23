# Handoff — Old Photo Restore Chat

## Chat Mission

Package the old-photo restoration workflow into a clean AIWF workflow pack.

## Primary Location

```text
AIWF-Workflow-Packs/old-photo-restore/
```

## Node Code Location If Needed

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

- old photo restore workflow JSON
- restoration model options
- face restore path notes
- inpaint/upscale flow
- workflow README
- model requirements
- install notes
- known quality limitations

## Does Not Own

- general workflow pack repo architecture
- EnvPack diagnostics
- broad ComfyUI node pack implementation
- unrelated image workflows

## Existing Projects to Check

Before building:

- CodeFormer
- GFPGAN
- RestoreFormer
- Real-ESRGAN
- SUPIR / newer restore workflows
- ReActor restore options
- ComfyUI restore/upscale nodes
- old photo restoration workflows on GitHub/Civitai

## Next GitHub-Ready Outputs

1. `old-photo-restore/README.md`
2. `old-photo-restore/workflow.json`
3. `old-photo-restore/models_needed.md`
4. `old-photo-restore/install_notes.md`
5. `old-photo-restore/known_issues.md`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns the Old Photo Restore workflow pack.

Primary location: AIWF-Workflow-Packs/old-photo-restore/

Mission: package a clean ComfyUI old-photo restoration workflow with model requirements, install notes, known issues, and restoration options.

Do not own the general workflow repo, EnvPack diagnostics, or broad node-pack implementation. If custom nodes are needed, hand that off to AIWF-ComfyUI-Nodes.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check CodeFormer, GFPGAN, RestoreFormer, Real-ESRGAN, SUPIR, ReActor, ComfyUI restore nodes, GitHub, and Civitai first.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Prefer PowerShell install notes.
- Keep output portable and avoid hardcoded local paths.

Next outputs:
old-photo-restore/README.md, workflow.json, models_needed.md, install_notes.md, known_issues.md
```
