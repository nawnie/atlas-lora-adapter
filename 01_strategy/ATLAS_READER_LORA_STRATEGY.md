# Atlas Reader LoRA Strategy

Status: strategy proposal  
Date: 2026-05-22  
Project: AI Without Fear / AIWF Atlas  
Target layer: `18_ATLAS_READER_LORA/`  
Related systems: AIWF Atlas, structured RAG, lane routing, retrieval cards, evaluation harness, local model adaptation

## Executive summary

The AIWF project is shifting from a standard RAG corpus toward a structured knowledge-routing system called the **AIWF Atlas**. The next strategic step is the **Atlas Reader LoRA**: a parameter-efficient adapter trained to help a base model read, route, rank, and apply structured RAG context more reliably.

The goal is not to train a LoRA that memorizes AIWF facts. The goal is to train a LoRA that understands how to operate over an Atlas-style knowledge system.

In short:

```text
Knowledge = RAG
Behavior = LoRA
Proof = evaluation harness
```

The Atlas stores the knowledge. The Atlas Reader LoRA teaches the model how to read that kind of knowledge. The evaluation harness proves whether the combined system works.

## Why this shift matters

A normal RAG system often works like this:

```text
documents -> chunks -> embeddings -> retrieval -> answer
```

That is useful, but it treats the knowledge base as a mostly flat pile of chunks. Weak notes, old source archives, canonical guidance, source policies, and current documentation can all compete in the same retrieval pool unless the system is carefully structured.

AIWF Atlas is different. It is designed as a mapped knowledge system:

```text
raw data -> source ledger -> lanes -> retrieval cards -> source priority -> failure signatures -> answer patterns -> evaluation
```

This turns the corpus into a navigable knowledge map rather than a loose reference folder.

The Atlas Reader LoRA is the behavioral adapter that helps a model understand this map.

## Terminology

### Tokenization

Tokenization is the process of breaking text into model-readable pieces. It does not make the model learn the information. It only prepares text for input.

### Embeddings

Embeddings turn text chunks into vectors for search and retrieval. In systems like AnythingLLM, embeddings make a document set searchable. They do not change the model's weights.

### RAG

Retrieval-Augmented Generation retrieves relevant chunks from an external knowledge base and passes them into the model as context.

RAG is external memory. It helps the model answer with reference material, but it does not make the model permanently learn the material.

### Fine-tuning / LoRA

Fine-tuning changes model behavior through training. LoRA is a parameter-efficient training method that adapts a base model by adding small trainable adapter weights while leaving most of the base model unchanged.

A LoRA is usually tied to a compatible base model family. One adapter concept can be reused across model families, but the actual adapter files normally need to be trained for each target architecture or compatible base.

### Atlas

In AIWF, an Atlas is a source-aware, lane-routed knowledge map designed to help AI systems retrieve, judge, and apply domain knowledge without treating every document chunk as equally trustworthy.

The term is adapted from the ordinary meaning of an atlas as a collection of maps. AIWF uses it to mean a mapped knowledge system around a RAG corpus.

### Atlas Reader LoRA

An Atlas Reader LoRA is a parameter-efficient adapter trained to improve how a model interprets structured RAG context, especially when that context includes lanes, source hierarchy, retrieval cards, failure signatures, answer patterns, and freshness rules.

It is not a fact LoRA. It is a RAG-literacy LoRA.

## Core thesis

The Atlas Reader LoRA should learn how to use structured retrieved evidence.

It should not learn the whole AIWF Atlas as memorized content.

The desired behavior is:

```text
Given a user question and retrieved context:
1. Identify the likely lane or problem class.
2. Determine which retrieved chunks are authoritative.
3. Prefer canonical lane guidance over raw archive material.
4. Detect stale, volatile, or unsupported claims.
5. Avoid inventing commands, paths, node names, APIs, or citations.
6. Use the correct answer pattern for the task.
7. Say when the retrieved context is insufficient.
8. Produce a practical, beginner-safe, source-aware answer.
```

## What makes this different from standard RAG

Standard RAG often asks the model to answer from retrieved chunks.

Atlas-style RAG gives the model a mapped operating environment:

