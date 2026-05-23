# Handoff — Brand Hub Chat

## Chat Mission

Build the parent AI Without Fear / AIWF brand hub.

## Repo Target

```text
nawnie/AI-Without-Fear
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

- Brand promise
- Naming standards
- Parent README
- Repo routing
- Product line map
- Public-facing roadmap
- Connection between Field Manual, EnvPack, Workflow Packs, Nodes, and Labs

## Does Not Own

- EnvPack code
- Model checker implementation
- Workflow JSON generation
- ComfyUI node implementation
- Labs experiments

## Existing Projects to Check

Before creating brand claims or repo links, check:

- existing AIWF repos
- current Field Manual repo structure
- EnvPack repo status
- Workflow Packs repo status
- GitHub owner namespace under `nawnie`

## Next GitHub-Ready Outputs

1. `README.md`
2. `BRAND.md`
3. `REPOS.md`
4. `ROADMAP.md`
5. `CHANGELOG.md`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns the parent brand hub only.

Repo target: nawnie/AI-Without-Fear

Mission: create the public landing repo for AIWF and route people to the correct child repos.

Do not implement EnvPack, model checker, workflow JSONs, or custom nodes here.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check whether existing projects already cover the scope.
- Write actual GitHub-ready files, not just ideas.
- Use changelog days only, no timestamps.
- Prefer PowerShell examples where commands are needed.
- Keep AIWF as the umbrella brand.

Next outputs:
README.md, BRAND.md, REPOS.md, ROADMAP.md, CHANGELOG.md
```
