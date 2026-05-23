# QA Test Prompts — Training, Data-Centric ML, and Volume II Research Spine

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** Should this problem use prompting, RAG, LoRA, or fine-tuning?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** How do I inspect a dataset before training?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** What does overfitting look like in a small local training run?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
