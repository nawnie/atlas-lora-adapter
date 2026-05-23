# QA Test Prompts — Compatibility Matrix RAG

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** Can this workflow run on 8 GB VRAM?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** Which models must be downloaded for this nodepack?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** Does this package belong in the shared ComfyUI venv or an isolated venv?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
