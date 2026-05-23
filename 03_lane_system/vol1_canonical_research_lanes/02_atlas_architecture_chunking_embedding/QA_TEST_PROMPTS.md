# QA Test Prompts — RAG Architecture, Chunking, and Embedding Strategy

Use these prompts to test whether this lane retrieves the right knowledge instead of vague adjacent content.

## Test 1

**Prompt:** How should I chunk package cards?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 2

**Prompt:** Should CSV files be embedded as prose or records?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 3

**Prompt:** What metadata should survive into AnythingLLM or a vector DB?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Test 4

**Prompt:** Why did dense retrieval miss an exact node class name?

**Expected retrieval:** concept card + canonical overview + relevant source folder.

## Negative control

Ask a question that belongs to a different lane. The assistant should route away instead of forcing this lane to answer.
