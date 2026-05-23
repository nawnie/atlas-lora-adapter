# QA Test Prompts — ComfyUI Core API, Workflow JSON, and Subgraph Research

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** How do I verify a ComfyUI workflow JSON before giving it to a user?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** Which fields are source of truth in workflow JSON?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** How should subgraphs be represented for a beginner UI?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
