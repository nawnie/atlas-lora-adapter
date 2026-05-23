# Gap Audit and Vol. 2 Queue — Adapter Evaluation

This lane now defines the core proof-testing shape. The next maturity step is to run the tests and record results across real models.

## Remaining gaps

- Actual benchmark result logs for small local models.
- Side-by-side answer samples from no-RAG, raw-RAG, adapter-RAG, and larger no-adapter conditions.
- Human-reviewed scoring examples.
- A simple Python runner for golden-question evals.
- Integration profiles for Ragas, DeepEval, MLflow, and LangSmith in one local test harness.

## Vol. 2 candidates

- Automated eval runner.
- Gradio evaluation dashboard.
- Model comparison matrix.
- Retrieval trace viewer.
- Source-groundedness scorecard.
- Red-team eval pack for prompt injection and bad-source handling.
