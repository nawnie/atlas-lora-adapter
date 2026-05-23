# Pre-Install Status

Status: active status guard  
Version added: v0.2.9-dev17  
Date: 2026-05-22

## Current truth

This project has **not** been installed on the target PC yet.

That means the repo currently has:

```text
installer prepared: yes
training scripts prepared: yes
TensorBoard support prepared: yes
report templates prepared: yes
seed lanes prepared: 18
seed cards prepared: 216
installed on target PC: no
smoke test run on target PC: no
training run completed: no
adapter trained: no
evaluation completed: no
performance wins claimed: no
```

## No-wins rule

Do not claim:

- the installer works on the target PC;
- the training stack works on the target PC;
- TensorBoard logs correctly on the target PC;
- the adapter improves anything;
- Atlas RAG beats raw RAG;
- a small model matches a larger model;
- the idea is validated.

Those statements require run logs.

## What can be claimed safely

Safe:

```text
The repo contains installer scripts.
The repo contains training scripts.
The repo contains report templates.
The repo contains seed lanes and seed cards.
The repo contains source/citation docs.
The repo is ready for first local install testing.
```

Unsafe:

```text
The lab works.
The adapter works.
The method works.
The model improved.
The training succeeded.
```

## Report templates

Report templates are useful.

They are not results.

A report template should remain blank, marked `TBD`, or explicitly marked as a template until a real run fills it in.

## First real proof step

The first useful proof step is:

```text
run labinstall.bat on the target PC
save lab_smoke_test_report.json
save lab_pip_freeze.txt
record whether CUDA is visible to PyTorch
```

Only after that should the project say the lab environment installed successfully.
