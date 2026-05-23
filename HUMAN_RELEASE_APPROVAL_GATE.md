# Human Release Approval Gate

Status: active governance rule  
Version added: v0.2.3  
Date: 2026-05-22  
Owner approval required: Shawn O'Hagan

## Rule

No AI assistant, automated script, agent, or external reviewer may promote this project from an `x.x.9` release to the next `x+1.0` or `x.(x+1).0` release without explicit human approval from Shawn O'Hagan.

This includes jumps such as:

```text
v0.9 -> v1.0
v0.2.9 -> v0.3.0
v0.3.9 -> v0.4.0
v0.9.9 -> v1.0.0
```

## Plain-language version

Patch and planning work can continue inside the current version track, but a major milestone jump must be approved by Shawn.

An AI can recommend a promotion.

An AI can prepare the release notes.

An AI can list the evidence.

An AI cannot decide that the promotion is official.

## Required approval language

A milestone jump is approved only when Shawn explicitly says something equivalent to:

```text
Approved: promote to vX.Y.0
```

or:

```text
I approve this as vX.Y.0
```

Ambiguous language is not enough.

Examples that are not approval:

```text
This looks good.
Let's keep going.
A.
Continue.
Package it.
Looks ready.
```

## Why this exists

Version numbers are project-governance signals.

This project is research-facing, and the difference between a planning artifact, a test artifact, a release candidate, and a published result matters.

The project should not drift into inflated maturity because an AI assistant keeps packaging updates or treating internal progress as release advancement.

## AI assistant behavior

When an AI assistant believes the project may be ready to move from `x.x.9` to the next milestone release, it should respond with:

1. current version;
2. proposed next version;
3. evidence that the exit gate is met;
4. known gaps;
5. risks or unresolved issues;
6. a clear request for Shawn's explicit approval.

The assistant should not update files to the next milestone version until approval is given.

## Example

Allowed:

```text
The v0.2.9 checklist appears complete. I recommend promotion to v0.3.0, but I need your explicit approval before changing the version.
```

Not allowed:

```text
I promoted the project to v0.3.0 because the checklist looked complete.
```

## Authority

Final milestone-promotion authority belongs to Shawn O'Hagan.

This is a human governance gate, not an AI judgment gate.