| Standard RAG | Atlas-style RAG |
|---|---|
| Flat chunks | Lanes and source layers |
| Retrieved text only | Retrieved text plus metadata and role |
| Weak and strong sources may compete | Source-priority rules decide authority |
| The model may ignore provenance | Source path and evidence role are preserved |
| Context may be overstuffed | Routing narrows the context pack |
| The model may answer from memory | Confidence gates require source discipline |
| Evaluation is often informal | Golden questions and rubrics measure behavior |

The Atlas Reader LoRA is trained specifically to operate in the second system.

## Mural network framing

The current AIWF work can be understood as designing a mural network around collected data.

This is not a neural network inside the model. It is a semantic routing network around the model.

The mural network gives every piece of knowledge:

- a place;
- a job;
- a lane;
- a source trail;
- a confidence role;
- neighboring lanes;
- boundaries;
- failure signatures;
- answer patterns.

This resembles older AI ideas such as knowledge bases, expert systems, semantic networks, and cognitive maps, but it is used alongside modern LLMs and RAG rather than replacing them.

The model remains the reasoning engine. The Atlas becomes the map, source ledger, rulebook, and troubleshooting scaffold.

## Product framing

The strongest product name is:

# Atlas Reader LoRA

Supporting terms:

- Atlas Reader Adapter
- Structured RAG Adapter
- Source-Governed RAG Reader Adapter
- RAG-literacy LoRA

Preferred public definition:

> Atlas Reader LoRA is a parameter-efficient adapter trained to improve how a model interprets lane-based, source-governed RAG context. It teaches the model to route, rank, verify, and answer from structured evidence instead of treating retrieved chunks as a flat pile of text.

## What the LoRA should learn

### 1. Lane routing

The model should identify which lane or domain area best matches the user question.

Example:

```text
Question: WAN crashes after 121 frames but image generation works.
Primary lane: video_vram_optimization
Secondary lanes: wan_video_workflows, last_frame_chaining_video_extension
Wrong lanes: prompt_anatomy_image_models, face_restore_faceswap
Reason: The issue is frame-count and VRAM related, not image prompt quality.
```

### 2. Source hierarchy

The model should prefer stronger source layers over weaker ones.

General priority:

```text
root guidance / operating policy
> read-first control files
> retrieval index and canonical lanes
> source-specific handbook sections
> source archives
> change history / old packaged releases
```

The exact priority may vary by corpus, but the behavior should remain consistent: understand source role before answering.

### 3. Evidence filtering

The model should ignore retrieved chunks that are unrelated, old, weak, or lower priority when better evidence is available.

### 4. Conflict handling

When retrieved sources disagree, the model should:

1. name the conflict;
2. prefer the higher-priority or newer source;
3. downgrade confidence if unresolved;
4. avoid pretending certainty.

### 5. Freshness awareness

The model should flag claims that may require current verification, especially:

- package versions;
- API behavior;
- active GitHub repositories;
- model availability;
- hardware compatibility;
- benchmark claims;
- license terms;
- security practices;
- pricing or cloud limits.

### 6. Exactness discipline

The model should avoid inventing:

- file paths;
- commands;
- package names;
- model filenames;
- API endpoints;
- ComfyUI node class types;
- socket names;
- citations;
- source claims.

If exact evidence is missing, it should say so and offer a safe next step.

### 7. Answer-format selection

The model should choose the right output structure based on the user request.

| User request type | Ideal output |
|---|---|
| Fix this error | Diagnostic tree |
| Review this repo | Audit summary |
| Plan this project | Roadmap |
| Build this app | Architecture and file plan |
| What source supports this? | Evidence map |
| Can I trust this? | Confidence assessment |
| Make this beginner-friendly | Explanation and safe defaults |
| QA this | Rubric-based review |

### 8. Insufficient-context behavior

The model should say when retrieval does not contain enough evidence.

It should not fill gaps with confident guesses.

## What should stay in RAG

The following should remain in RAG because they are exact, large, volatile, or source-sensitive:

- current install commands;
- package versions;
- API routes and behavior;
- model names and file locations;
- license details;
- source excerpts;
- ComfyUI node class names;
- workflow JSON socket details;
- Gradio version behavior;
- current compatibility matrices;
- hardware recommendations;
- citations and provenance.

