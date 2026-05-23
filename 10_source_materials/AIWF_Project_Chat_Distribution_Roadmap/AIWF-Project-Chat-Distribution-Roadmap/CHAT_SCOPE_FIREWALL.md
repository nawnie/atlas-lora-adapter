# AIWF Chat Scope Firewall

This file defines how individual AIWF project chats should behave.

## Primary Rule

Each project chat owns **one** lane.

It may read other roadmaps for context, but it should not alter, rewrite, reprioritize, or implement them.

## Memory Rule

Each chat should store only its own assigned roadmap as active memory/context.

Other roadmaps are reference-only and should not become new tasks unless the Brand Hub explicitly reassigns scope.

## Cross-Project Notes

If a chat notices something another project needs, it must not derail its own lane. It should write a Markdown-only note like this:

```markdown
# CROSS_PROJECT_NOTE.md

From: AIWF EnvPack Chat
To: AIWF Model Checker Chat / Brand Hub

## Issue
Briefly explain the dependency or conflict.

## Why It Matters
Explain impact on the current project.

## Requested Routing
Ask Brand Hub to route the note or ask the target project to review.
```

Then the chat should return to its assigned roadmap.

## Forbidden Drift

Do not:

- start implementing another repo
- rewrite another project's roadmap
- create `.txt` suggestion files for other projects
- bury cross-project advice in normal chat
- change release order unless the Brand Hub owns that change
- turn every project chat into a brand strategy chat

## Allowed Coordination

A project chat may:

- reference another roadmap to avoid duplication
- flag a dependency using `CROSS_PROJECT_NOTE.md`
- ask Brand Hub for routing
- ask Release Packaging for standards
- keep its own output compatible with shared AIWF naming and changelog rules
