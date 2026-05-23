# Terminology

## Atlas

A source-aware, lane-routed knowledge map designed to help AI systems retrieve, judge, and apply domain knowledge without treating every document chunk as equally trustworthy.

## Lane

A bounded topic area with its own scope, source coverage, retrieval cards, failure signatures, answer patterns, and tests.

## Retrieval card

A compact routing and answer-support record that tells the model when to use a topic, what evidence matters, what to avoid, and how to answer.

## Source hierarchy

The rule that not all retrieved context is equal. Canonical guidance usually outranks old archives, loose notes, and release history.

## Failure signature

A recognizable error pattern or bad-output pattern that routes to a diagnostic lane.

## Atlas Reader LoRA

A LoRA trained to improve how a model reads structured RAG context.

## Raw RAG

A retrieval setup where files are chunked and retrieved without strong lane, source-priority, or answer-pattern structure.

## Atlas RAG

A retrieval setup that uses lanes, source roles, retrieval cards, and metadata to guide answer behavior.
