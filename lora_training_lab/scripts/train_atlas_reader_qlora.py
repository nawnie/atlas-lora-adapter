#!/usr/bin/env python3
"""
Train Atlas Reader Mini with TRL + PEFT LoRA/QLoRA.

Status:
    Runnable training-layer script. It is intentionally defensive and supports
    dry-run validation before spending GPU time.

Typical dry run:
    python scripts/train_atlas_reader_qlora.py --config 06_experiments/training_configs/A_sanity_r8_lr0001.json --dry-run

Typical training run:
    python scripts/train_atlas_reader_qlora.py --config 06_experiments/training_configs/A_sanity_r8_lr0001.json

Expected dataset:
    JSONL with either:
      1. {"messages": [{"role": "system|user|assistant", "content": "..."}], ...}
      2. Atlas training-record schema from TRAINING_RECORD_SCHEMA_V1.json

If Atlas training records are provided, this script renders them into
conversational messages in memory before sending them to SFTTrainer.
"""

from __future__ import annotations

import argparse
import inspect
import json
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SYSTEM_MESSAGE = """You are Atlas Reader Mini.
Follow the Atlas Contract.
Primary lane first.
Use no more than 5 cards.
Use secondary lanes only when selected cards justify it.
Answer from evidence.
Do not invent exact commands, paths, node names, versions, licenses, or current facts.
Qualify missing or stale evidence."""


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def resolve_path(value: str | None) -> Optional[Path]:
    if not value:
        return None
    p = Path(value)
    if not p.is_absolute():
        p = ROOT / p
    return p


