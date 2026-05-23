# Canonical Overview — Adapter Evaluation and Proof Testing

The AIWF Atlas is designed to make AI assistants more useful by giving them structured, source-aware domain memory. That claim needs testing.

## The core comparison

Evaluate the same model/task under multiple conditions:

| Mode | Description | Purpose |
|---|---|---|
| No RAG | Model answers from internal knowledge only | Baseline hallucination and missing-context rate |
| Raw-file RAG | Model retrieves from unstructured source files | Measures whether dumping files is enough |
| AIWF Atlas retrieval | Model retrieves from lanes, cards, policies, and sources | Measures value of structure and governance |
| Larger no-adapter model | Stronger model without domain memory | Tests whether structure can compensate for model size |

## What to measure

- **Retrieval hit rate**: did the expected lane/card/source appear?
- **Groundedness**: does the answer stay inside retrieved evidence?
- **Answer relevance**: does the answer solve the user’s actual task?
- **Actionability**: can the user safely apply it?
- **Source behavior**: does the assistant cite, qualify, or say when a claim is unverified?
- **Version awareness**: does it avoid treating old/historical files as current?
- **Operator safety**: does it avoid destructive commands unless the user clearly asked and the path is safe?

## Framework alignment

Ragas provides metrics for measuring LLM application performance across RAG and agentic workflows. MLflow frames LLM/agent evaluation as systematic measurement and monitoring across development and production. DeepEval provides plug-and-play metrics for LLM applications. LangSmith describes evaluation workflows using datasets, evaluators, and experiments.

## AIWF quality bar

A good adapter answer should feel like a field tech who brought the right binder, not a fortune teller with a GPU bill.
