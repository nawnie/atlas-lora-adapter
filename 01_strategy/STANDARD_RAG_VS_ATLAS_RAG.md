# Standard RAG vs Atlas-Style RAG

## Standard RAG

Standard RAG often follows:

```text
documents -> chunks -> embeddings -> retrieved context -> answer
```

Strengths:

- simple;
- useful for document lookup;
- easy to implement;
- can improve factual grounding.

Weaknesses:

- chunks are often treated as equal;
- weak or old content may compete with canonical guidance;
- metadata is often ignored;
- source hierarchy may be unclear;
- the model may answer from memory;
- evaluation is often informal.

## Atlas-style RAG

Atlas-style RAG follows:

```text
source ledger -> lanes -> retrieval cards -> source priority -> failure signatures -> answer patterns -> evaluation
```

Strengths:

- gives knowledge a map;
- separates canonical guidance from archives;
- preserves source roles;
- routes questions to narrower context packs;
- uses do-not-confuse boundaries;
- supports evaluation and regression testing.

Weaknesses:

- requires more upfront structure;
- can over-fragment if lanes are weak;
- needs schema discipline;
- still depends on model capacity and retrieval quality.

## Atlas Reader LoRA role

The Atlas Reader LoRA should learn to operate inside Atlas-style RAG.

It should learn that retrieved context is not just text. It has:

- source path;
- layer;
- priority;
- freshness status;
- lane role;
- confidence;
- answer pattern;
- neighboring lanes.