def filter_kwargs(cls_or_func: Any, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Drop kwargs not accepted by installed library version."""
    try:
        sig = inspect.signature(cls_or_func)
    except Exception:
        return kwargs
    allowed = set(sig.parameters)
    return {k: v for k, v in kwargs.items() if k in allowed}


def format_card(card: Dict[str, Any]) -> str:
    dnc = "; ".join(card.get("do_not_confuse_with", []) or [])
    return (
        f"- {card.get('card_id')} | lane={card.get('lane_id')} | type={card.get('card_type')} | title={card.get('title')}\n"
        f"  summary: {card.get('canonical_summary')}\n"
        f"  source_rule: {card.get('source_priority_rule')}\n"
        f"  do_not_confuse_with: {dnc}\n"
        f"  answer_pattern: {card.get('answer_pattern')}\n"
        f"  exactness_guard: {card.get('exactness_guard')}"
    )


def atlas_record_to_messages(record: Dict[str, Any]) -> Dict[str, Any]:
    pack = record.get("context_pack", {})
    cards = pack.get("cards", []) or []
    card_text = "\n\n".join(format_card(c) for c in cards)

    user = f"""Atlas Contract:
{record.get('contract_id', pack.get('contract_id', 'unknown'))}

User Query:
{record.get('user_query', '')}

Primary Lane:
{pack.get('primary_lane_id', '')}

Secondary Lanes:
{', '.join(pack.get('secondary_lane_ids', []) or []) or 'none'}

Context Pack:
{card_text}

Routing Rule:
{pack.get('routing_rule', 'Primary lane first.')}"""

    answer_obj = record.get("expected_answer", {})
    assistant = answer_obj.get("answer", "")
    limits = answer_obj.get("limits", "")
    if limits:
        assistant = assistant.rstrip() + "\n\nLimits: " + limits

    return {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_MESSAGE},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "metadata": {
            "record_id": record.get("record_id"),
            "record_type": record.get("record_type"),
            "primary_lane_id": pack.get("primary_lane_id"),
        },
    }


def detect_record_shape(example: Dict[str, Any]) -> str:
    if "messages" in example:
        return "messages"
    if "context_pack" in example and "expected_answer" in example:
        return "atlas_record"
    if "text" in example:
        return "text"
    raise ValueError("Dataset record must contain either `messages`, `text`, or Atlas training-record fields.")


def load_jsonl_records(path: Path) -> List[Dict[str, Any]]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
    return rows


def prepare_dataset(path: Path):
    from datasets import Dataset

    records = load_jsonl_records(path)
    if not records:
        raise ValueError(f"No records found in {path}")

    shape = detect_record_shape(records[0])
    if shape == "atlas_record":
        records = [atlas_record_to_messages(r) for r in records]
    elif shape == "messages":
        pass
    elif shape == "text":
        pass

    return Dataset.from_list(records), shape, len(records)


def get_git_commit() -> str:
    try:
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(ROOT), stderr=subprocess.DEVNULL, text=True)
        return out.strip()
    except Exception:
        return "not_available"


def collect_runtime_info() -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "platform": platform.platform(),
        "git_commit": get_git_commit(),
    }
    try:
        import torch
        info["torch_version"] = torch.__version__
        info["cuda_available"] = bool(torch.cuda.is_available())
        if torch.cuda.is_available():
            info["cuda_device_count"] = torch.cuda.device_count()
            info["cuda_device_name"] = torch.cuda.get_device_name(0)
            info["cuda_capability"] = torch.cuda.get_device_capability(0)
    except Exception as exc:
        info["torch_error"] = str(exc)

    for module_name in ["transformers", "datasets", "peft", "trl", "accelerate", "bitsandbytes"]:
        try:
            mod = __import__(module_name)
            info[f"{module_name}_version"] = getattr(mod, "__version__", "unknown")
        except Exception as exc:
            info[f"{module_name}_error"] = str(exc)

    return info


def sanity_check_config(config: Dict[str, Any]) -> List[str]:
    issues: List[str] = []
    train_path = resolve_path(config.get("dataset_train"))
    eval_path = resolve_path(config.get("dataset_eval"))

    if not config.get("base_model") or config.get("base_model") == "REPLACE_WITH_BASE_MODEL":
        issues.append("base_model is not set. Replace REPLACE_WITH_BASE_MODEL with a real local path or HF model ID.")
    if not train_path or not train_path.exists():
        issues.append(f"dataset_train not found: {train_path}")
    if eval_path and not eval_path.exists():
        issues.append(f"dataset_eval not found: {eval_path}")

    lora = config.get("lora", {})
    if int(lora.get("r", 0)) <= 0:
        issues.append("lora.r must be > 0")
    if not lora.get("target_modules"):
        issues.append("lora.target_modules is empty")

    return issues


def maybe_build_quant_config(config: Dict[str, Any]):
    quant = config.get("quantization", {})
    if not quant.get("load_in_4bit"):
        return None

    import torch
    from transformers import BitsAndBytesConfig

    dtype_name = str(quant.get("bnb_4bit_compute_dtype", "float16")).lower()
    if "bf16" in dtype_name and torch.cuda.is_available() and torch.cuda.is_bf16_supported():
        compute_dtype = torch.bfloat16
    else:
        compute_dtype = torch.float16

    return BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type=quant.get("bnb_4bit_quant_type", "nf4"),
        bnb_4bit_use_double_quant=bool(quant.get("bnb_4bit_use_double_quant", True)),
        bnb_4bit_compute_dtype=compute_dtype,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, type=Path, help="Training config JSON")
    parser.add_argument("--dry-run", action="store_true", help="Validate config/datasets/imports without training")
    parser.add_argument("--resume-from-checkpoint", default=None)
    parser.add_argument("--allow-scaffold", action="store_true", help="Allow sample/scaffold datasets; otherwise warn only")
    args = parser.parse_args()

    config_path = args.config if args.config.is_absolute() else ROOT / args.config
    config = load_json(config_path)

    run_id = config.get("run_id", config_path.stem)
    output_dir = resolve_path(config.get("adapter_output_dir")) or (ROOT / "06_experiments" / "runs" / run_id / "adapter")
    run_dir = output_dir.parent
    run_dir.mkdir(parents=True, exist_ok=True)
    tensorboard_dir = run_dir / "tensorboard"

    runtime_info = collect_runtime_info()
    write_json(run_dir / "runtime_info.json", runtime_info)
    shutil.copy2(config_path, run_dir / "config_used.json")

    issues = sanity_check_config(config)
    if issues:
        print("CONFIG ISSUES:")
        for issue in issues:
            print(f"- {issue}")
        print()
        print("Dry-run failed before training.")
        return 2

    train_path = resolve_path(config.get("dataset_train"))
    eval_path = resolve_path(config.get("dataset_eval"))

    print(f"Run ID: {run_id}")
    print(f"Config: {config_path}")
    print(f"Output: {output_dir}")
    print(f"Train dataset: {train_path}")
    print(f"Eval dataset: {eval_path}")

    if args.dry_run:
        train_records = load_jsonl_records(train_path)
        shape = detect_record_shape(train_records[0])
        print(f"Dry-run dataset shape: {shape}")
        print(f"Dry-run train records: {len(train_records)}")
        if eval_path:
            eval_records = load_jsonl_records(eval_path)
            print(f"Dry-run eval records: {len(eval_records)}")
        print("Dry-run passed. No model loaded and no training started.")
        return 0

    # Heavy imports happen only after dry-run checks.
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import LoraConfig, prepare_model_for_kbit_training
    from trl import SFTConfig, SFTTrainer

    train_dataset, train_shape, train_count = prepare_dataset(train_path)
    eval_dataset = None
    eval_shape = None
    eval_count = 0
    if eval_path:
        eval_dataset, eval_shape, eval_count = prepare_dataset(eval_path)

    tokenizer = AutoTokenizer.from_pretrained(config["base_model"], trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    quant_config = maybe_build_quant_config(config)

    model_kwargs = {
        "trust_remote_code": True,
        "device_map": "auto",
    }
    if quant_config is not None:
        model_kwargs["quantization_config"] = quant_config
    else:
        model_kwargs["torch_dtype"] = torch.float16

    model = AutoModelForCausalLM.from_pretrained(config["base_model"], **model_kwargs)
    if quant_config is not None:
        model = prepare_model_for_kbit_training(model)

    lora_cfg = LoraConfig(
        r=int(config["lora"]["r"]),
        lora_alpha=int(config["lora"]["lora_alpha"]),
        lora_dropout=float(config["lora"].get("lora_dropout", 0.05)),
        bias=config["lora"].get("bias", "none"),
        task_type=config["lora"].get("task_type", "CAUSAL_LM"),
        target_modules=config["lora"]["target_modules"],
    )

    train_cfg = config.get("training", {})
    sft_kwargs = {
        "output_dir": str(output_dir),
        "tensorboard_dir": str(tensorboard_dir),
        "num_train_epochs": train_cfg.get("num_train_epochs", 1),
        "per_device_train_batch_size": train_cfg.get("per_device_train_batch_size", 1),
        "per_device_eval_batch_size": train_cfg.get("per_device_eval_batch_size", 1),
        "gradient_accumulation_steps": train_cfg.get("gradient_accumulation_steps", 8),
        "learning_rate": train_cfg.get("learning_rate", 0.0001),
        "warmup_ratio": train_cfg.get("warmup_ratio", 0.05),
        "max_grad_norm": train_cfg.get("max_grad_norm", 1.0),
        "lr_scheduler_type": train_cfg.get("lr_scheduler_type", "cosine"),
        "logging_steps": train_cfg.get("logging_steps", 10),
        "eval_steps": train_cfg.get("eval_steps", 50),
        "save_steps": train_cfg.get("save_steps", 50),
        "save_total_limit": train_cfg.get("save_total_limit", 2),
        "gradient_checkpointing": train_cfg.get("gradient_checkpointing", True),
        "packing": train_cfg.get("packing", False),
        "assistant_only_loss": train_cfg.get("assistant_only_loss", True),
        "report_to": train_cfg.get("report_to", "none"),
        "logging_dir": str(resolve_path(train_cfg.get("logging_dir")) or tensorboard_dir),
        "seed": train_cfg.get("seed", 42),
    }

    # TRL versions may call this max_length or max_seq_length depending on release.
    sft_sig = inspect.signature(SFTConfig)
    if "max_length" in sft_sig.parameters:
        sft_kwargs["max_length"] = train_cfg.get("max_length", 2048)
    elif "max_seq_length" in sft_sig.parameters:
        sft_kwargs["max_seq_length"] = train_cfg.get("max_length", 2048)

    if eval_dataset is not None:
        sft_kwargs["eval_strategy"] = "steps"
        if "evaluation_strategy" in sft_sig.parameters:
            sft_kwargs.pop("eval_strategy", None)
            sft_kwargs["evaluation_strategy"] = "steps"

    sft_args = SFTConfig(**filter_kwargs(SFTConfig, sft_kwargs))

    trainer_kwargs = {
        "model": model,
        "args": sft_args,
        "train_dataset": train_dataset,
        "eval_dataset": eval_dataset,
        "peft_config": lora_cfg,
    }
    trainer_sig = inspect.signature(SFTTrainer)
    if "processing_class" in trainer_sig.parameters:
        trainer_kwargs["processing_class"] = tokenizer
    elif "tokenizer" in trainer_sig.parameters:
        trainer_kwargs["tokenizer"] = tokenizer

    trainer = SFTTrainer(**filter_kwargs(SFTTrainer, trainer_kwargs))

    print("Starting training...")
    train_result = trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)
    print("Training complete.")

    trainer.save_model(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))

    metrics = train_result.metrics if hasattr(train_result, "metrics") else {}
    write_json(run_dir / "train_metrics.json", dict(metrics))

    summary = {
        "run_id": run_id,
        "base_model": config["base_model"],
        "output_dir": str(output_dir),
        "train_dataset": str(train_path),
        "eval_dataset": str(eval_path) if eval_path else None,
        "train_shape": train_shape,
        "eval_shape": eval_shape,
        "train_count": train_count,
        "eval_count": eval_count,
        "training_finished_utc": datetime.now(timezone.utc).isoformat(),
        "metrics": dict(metrics),
    }
    write_json(run_dir / "run_summary.json", summary)
    print(f"Saved adapter and run summary to: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
