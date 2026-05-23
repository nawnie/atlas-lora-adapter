# QA Test Prompts — ComfyUI Custom Node Ecosystem and Nodepack Evaluation

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** Which node pack should I use for inpainting?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** Can this node class_type be placed in generated JSON safely?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** Should AIWF use, wrap, document, or build around this repo?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
