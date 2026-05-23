# Atlas Reader LoRA

## A mapped knowledge system for teaching AI models how to read structured RAG

A normal AI model is like a brain that learned patterns from a massive amount of text. It can reason and explain things, but it does not automatically know the exact structure of a project, which files matter most, which sources should be trusted, or when something is outdated.

A normal RAG system helps by giving the AI reference material. That is basically like handing the AI a big box of notes and saying, “Search through this before you answer.”

That helps, but it is still messy. Old notes, strong sources, weak sources, examples, rules, and outdated information can all get mixed together.

So instead of just making a pile of reference files, this project uses an **Atlas**.

The Atlas is like a mapped road system around the knowledge. Each subject gets a lane. One lane might be for ComfyUI workflow errors. Another might be for CUDA and Torch issues. Another might be for video memory problems. Another might be for source quality.

The lanes tell the AI things like:

- This kind of question belongs here.
- This source is stronger than that source.
- This older note should not override this newer rule.
- Do not invent exact commands, file paths, or node names.
- If the answer is uncertain, say so.
- If the issue is about one type of problem, do not confuse it with another type of problem.

So the AI is no longer just reading random chunks of text. It is following a map.

## The Atlas Reader LoRA

The next idea is called the **Atlas Reader LoRA**.

A LoRA is a small training adapter that can change how an AI model behaves without retraining the whole model.

The goal is **not** to train it to memorize all the facts in the Atlas. Facts change. Software versions change. APIs change.

Instead, the goal is to train it to understand how to read an Atlas-style knowledge system.

That means teaching it to:

- route the question to the right lane;
- rank sources by trust level;
- ignore weak or outdated notes;
- notice missing evidence;
- avoid making things up;
- choose the right kind of answer;
- warn when something needs current verification.

The knowledge stays in the RAG.

The reading behavior goes into the LoRA.

The testing system checks whether it actually works.

## Simple version

A normal RAG gives the AI a pile of notes.

An Atlas gives the AI a map.

The Atlas Reader LoRA teaches the AI how to read the map.

That is the project.

## Why 128 validated lanes

The project target is around **128 validated lanes** before serious LoRA training.

The reason is simple: the model needs enough examples to learn the pattern. If it is trained on only a few topics, it may just memorize those topics. But if it is trained across many different lanes, it has a better chance of learning the actual skill:

> how to use structured knowledge correctly.

Even if the LoRA training fails, the data from testing may still be useful. It can show how small AI models handle structured knowledge, where they fail, whether lane routing improves answers, and whether better organization can help smaller models perform closer to larger ones.

## One-sentence version

This project builds a mapped knowledge system around RAG, then trains a small adapter to teach AI models how to follow the lanes, trust the right sources, and answer from structured evidence instead of guessing.
