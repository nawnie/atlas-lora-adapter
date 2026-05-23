# Adapter Evaluation and Proof Testing

This lane defines how to prove that the AIWF Atlas improves assistant behavior compared with no RAG, raw-file retrieval, or a larger model with no domain memory.

The goal is not academic theater. The goal is practical: when a user asks about ComfyUI, Gradio, source verification, model paths, RAG chunking, or workflow repair, the assistant should retrieve the right knowledge, explain the answer clearly, cite/qualify when needed, and avoid confident nonsense.

## Core idea

A Atlas Layer should be evaluated on four layers:

1. **Retrieval quality** — did the system find the right lane, card, and source?
2. **Answer quality** — is the answer correct, actionable, and beginner-safe?
3. **Grounding quality** — does it cite or qualify the claim appropriately?
4. **Operational quality** — does it know when to ask for logs, refuse risky actions, or choose the stable path?

## AIWF stance

If an eval only rewards smooth prose, it is not an AIWF eval. Smooth prose can still drive straight into a cactus wearing a lab coat. Measure usefulness, evidence, and operator safety.
