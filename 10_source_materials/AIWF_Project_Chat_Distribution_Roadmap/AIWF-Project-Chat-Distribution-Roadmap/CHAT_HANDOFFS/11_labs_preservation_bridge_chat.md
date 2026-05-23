# Handoff — Labs / Preservation Bridge Chat

## Chat Mission

Explore unstable AIWF experiments without contaminating beta repos.

## Repo Target

```text
nawnie/AIWF-Labs
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

- A1111 Preservation Bridge
- A1111 extension-to-ComfyUI analysis
- extension classifier prototypes
- router shell prototypes
- node converter experiments
- risky helper scripts
- proof-of-concept code

## Does Not Own

- public beta promises
- stable node pack releases
- EnvPack v0.1
- Field Manual core content

## Existing Projects to Check

Before building:

- ComfyUI extension/node architecture
- A1111 extension APIs
- existing A1111-to-ComfyUI migration guides
- ComfyUI custom node examples
- Python AST/static analysis tools
- GitHub repos attempting similar conversion

## Labs Rule

Labs can be messy. Public repos cannot.

Do not promote a Labs project until it has:

- README
- known limitations
- dependency notes
- at least one working example
- clear reason it is not duplicating an existing project

## Next GitHub-Ready Outputs

1. `README.md`
2. `a1111-preservation-bridge/README.md`
3. `docs/EXISTING_PROJECTS_REVIEW.md`
4. `docs/RISK_REGISTER.md`
5. `examples/`

## Copy/Paste Starter Prompt

```text
You are working inside the AI Without Fear GitHub project. This chat owns Labs / Preservation Bridge experiments.

Repo target: nawnie/AIWF-Labs

Mission: explore unstable ideas like A1111 Preservation Bridge, extension-to-ComfyUI analysis, router shell prototypes, and node converter experiments.

Do not define public beta promises here. Do not push unstable work into AIWF-EnvPack or AIWF-ComfyUI-Nodes.

Scope and memory rules:
- Store this assigned roadmap as the active working memory/context for this chat.
- Treat other AIWF roadmaps as read-only reference only.
- Do not work on other project lanes unless Brand Hub explicitly reassigns scope.
- Do not make casual suggestions for other projects in normal chat or .txt files.
- If a cross-project note is unavoidable, output it only as Markdown inside a fenced code block titled CROSS_PROJECT_NOTE.md, then return to this project's assigned work.

Standing rules:
- Do not reinvent the wheel; check ComfyUI architecture, A1111 extension APIs, migration guides, AST/static analysis tools, and GitHub repos first.
- Write actual GitHub-ready files.
- Changelog uses days only, no timestamps.
- Labs can be messy, but every experiment needs a README and known limitations.
- Promote only when stable.

Next outputs:
README.md, a1111-preservation-bridge/README.md, docs/EXISTING_PROJECTS_REVIEW.md, docs/RISK_REGISTER.md, examples/
```
