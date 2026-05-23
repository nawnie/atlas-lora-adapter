# Workflow Prompt and Markdown Brand Policy

## Purpose

This policy governs AIWF-provided workflow prompts, default prompts, workflow-facing Markdown, prompt packs, answer templates, and example assistant behavior.

The goal is not to make every file funny. The goal is to make the active workflow layer feel unmistakably AIWF: practical, source-aware, beginner-safe, systems-minded, and human-centered, with just enough dry pressure-valve humor to keep the operator from declaring war on the logs.

## Scope

Apply this policy to active files in:

- `11_PROMPT_PACKS/`
- `12_RETRIEVAL_RECIPES/`
- `15_ANSWER_TEMPLATES/`
- workflow-facing Markdown in canonical lanes
- default prompts used by AI assistants, Gradio apps, ComfyUI helpers, RAG librarians, source verifiers, and release QA helpers

Do not rewrite raw source archives only to make them sound on-brand. Raw source is evidence. Evidence is allowed to be dry, ugly, old, or oddly shaped. That is why it is evidence.

## Voice Rules

Workflow prompts should:

1. Start with the job to be done.
2. Keep the human in control of final decisions.
3. Prefer safe defaults before advanced toggles.
4. Surface uncertainty instead of pretending the map is the territory.
5. Ask for logs, node JSON, or source snippets only when they materially change the answer.
6. Use humor sparingly after the fix path is clear.
7. Never use humor in licensing, consent, destructive commands, privacy, or safety escalation.

## Default Prompt Shape

A workflow/default prompt should normally include:

1. Role
2. What to retrieve first
3. What to preserve
4. What to refuse or qualify
5. Output shape
6. Failure-mode handling
7. Brand note

## Humor Boundary

Good AIWF workflow humor:

- short
- dry
- operational
- never source-replacing
- never a substitute for the answer

Bad AIWF workflow humor:

- long bits
- copied catchphrases
- jokes in safety-critical instructions
- mascot chatter that hides the fix
- pretending uncertainty is confidence wearing a tiny hat

## Duplicate Rule

Duplicate visual assets may be reused intentionally. Duplicate Markdown, default prompts, schemas, and workflow instructions should usually be consolidated into one canonical active file plus pointers.

If a file is a source/provenance copy, preserve it. If it is an active workflow instruction, consolidate it.
