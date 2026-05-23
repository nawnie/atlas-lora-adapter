# Handoff — EnvPack / Workstation Validator Chat

## Chat Mission

Ship the first real AIWF GitHub beta.

## Repo Target

```text
nawnie/AIWF-EnvPack
```

## Beta Target

```text
v0.1-beta
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

- AI workstation diagnostic report
- ComfyUI environment report
- GPU / VRAM / CUDA / Torch checks
- Python / venv detection
- ComfyUI path detection
- custom node inventory
- `extra_model_paths.yaml` reading
- log tailing and error detection
- markdown and JSON report output
- PowerShell one-command run path

## Does Not Own

- Workflow JSON creation
- Field Manual editing
- broad brand architecture
- unstable Labs experiments
- automatic fixes in v0.1

## Existing Projects to Check

Before building features, compare against:

- ComfyUI-Manager
- ComfyUI-Doctor
- MTB `/mtb`
- Python `torch.utils.collect_env`
- `nvidia-smi`
- existing local-AI diagnostic scripts on GitHub

AIWF EnvPack should not replace those. It should package the whole support context into one clean report.

## v0.1-beta Rule

Report only.

No destructive moves. No automatic repair. No model moving. No dependency changes.

## Next GitHub-Ready Outputs

1. `README.md`
2. `CHANGELOG.md`
3. `install.ps1`
4. `run_envpack.ps1`
5. `awf_envpack.py`
6. `examples/example_report.md`
7. `docs/KNOWN_LIMITATIONS.md`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns AIWF EnvPack / Workstation Validator, the first GitHub beta.

Repo target: nawnie/AIWF-EnvPack
Beta target: v0.1-beta

Mission: create a one-command Windows/PowerShell tool that generates a clean local-AI support report showing GPU, CUDA, Torch, Python, venv, ComfyUI, custom nodes, ports, logs, model folders, duplicates, and likely mismatches.

Do not implement workflow packs, Field Manual content, or Labs experiments here.

v0.1-beta is report-only. No auto-fix.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; compare against ComfyUI-Manager, ComfyUI-Doctor, MTB, torch collect_env, and nvidia-smi.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Prefer PowerShell commands.
- Keep one-click install in mind.

Next outputs:
README.md, CHANGELOG.md, install.ps1, run_envpack.ps1, awf_envpack.py, examples/example_report.md, docs/KNOWN_LIMITATIONS.md
```
