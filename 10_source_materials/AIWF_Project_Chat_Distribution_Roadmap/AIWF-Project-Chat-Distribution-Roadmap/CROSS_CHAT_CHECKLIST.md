# AIWF — Cross-Chat Coordination Checklist

Use this at the start of each project chat.

## Identify the lane

- [ ] What repo does this chat serve?
- [ ] What files should this chat produce?
- [ ] What is out of scope?
- [ ] What existing projects might already solve this?
- [ ] What is the next GitHub-ready output?

## Before building

- [ ] Check ComfyUI built-ins
- [ ] Check ComfyUI-Manager
- [ ] Check ComfyUI-Doctor
- [ ] Check MTB
- [ ] Check Hugging Face
- [ ] Check Civitai
- [ ] Check GitHub
- [ ] Decide: use, wrap, document, or build missing piece

## Repo hygiene

- [ ] README exists
- [ ] CHANGELOG exists
- [ ] Changelog uses days only
- [ ] Install command exists
- [ ] Windows PowerShell path exists
- [ ] Examples exist
- [ ] Known limitations are documented
- [ ] No unstable Labs code in beta repo

## AIWF naming

- [ ] Public name uses `AIWF [Thing]`
- [ ] Repo name is short and readable
- [ ] README links back to parent AIWF brand
- [ ] Tool promise is clear in one sentence

## Beta quality bar

- [ ] Narrow scope
- [ ] Runs locally
- [ ] Has one-click or near-one-click command
- [ ] Produces a useful artifact
- [ ] Does not require perfect setup
- [ ] Fails gracefully
- [ ] Explains next action to the user


## Scope Firewall Checklist

Before any project chat starts work, confirm:

- [ ] `SENDOFF_MASTER.md` was pasted first.
- [ ] Only that chat's assigned handoff was pasted as active roadmap.
- [ ] Other project roadmaps were marked reference-only.
- [ ] The chat understands it should not work on other project lanes.
- [ ] Cross-project concerns will be sent as fenced Markdown titled `CROSS_PROJECT_NOTE.md`.
- [ ] No `.txt` files are used for suggestions.
- [ ] The chat returns to its assigned output after any cross-project note.

## Field Guide Agent Checklist

- [ ] Volume I remains the active Field Guide production focus.
- [ ] 8-agent structure is recognized for Field Guide work: 4 GPT-side, 4 Grok-side.
- [ ] Claude is reserved for the final editorial pass.
- [ ] Volume II / Training AI stays parked until 3.5 training becomes practical enough to document seriously.
