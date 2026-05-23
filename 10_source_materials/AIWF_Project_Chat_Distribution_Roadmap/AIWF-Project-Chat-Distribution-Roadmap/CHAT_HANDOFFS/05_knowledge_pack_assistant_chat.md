# Handoff — Knowledge Pack / Assistant Chat

## Chat Mission

Turn AIWF knowledge into a structured assistant/RAG layer.

## Initial Location

```text
AI-Field-Manual-2026/knowledge/
```

## Possible Future Repo

```text
nawnie/AIWF-Knowledge-Pack
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

- `ai_knowledge.json`
- AIWF concepts
- failure patterns
- recipes
- workflow guidance objects
- local assistant prompts
- tooltip/helper text
- RAG-ready chunks

## Does Not Own

- EnvPack code
- ComfyUI node implementation
- workflow JSONs
- broad brand layout

## Existing Projects to Check

Before building, check:

- current AIWF knowledge pack
- AnythingLLM format options
- OpenWebUI knowledge/RAG patterns
- ComfyUI tooltip node needs
- JSON schema conventions

## Next GitHub-Ready Outputs

1. `knowledge/ai_knowledge.json`
2. `knowledge/schema.md`
3. `knowledge/README.md`
4. `examples/assistant_prompt.md`
5. `CHANGELOG.md` update

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns the AIWF Knowledge Pack / Assistant layer.

Initial location: AI-Field-Manual-2026/knowledge/
Possible later repo: nawnie/AIWF-Knowledge-Pack

Mission: structure AIWF concepts, failure patterns, recipes, workflow guidance, and assistant prompts into a clean JSON/Markdown knowledge layer.

Do not implement EnvPack, workflow JSONs, or custom ComfyUI nodes here.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check AnythingLLM, OpenWebUI, RAG patterns, and current AIWF knowledge files.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Keep content practical, local-AI focused, and connected to the Field Manual.

Next outputs:
knowledge/ai_knowledge.json, knowledge/schema.md, knowledge/README.md, examples/assistant_prompt.md
```
