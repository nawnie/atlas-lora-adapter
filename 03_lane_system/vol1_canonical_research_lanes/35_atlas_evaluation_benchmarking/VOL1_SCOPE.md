# Scope — Adapter Evaluation and Proof Testing

## In scope

- Golden question sets for AIWF topics.
- Expected-source retrieval checks.
- Raw-file retrieval vs adapter comparisons.
- Small-model evaluation protocols.
- RAG faithfulness, answer relevance, and context precision/recall concepts.
- Agent/tool-use task completion checks.
- Source-grounding and citation quality checks.
- Regression tests after archive updates.
- Human review rubrics for answers that affect installs, code, security, licensing, or data handling.

## Out of scope

- Claiming benchmark superiority without running tests.
- Treating LLM-as-judge output as unquestionable truth.
- Using eval scores as a replacement for human review in high-risk answers.
- Letting an eval harness grade itself with no audit trail. That is how the spreadsheet becomes a ghost story.
