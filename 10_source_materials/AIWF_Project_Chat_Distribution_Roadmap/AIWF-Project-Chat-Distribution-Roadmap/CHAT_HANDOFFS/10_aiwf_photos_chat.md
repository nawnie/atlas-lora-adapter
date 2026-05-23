# Handoff — AIWF Photos Chat

## Chat Mission

Plan the future local-first AIWF Photos app without distracting from the first beta.

## Future Repo Target

```text
nawnie/AIWF-Photos
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

- local-first photo manager concept
- automatic person clustering
- privacy-first design
- folder/index strategy
- app architecture
- import/export design
- future roadmap

## Does Not Own

- EnvPack beta
- ComfyUI workflow packs
- Field Manual editing
- ComfyUI custom node pack

## Existing Projects to Check

Before building:

- Immich
- PhotoPrism
- Ente
- LibrePhotos
- local face clustering libraries
- CLIP/image embedding tools
- SQLite/DuckDB indexing patterns

## Priority Rule

This is later-stage. Do not let it block EnvPack or the brand hub.

## Next GitHub-Ready Outputs

1. `README.md` concept draft
2. `docs/ARCHITECTURE.md`
3. `docs/PRIVACY_MODEL.md`
4. `docs/EXISTING_PROJECTS_REVIEW.md`
5. `ROADMAP.md`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns future AIWF Photos planning only.

Future repo target: nawnie/AIWF-Photos

Mission: plan a local-first Google Photos alternative with automatic person clustering, privacy-first indexing, and practical export/import design.

Do not let this block AIWF EnvPack, the brand hub, workflow packs, or Field Manual work.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check Immich, PhotoPrism, Ente, LibrePhotos, local face clustering libraries, CLIP/image embeddings, and SQLite/DuckDB indexing patterns.
- Write actual GitHub-ready planning files.
- Changelog uses days only, no timestamps.
- Keep it local-first and privacy-first.
- Treat this as future product planning, not first beta.

Next outputs:
README.md, docs/ARCHITECTURE.md, docs/PRIVACY_MODEL.md, docs/EXISTING_PROJECTS_REVIEW.md, ROADMAP.md
```