## What should be trained into the LoRA

The following behaviors are good training targets:

- reading structured context;
- recognizing source role;
- routing to lanes;
- rejecting weak evidence;
- handling conflicts;
- knowing when verification is required;
- producing practical troubleshooting answers;
- keeping beginner safety boundaries;
- using AIWF-style answer discipline;
- avoiding unsupported exact identifiers;
- formatting answers based on task type.

## Reusable architecture

The long-term architecture is:

```text
Base model
  + Atlas Reader LoRA
  + structured RAG corpus
  + retrieval policy / system prompt
  + evaluation harness
  = source-aware domain assistant
```

The same concept can be applied to multiple domains:

```text
Base model + Atlas Reader LoRA + AIWF Atlas = AIWF assistant
Base model + Atlas Reader LoRA + hotel operations Atlas = hotel ops assistant
Base model + Atlas Reader LoRA + repair manual Atlas = repair assistant
Base model + Atlas Reader LoRA + project docs Atlas = project assistant
```

The facts change. The reading behavior stays the same.

## Important limitation

A single LoRA is not universally portable across all model families.

The strategy is reusable, but adapter weights usually need to match a compatible base model architecture.

Recommended framing:

```text
One Atlas Reader training method.
Separate Atlas Reader adapters per model family or compatible base.
```

Example:

```text
Qwen 4B + Atlas Reader LoRA for Qwen 4B
Qwen 7B + Atlas Reader LoRA for Qwen 7B
Mistral 7B + Atlas Reader LoRA for Mistral-compatible bases
```

## Training data design

Training data should not be raw Atlas dumps.

The dataset should consist of structured task examples:

```text
user question + retrieved context + metadata -> correct RAG-aware answer
```

### Core training record fields

Suggested JSONL schema:

```json
{
  "record_id": "string",
  "task_type": "lane_routing | answer_from_context | conflict_resolution | insufficient_context | exactness_guard | freshness_check | answer_format_selection | multi_rag_generalization",
  "user_question": "string",
  "retrieved_context": [
    {
      "source_path": "string",
      "layer": "root_guidance | read_first | retrieval_index | canonical_lane | source_pack | source_archive | change_history | unknown",
      "lane_id": "string or null",
      "priority": 1,
      "freshness": "current | stable | stale | volatile | unknown",
      "content": "string"
    }
  ],
  "expected_behavior": {
    "primary_lane": "string or null",
    "secondary_lanes": [],
    "sources_to_use": [],
    "sources_to_ignore": [],
    "needs_current_verification": false,
    "confidence": "high | medium | low",
    "answer_format": "diagnostic_tree | roadmap | audit | checklist | code_fix | evidence_map | explanation"
  },
  "output": "string"
}
```

## Training example types

### Type 1: lane routing

Purpose: teach the model to route questions into the right lane before answering.

```json
{
  "task_type": "lane_routing",
  "user_question": "WAN crashes after 121 frames but image generation works fine. What should I check?",
  "expected_behavior": {
    "primary_lane": "video_vram_optimization",
    "secondary_lanes": ["wan_video_workflows", "last_frame_chaining_video_extension"],
    "confidence": "high"
  },
  "output": "This routes primarily to video VRAM optimization, with WAN video workflows and last-frame chaining as secondary lanes. The clue is that still images work but longer frame counts fail, which points to memory pressure, batching, cache behavior, or video-length strategy rather than prompt quality."
}
```

### Type 2: answer from context

Purpose: teach the model to answer from retrieved evidence instead of memory.

```json
{
  "task_type": "answer_from_context",
  "user_question": "Why won't these ComfyUI nodes connect?",
  "retrieved_context": [
    {
      "source_path": "lanes/comfyui_socket_contract_debugging/FAILURE_SIGNATURES.md",
      "layer": "canonical_lane",
      "priority": 2,
      "content": "IMAGE, LATENT, MASK, CONDITIONING, and MODEL are separate socket types. A workflow fails when an output socket is connected to an incompatible input socket."
    }
  ],
  "output": "This is likely a socket-contract problem. The retrieved lane says IMAGE, LATENT, MASK, CONDITIONING, and MODEL are separate socket types, so the first check is whether the output type of one node matches the input type of the next. Do not install another node pack until the socket boundary is verified."
}
```

