# Canonical Overview — Governance, Licensing, Ethics, and Responsible Use

Governance is the practical answer to “can I use, ship, sell, train on, or connect this?” The adapter should identify license constraints, consent requirements, provenance gaps, disclosure needs, and high-risk use cases. It should distinguish project policy from legal fact, and recommend verification from the source license before commercial release.

## Practitioner framing
This lane should be used as a decision-support layer, not as an isolated essay. It maps concepts to concrete AIWF use cases: local-first assistants, Atlas systems, Gradio tools, ComfyUI support agents, dataset QA, and small-model augmentation.

## Core concepts
- license
- commercial use
- non-commercial weights
- data provenance
- consent receipt
- model card
- data card
- risk register
- audit log
- human oversight
- content provenance
- incident disclosure

## Source-backed anchors
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Generative AI Profile publication: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- OWASP GenAI Security Project: https://genai.owasp.org/llm-top-10/

## Freshness policy
- Foundational concepts are `stable` or `slow_changing`.
- Current tools, model families, security advisories, and platform behavior are `fast_moving` or `volatile`.
- If a user asks for latest versions, prices, benchmarks, vulnerabilities, or release status, the assistant should verify current sources before finalizing the answer.
