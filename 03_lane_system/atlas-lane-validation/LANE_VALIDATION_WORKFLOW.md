# Lane Validation Workflow

Status: Phase 3 workflow  
Purpose: define how lanes become valid training material for Atlas Reader LoRA.

## Workflow

### 1. Candidate lane intake

A proposed lane enters the candidate list when it represents a repeated question class, distinct troubleshooting path, distinct source authority, distinct answer format, or distinct failure signature.

### 2. Duplication review

Before creating lane files, compare the lane against nearby existing lanes.

Reject or merge if the proposed lane is only a synonym or a single concept that belongs as a retrieval card inside another lane.

### 3. Lane kit creation

Create the standard lane kit:

```text
CANONICAL_OVERVIEW.md
CONCEPT_MAP.md
RETRIEVAL_CARDS.jsonl
SOURCE_COVERAGE.md
FAILURE_SIGNATURES.md
QA_TEST_PROMPTS.md
ANSWER_PATTERNS.md
DO_NOT_CONFUSE_WITH.md
GAP_AUDIT_AND_VOL2_QUEUE.md
lane_profile.json
```

### 4. Retrieval-card pass

Each lane needs at least 8 answer-bearing retrieval cards.

Cards should not use the weak template pattern:

```text
X is a core retrieval concept for Y.
```

Instead, each card should include:

- concrete problem pattern;
- likely user phrasing;
- source-priority rule;
- exact identifiers to preserve;
- answer pattern;
- do-not-confuse guidance;
- freshness or uncertainty rule.

### 5. QA prompt pass

Each lane needs at least 3 QA prompts:

1. normal answer test;
2. boundary/confusion test;
3. insufficient-context or freshness test.

### 6. Training record pass

Each lane should produce at least 6 structured training records before the 128-lane training gate is considered satisfied.

### 7. Evaluation pass

Each lane should be tested under:

```text
base model, no RAG
base model + raw RAG
base model + Atlas RAG
base model + Atlas Reader LoRA + Atlas RAG
```

### 8. Promotion

A lane can be marked `validated` when it has complete files, training examples, QA prompts, and at least one evaluation result.

## Output

The output of this process is not just a cleaner Atlas. It is a measured dataset showing whether structured RAG improves model behavior and whether the Atlas Reader LoRA improves how the model uses that structure.
