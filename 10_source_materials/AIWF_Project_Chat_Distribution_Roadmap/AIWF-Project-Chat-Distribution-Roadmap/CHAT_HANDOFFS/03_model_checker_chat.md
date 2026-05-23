# Handoff — Model Checker / Sorter Chat

## Chat Mission

Build the model scan, placement, duplicate, and metadata logic that supports EnvPack.

## Primary Location

Start as a module inside:

```text
nawnie/AIWF-EnvPack
```

Suggested path:

```text
awf_model_checker/
```

Do not split into a separate repo until EnvPack is stable.

## Scope Firewall / Memory Rule

This chat owns only this roadmap.

- Store **this chat's assigned roadmap** as the active working memory/context for this chat.
- Treat all other project roadmaps as **read-only reference** only.
- Do **not** begin work on another project's files, repo, roadmap, features, or implementation unless the Brand Hub explicitly reassigns scope.
- Do **not** casually suggest changes for other projects in normal chat, `.txt` files, or side notes.
- If a cross-project dependency or concern is unavoidable, write it only as a Markdown handoff note in a fenced code block, titled `CROSS_PROJECT_NOTE.md`, and send it back to Brand Hub / Release Packaging for routing.
- When uncertain, stay in lane and produce the next GitHub-ready file for this project.

## Owns

- model folder scan
- model type detection
- duplicate detection
- bad placement warnings
- safetensors header inspection
- dry-run reports
- optional move/copy later, after report-only beta

## Does Not Own

- full EnvPack report UI
- custom ComfyUI nodes
- workflow JSONs
- model downloading, except future helper docs

## Existing Projects to Check

Before building, check:

- ComfyUI model folder conventions
- ComfyUI-Manager model management abilities
- Civitai metadata conventions
- safetensors metadata behavior
- existing duplicate-file scanner approaches
- Hugging Face cache layout

## v0.1 Rule

Report only.

No moving or deleting models during the first beta.

## Next GitHub-Ready Outputs

1. `awf_model_checker.py`
2. `docs/MODEL_CHECKER.md`
3. `examples/model_report.md`
4. `tests/test_model_classifier.py`
5. update parent `CHANGELOG.md`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns the Model Checker / Sorter module for AIWF EnvPack.

Primary location: AIWF-EnvPack/awf_model_checker/

Mission: scan ComfyUI model folders, detect likely model types, warn about bad placement, find duplicates, inspect safetensors headers, and produce a clean report.

Do not split this into a separate repo yet. Do not implement destructive moves in v0.1. Report only.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check ComfyUI conventions, ComfyUI-Manager, Civitai metadata, Hugging Face cache behavior, and safetensors metadata.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Prefer PowerShell examples.
- Keep output useful for support requests.

Next outputs:
awf_model_checker.py, docs/MODEL_CHECKER.md, examples/model_report.md, tests/test_model_classifier.py
```
