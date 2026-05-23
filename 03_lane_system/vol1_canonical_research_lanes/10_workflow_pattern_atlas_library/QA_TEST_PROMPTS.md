# QA Test Prompts — Workflow Pattern Library RAG

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** What is the best graph pattern for auto-inpaint?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** How do I combine restore, pose, and inpaint without making a broken monster workflow?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** Which inputs belong in a master control panel?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
