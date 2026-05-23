# QA Test Prompts — Python/Pip Runtime Dependencies and Local AI Environment Support

Use these prompts to test retrieval and answer quality. Each prompt should be answerable using only this lane's `CANONICAL_OVERVIEW.md`, `CONCEPT_MAP.md`, and `RETRIEVAL_CARDS.jsonl`, plus the cross-linked lanes named in those files. Volatile-fact prompts are tagged with `[V]`.

## Diagnostic prompts

1. A user reports that ComfyUI launched fine yesterday but today a custom node is red and the console says `ImportError: DLL load failed`. Name the most likely cluster and the first three safe checks before any reinstall.
2. A user installed `onnxruntime-gpu` with `pip install onnxruntime-gpu` and the ORT log shows `CUDAExecutionProvider` is not available. What cluster owns this and what specifically should you check first?
3. A user's Gradio app fails to start with `OSError: [Errno 98] Address already in use`. Give the OS-correct (Windows + Linux) sequence to find and clear the bound port without rebooting.
4. A user updated `torch` and now `xformers` raises an obscure runtime warning followed by a CUDA crash. What is the "package cluster" rule and what's the minimal fix?
5. `pip install` reported success but `import bitsandbytes` raises `RuntimeError: cuda runtime version is older than the cuda libraries`. Which cluster, and what's the AIWF-safe order of remediation?

## Conceptual prompts

6. Define "venv island" and "ABI boundary" in your own words; explain why both matter for AIWF beginners.
7. What is an "import smoke test" and what minimum set of imports should one cover for a ComfyUI environment? For a Gradio LLM app?
8. Explain "provider mismatch" using ONNX Runtime as the example. Why does it fail silently?

## Decision prompts

9. A user asks "should I just `pip install -U` everything?" Give the AIWF answer plus the rationale.
10. A user wants to run ComfyUI and a separate Gradio app on the same machine. Should they share a venv or use two? Justify in terms of the cluster taxonomy.
11. A user has a working environment and a new custom node requires a different `transformers` version than what's installed. What are the three AIWF options (use / wrap / document / build) in order of safety?

## Volatile-fact prompts (must verify before quoting)

12. `[V]` Which CUDA toolkit minor versions does the current stable PyTorch wheel set publish for? Mark as `volatile_needs_recheck` and point to pytorch.org/get-started as the authority.
13. `[V]` What Python version does the current stable ComfyUI release require? Note any in-flight migration (e.g. 3.10 → 3.12).
14. `[V]` Does `uv` currently support CUDA-aware Torch installs without manual index URL? Tag for re-verification.

## Beginner-safety prompts

15. A user pastes a stack trace and asks "what command should I run?" What is the AIWF answer pattern? (Hint: diagnose first, name cluster, then minimal command, never `pip install -U` everything as the first move.)
16. A user proposes deleting their `.venv/` and reinstalling everything. Under what conditions is that the right answer, and under what conditions is it the wrong one?

## Pass criteria

A response passes if:

- it names the correct cluster from the taxonomy in `CONCEPT_MAP.md`
- it offers a non-destructive check before any destructive fix
- it does not invent specific version numbers for the volatile prompts
- it points to the correct cross-lane link when the question crosses into compatibility or failure-signature territory

## Negative control

Ask a question that belongs to a different lane (e.g. "What's the best CFG value for SDXL?"). The assistant should route to RP07 (CFG/Denoise/Inpaint theory) instead of forcing this lane to answer.