### Type 3: conflict resolution

Purpose: teach the model to prefer stronger sources.

```json
{
  "task_type": "conflict_resolution",
  "user_question": "Should I use this old launch flag by default?",
  "retrieved_context": [
    {
      "source_path": "00_AI_READ_FIRST/SOURCE_PRIORITY_AND_CONFLICT_RESOLUTION.md",
      "layer": "read_first",
      "priority": 1,
      "content": "Current official documentation outranks older archive notes for volatile command and API behavior."
    },
    {
      "source_path": "06_CHANGE_HISTORY/old_notes.md",
      "layer": "change_history",
      "priority": 7,
      "content": "Use the old flag by default."
    }
  ],
  "output": "Do not treat the old launch flag as a default from this retrieval alone. The higher-priority source says current official documentation outranks older archive notes for volatile command behavior. The safe answer is to verify the flag against current docs before recommending it."
}
```

### Type 4: insufficient context

Purpose: teach the model not to invent missing facts.

```json
{
  "task_type": "insufficient_context",
  "user_question": "What exact node class_type should I use for this workflow?",
  "retrieved_context": [
    {
      "source_path": "lanes/comfyui_workflow_repair/CANONICAL_OVERVIEW.md",
      "layer": "canonical_lane",
      "priority": 2,
      "content": "Validate node class_type values against object_info before generating workflow JSON."
    }
  ],
  "output": "The retrieved context does not provide the exact class_type. It only says class_type values should be validated against object_info before generating workflow JSON. I should not invent the node name. The next step is to inspect object_info or the installed node definition."
}
```

### Type 5: freshness check

Purpose: teach the model to flag volatile claims.

```json
{
  "task_type": "freshness_check",
  "user_question": "Is this Gradio 6 API behavior still current?",
  "retrieved_context": [
    {
      "source_path": "INGESTION_GUIDE.md",
      "layer": "root_guidance",
      "priority": 1,
      "content": "Before treating an answer as current guidance, verify claims about API behavior, package versions, licenses, active GitHub repository status, and security practices."
    }
  ],
  "output": "This needs current verification. The retrieved guidance says API behavior and package-version claims should be checked before being treated as live guidance. I can use the Atlas for structure, but the final answer should verify against current Gradio documentation."
}
```

### Type 6: multi-RAG generalization

Purpose: prevent overfitting to AIWF-only terms.

Use synthetic corpora that follow the same structure but cover different domains:

```text
AIWF Atlas
Hotel operations Atlas
Vehicle repair Atlas
Python project docs Atlas
Fiction/worldbuilding Atlas
```

The adapter should learn the reading protocol, not just AIWF vocabulary.

## Implementation plan

### Phase 1: define the formal strategy

Create the initial Atlas Reader LoRA strategy files:

```text
18_ATLAS_READER_LORA/
  ATLAS_READER_LORA_STRATEGY.md
  TRAINING_DATA_SCHEMA.json
  TRAINING_EXAMPLE_TYPES.md
  SAMPLE_RECORDS.jsonl
  EVALUATION_PLAN.md
  MODEL_FAMILY_NOTES.md
```

### Phase 2: create schema and sample data

Build the first dataset schema and 50-100 high-quality sample records.

Initial categories:

1. lane routing;
2. answer from context;
3. conflict resolution;
4. insufficient context;
5. freshness check;
6. exactness guard;
7. answer-format selection;
8. multi-RAG generalization.

### Phase 3: generate training data from Atlas lanes

Use the Atlas lane system to generate training records.

Do not convert raw Markdown directly into training samples. Instead:

1. retrieve a lane or card;
2. create a user-like question;
3. attach relevant and distractor context;
4. write the correct answer;
5. record expected behavior metadata.

### Phase 4: train first adapter

Initial training target should be a practical local instruct model family, likely a Qwen instruct-class model or similar local model suitable for structured instructions and code-adjacent work.

Exact model choice should be verified before training because local model availability, licensing, and best options change quickly.

Recommended first experiments:

