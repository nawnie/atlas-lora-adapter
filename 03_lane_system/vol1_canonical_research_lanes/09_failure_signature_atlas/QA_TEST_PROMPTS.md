# QA Test Prompts — Failure Signature Atlas RAG

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** What does this traceback usually mean?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** Why are my nodes red?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** What log should I paste for help?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 4

**Prompt:** How do I recover from CUDA/cuDNN mismatch safely?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
