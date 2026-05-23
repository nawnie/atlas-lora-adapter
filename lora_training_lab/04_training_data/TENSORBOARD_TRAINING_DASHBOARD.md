# TensorBoard Training Dashboard

Status: implemented dashboard support  
Version added: v0.2.9-dev12  
Purpose: local browser dashboard for training metrics.

## What this is

The training statistics window is **TensorBoard**.

It runs locally in a browser and shows training graphs such as:

```text
loss
eval_loss
learning_rate
epoch
grad_norm
runtime / steps per second
```

Depending on what the trainer logs, these appear in TensorBoard under Scalars or Time Series.

## Why it matters for Atlas Reader LoRA

The smoke train should not be judged by vibes.

TensorBoard gives a quick view of whether training is behaving normally:

- loss decreasing too fast;
- loss not moving;
- eval loss rising while train loss falls;
- learning rate schedule doing what the config says;
- training collapse;
- suspicious overfit patterns.

## How it is enabled

Training configs now default to:

```json
"report_to": "tensorboard",
"logging_dir": "06_experiments/runs/<run_id>/tensorboard"
```

The training script passes `logging_dir` into TRL/Hugging Face training arguments when supported.

## Start TensorBoard

From repo root:

```powershell
tools\powershell\start_tensorboard.ps1
```

Default URL:

```text
http://127.0.0.1:6006
```

Custom port:

```powershell
tools\powershell\start_tensorboard.ps1 -Port 6007
```

## Check for event files

After a training run:

```powershell
python scripts\list_tensorboard_runs.py
```

Expected event files look like:

```text
06_experiments/runs/<run_id>/tensorboard/events.out.tfevents...
```

## What to watch

### Healthy-ish signs

```text
training loss trends downward
learning rate follows expected schedule
eval loss does not explode
steps/sec is stable
```

### Warnings

```text
train loss drops but eval loss rises quickly
loss becomes NaN
learning rate is zero unexpectedly
learning rate spikes unexpectedly
loss flatlines from the start
```

### Atlas-specific warnings

```text
model repeats lane IDs instead of answering
model learns scaffold/meta phrasing
model overuses secondary lanes
model ignores freshness warnings
model invents exact commands or versions
```

TensorBoard cannot detect those Atlas-specific failures by itself. Use the smoke-eval protocol and answer review for that.

## Source basis

TensorBoard is documented as a visualization/measurement tool for machine-learning workflows, and its Scalars/Time Series dashboards track values such as loss, metrics, training speed, and learning rate [tensorboard_get_started].

Hugging Face Transformers documents `TensorBoardCallback`, which sends trainer logs to TensorBoard, and notes `TENSORBOARD_LOGGING_DIR` / output-dir based logging behavior [hf_transformers_callbacks].

## Pre-install / no-results guard

This project has not yet been installed on the target PC.

No adapter has been trained.

No evaluation result exists yet.

Prepared scripts, templates, and diagrams are not wins; they are the test bench.
