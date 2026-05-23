# Canonical Overview — Vision-Language, OCR, and Document AI

## Core Definition
Vision-Language Document AI replaces brittle OCR with multimodal models that jointly understand layout, text, tables, and charts, enabling agentic extraction and reasoning over complex real-world documents.

## Metadata
Topic 22, v2.2, 2026-05-19, Sources: BentoML 2026 VLM guide, LlamaIndex agentic OCR benchmarks, DeepSeek-OCR paper, Qwen3-VL late-2025 technical report, Parseur Vision AI 2026 guide.

## Executive Summary Extract
## 1. Executive Summary & 2026 Landscape

Vision-Language Models (VLMs) have completely replaced traditional OCR pipelines in 2026. The shift from “extract text then reason” to “see the entire document and reason jointly” has delivered 30-50% accuracy lifts on complex real-world documents (noisy scans, handwriting, tables, forms, long contracts).

**Dominant 2026 Models**:
- **Qwen3-VL-235B-A22B** — Near frontier performance on document QA, layout analysis, chart understanding, and multilingual OCR (32+ languages).
- **DeepSeek-VL2 / DeepSeek-OCR** — Revolutionary “Contexts Optical Compression” technique; extremely efficient MoE (only 4.5B active params) with SOTA table/chart performance.
- **LlamaParse + Llama-3.2-Vision** — Best open agentic OCR with citations, confidence, and event-driven workflows.
- **Qwen2.5-VL / Aria / MiniCPM-V** — Strong open alternatives for specific niches.

**Data Engineering Implication**: Document images + layout + text + table structures + embeddings must be versioned together in a multimodal lakehouse (Lance + lakeFS). Pure text extraction is now considered legacy.

---

## Core Concepts / Architecture Extract
## 2. Core Concepts & The New Document AI Stack

**Traditional OCR (Legacy)**: Tesseract, EasyOCR, Google Document AI (template-based) — brittle on layout, tables, handwriting.

**Modern VLM Pipeline (2026 Standard)**:
1. Page → high-res image (300-600 DPI recommended)
2. VLM jointly processes visual layout + text + tables + charts
3. Structured JSON output with bounding boxes, confidence, citations
4. LLM post-processing / validation / enrichment
5. Agentic workflow (extract → reason → act)

**Key Data Types**:
- Raw page images (PNG/JPEG/WebP)
- Layout-aware JSON (blocks, lines, words, tables, figures)
- Table structures (Markdown, HTML, or relational)
- Embeddings (page-level + chunk-level + table-level)
- Provenance metadata (scan quality, source, consent)

---

## Best Practices / Patterns Extract
## 3. Architecture Patterns & Best Practices

**Recommended Production Architecture**:
- **Ingestion**: S3/GCS + lakeFS branching for raw scans
- **Processing**: Ray + Qwen3-VL or DeepSeek-VL2 (batch) + LlamaParse (agentic)
- **Storage**: Lance (images + embeddings + JSON) + lakeFS for versioning
- **Retrieval**: Hybrid (vector + keyword + table-aware) with LlamaIndex or LangChain
- **Evaluation**: DocVQA, ChartQA, KIE (Key Information Extraction) benchmarks + human review on high-stakes docs

**Critical Best Practices**:
- Always keep raw images + extracted JSON together (never throw away pixels).
- Use confidence + LLM-as-judge validation loops.
- For long documents (>50 pages): page-level chunking + hierarchical retrieval.
- Version the VLM + prompt + preprocessing config alongside the data.
- Add environmental metadata (scan DPI, lighting, paper type) for drift detection.

---
