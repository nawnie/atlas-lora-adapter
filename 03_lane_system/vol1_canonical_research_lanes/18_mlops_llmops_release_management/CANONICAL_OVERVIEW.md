# Canonical Overview — MLOps, LLMOps, and Release Management

LLMOps extends MLOps into prompt, retrieval, tool, model, and evaluation versioning. The assistant should treat each AI app release as a bundle: model version, prompt version, retrieval index version, dataset version, eval result, config, and rollback path. The adapter itself should follow this discipline.

## Practitioner framing
This lane should be used as a decision-support layer, not as an isolated essay. It maps concepts to concrete AIWF use cases: local-first assistants, Atlas systems, Gradio tools, ComfyUI support agents, dataset QA, and small-model augmentation.

## Core concepts
- experiment tracking
- model registry
- prompt registry
- dataset version
- eval version
- release gate
- rollback
- canary release
- shadow traffic
- drift monitoring
- feedback loop
- incident report
- changelog

## Source-backed anchors
- MLflow GenAI eval and monitoring: https://mlflow.org/docs/latest/genai/eval-monitor/
- MLflow evaluation datasets: https://mlflow.org/docs/latest/genai/datasets/
- Arize AI observability: https://arize.com/
- LangChain / LangSmith platform: https://www.langchain.com/

## Freshness policy
- Foundational concepts are `stable` or `slow_changing`.
- Current tools, model families, security advisories, and platform behavior are `fast_moving` or `volatile`.
- If a user asks for latest versions, prices, benchmarks, vulnerabilities, or release status, the assistant should verify current sources before finalizing the answer.
