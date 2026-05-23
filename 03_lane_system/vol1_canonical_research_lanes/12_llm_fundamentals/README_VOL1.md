# LLM Fundamentals — Vol. 1 Lane

## Lane ID
`12_llm_fundamentals`

## Purpose
Ground the adapter in how modern language models work: tokenization, transformer attention, context windows, decoding, alignment, quantization, and local model family selection.

## Machine-use summary
LLM fundamentals is the base layer for every assistant using the adapter. The assistant must know the difference between model knowledge, retrieved context, tool output, chat template formatting, and decoding behavior. A retrieval-augmented small model should be treated as a reasoning engine plus external memory, not as a memorized encyclopedia. Transformer attention is stable foundational knowledge; model-family rankings and context-window limits are volatile and must be tagged as fast-moving.

## How an AI assistant should use this lane
- Retrieve this lane when user asks about llm fundamentals concepts, implementation decisions, risks, or architecture tradeoffs.
- Prefer this lane's canonical overview before raw source notes.
- Treat model rankings, current tools, and vendor claims as fast-moving unless source freshness says otherwise.
- For answerable implementation questions, combine this lane with relevant app, deployment, data, or safety lanes.

## Primary related lanes
- `02_atlas_architecture_chunking_embedding`
- `11_gradio_ui_research`
- `24_ai_application_architecture`