```text
4B base model + Atlas Reader LoRA
7B base model + Atlas Reader LoRA
```

Use QLoRA/LoRA-style instruction tuning to reduce VRAM cost.

### Phase 5: evaluate against baselines

Run the same question sets across:

```text
4B base, no RAG
4B base + raw RAG
4B base + Atlas RAG
4B base + Atlas Reader LoRA + Atlas RAG
7B base, no RAG
7B base + raw RAG
7B base + Atlas RAG
7B base + Atlas Reader LoRA + Atlas RAG
```

Use the AIWF evaluation rubric categories:

- grounding;
- exactness;
- actionability;
- retrieval discipline;
- beginner safety;
- AIWF alignment.

### Phase 6: test cross-corpus behavior

To prove this is not merely an AIWF memorization adapter, test it on at least two non-AIWF structured corpora:

1. hotel operations Atlas;
2. Python project docs Atlas;
3. vehicle repair Atlas;
4. fictional/worldbuilding Atlas;
5. another small technical manual.

The claim to test:

> Atlas Reader LoRA improves how the model uses structured RAG context, even when the RAG corpus changes.

## Evaluation success criteria

The Atlas Reader LoRA is useful if it improves:

1. correct lane selection;
2. source-priority discipline;
3. refusal to invent exact identifiers;
4. recognition of insufficient context;
5. freshness warnings for volatile claims;
6. correct answer formatting;
7. beginner safety;
8. performance of smaller models against larger baselines in bounded tasks.

## Claims we can make now

Safe current claims:

- Atlas Reader LoRA is a proposed adapter strategy.
- It is designed to improve structured-RAG reading behavior.
- It should train behavior, not facts.
- It should be evaluated against raw RAG and no-RAG baselines.
- It may help smaller models perform better in bounded, source-grounded tasks.

## Claims we should not make yet

Do not claim:

- that this makes RAG obsolete;
- that this makes a 4B model equal a 7B model globally;
- that one LoRA works across all base models;
- that the adapter improves performance before evaluation results exist;
- that it contains current truth about volatile tools or models;
- that it replaces official documentation;
- that it is a new LoRA algorithm.

The correct claim is:

> Atlas Reader LoRA is a new practical adapter use-pattern: a LoRA trained to improve how a model reads and applies structured RAG context.

## Relationship to AIWF Atlas lanes

Atlas Reader LoRA should become both:

1. a strategy/project layer under `18_ATLAS_READER_LORA/`;
2. a canonical lane once enough source material, training examples, and evaluation plans exist.

Suggested future lane:

```text
51_atlas_reader_lora/
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

## Relationship to lane expansion

The lane expansion plan and Atlas Reader LoRA reinforce each other.

More precise lanes help retrieval.

The Atlas Reader LoRA teaches the model how to use those lanes.

The evaluation harness proves whether the combination works.

The combined system is:

```text
more precise lanes
+ answer-bearing retrieval cards
+ source hierarchy
+ do-not-confuse rules
+ Atlas Reader LoRA
+ evaluation harness
= stronger small-model domain assistance
```

## Minimal viable experiment

The first MVP should be small:

1. Choose 3 lanes:
   - ComfyUI socket contract debugging;
   - video VRAM optimization;
   - retrieval card authoring.
2. Create 100-200 training examples.
3. Include both good context and distractor context.
4. Train a small adapter on one base model.
5. Test 25 golden questions across base, RAG, and LoRA+RAG conditions.
6. Record results before expanding.

## Long-term product idea

Atlas Reader LoRA can become a repeatable method:

```text
Any messy expertise archive
-> convert to Atlas-style lanes
-> generate structured RAG-reader training examples
-> train Atlas Reader adapter
-> evaluate against raw RAG
-> deploy as a source-aware assistant
```

This makes AIWF more than a guide or RAG corpus. It becomes a method for turning messy expertise into model-usable external cognition.

## Final framing

AIWF Atlas is the mapped knowledge system.

Atlas Reader LoRA is the adapter that teaches a model how to read that map.

The model supplies language and reasoning.

The Atlas supplies structured memory.

The LoRA supplies disciplined reading behavior.

The evaluation harness supplies proof.

That is the shift.
