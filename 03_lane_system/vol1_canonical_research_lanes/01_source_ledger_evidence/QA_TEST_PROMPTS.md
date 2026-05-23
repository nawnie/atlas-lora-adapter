# QA Test Prompts — Source Ledger and Evidence Governance

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** Which source supports this ComfyUI node claim?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** Is this package/card source-backed or chat-derived?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** What should be refreshed before publishing?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 4

**Prompt:** Which older file was consolidated into the canonical copy?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
