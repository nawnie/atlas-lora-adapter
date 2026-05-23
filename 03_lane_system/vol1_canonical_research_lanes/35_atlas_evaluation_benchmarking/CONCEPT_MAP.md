# Concept Map — Adapter Evaluation and Proof Testing

## Main concepts

- **Golden question** → a representative user question with expected answer traits.
- **Expected source** → the lane/card/source that should be retrieved.
- **Rubric** → scoring criteria for answer quality.
- **Regression test** → repeated test after each archive update.
- **Raw-RAG baseline** → performance when only source files are embedded.
- **Adapter-RAG condition** → performance when AIWF lanes, cards, policies, and source gates are used.
- **LLM-as-judge** → model-based scoring that must be audited and sampled by humans.
- **Human spot check** → human review for safety, sourcing, and practical usefulness.

## Relationship map

- Evaluation harness depends on source policy.
- Source policy depends on source verification.
- Retrieval tests depend on Atlas cards.
- Golden questions depend on real user tasks.
- Regression tests depend on stable expected outputs and expected sources.
- Human review overrides automated scores when safety, licensing, privacy, or destructive commands are involved.

## Torchie field note

If the eval system says every answer is perfect, assume the gauge is broken. Perfect systems are usually either imaginary or on fire behind a very confident dashboard.
