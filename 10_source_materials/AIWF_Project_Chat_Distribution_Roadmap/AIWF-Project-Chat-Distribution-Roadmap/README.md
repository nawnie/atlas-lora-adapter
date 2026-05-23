# AIWF Project Chat Distribution Roadmap

This package contains a roadmap for distributing the AI Without Fear GitHub project across individual project chats.

## Files

```text
MASTER_DISTRIBUTION_ROADMAP.md
PROJECT_CHAT_MAP.md
CROSS_CHAT_CHECKLIST.md
CHANGELOG.md
CHAT_HANDOFFS/
```

## How to use

Open the handoff file for the chat you are working in, paste the starter prompt into that chat, and keep that chat focused on its assigned lane.

The most important rule:

> AI Without Fear is the umbrella. Each chat owns one product lane.

## First beta priority

The first GitHub beta should be:

```text
AIWF-EnvPack
```

Purpose:

> One PowerShell command creates a clean local-AI support report showing GPU, CUDA, Torch, ComfyUI, custom nodes, ports, logs, model folders, duplicates, and likely mismatches.


## Updated distribution rule

Use `SENDOFF_MASTER.md` before any individual handoff. Each project chat should store only its assigned roadmap as active memory/context. Other roadmaps are reference-only.

Cross-project suggestions must not drift into normal chat or `.txt` files. If unavoidable, write them as Markdown in a fenced code block titled `CROSS_PROJECT_NOTE.md` and route them back to Brand Hub or Release Packaging.

## New control files

```text
SENDOFF_MASTER.md
CHAT_SCOPE_FIREWALL.md
AI_FIELD_GUIDE_AGENT_PLAN.md
```
