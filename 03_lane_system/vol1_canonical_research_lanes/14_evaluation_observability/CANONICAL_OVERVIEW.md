# Canonical Overview — AI Evaluation and Observability

Evaluation is the difference between a knowledge pack that feels useful once and one that remains reliable over time. The adapter should score retrieval, answer correctness, citation quality, refusal behavior, tool selection, and troubleshooting usefulness. Observability connects traces, prompts, retrieved chunks, tool calls, latency, cost, and user outcomes so changes can be measured instead of guessed.

## Practitioner framing
This lane should be used as a decision-support layer, not as an isolated essay. It maps concepts to concrete AIWF use cases: local-first assistants, Atlas systems, Gradio tools, ComfyUI support agents, dataset QA, and small-model augmentation.

## Core concepts
- eval dataset
- golden answer
- retrieval precision
- retrieval recall
- groundedness
- answer correctness
- hallucination rate
- LLM judge
- trace
- span
- latency p95
- cost per task
- regression test
- online monitoring

## Source-backed anchors
- MLflow GenAI evaluation and monitoring: https://mlflow.org/docs/latest/genai/eval-monitor/
- MLflow evaluation datasets: https://mlflow.org/docs/latest/genai/datasets/
- Azure Databricks GenAI eval harness: https://learn.microsoft.com/en-us/azure/databricks/mlflow3/genai/eval-monitor/concepts/eval-harness
- Arize AI observability / Phoenix OSS: https://arize.com/

## Freshness policy
- Foundational concepts are `stable` or `slow_changing`.
- Current tools, model families, security advisories, and platform behavior are `fast_moving` or `volatile`.
- If a user asks for latest versions, prices, benchmarks, vulnerabilities, or release status, the assistant should verify current sources before finalizing the answer.
