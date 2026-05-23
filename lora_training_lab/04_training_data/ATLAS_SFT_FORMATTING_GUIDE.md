# Atlas SFT Formatting Guide

Status: planning  
Version added: v0.2.9-dev6

## Goal

Convert Atlas training records into chat-style SFT examples.

## Recommended chat shape

Use a system message for the Atlas contract and behavior.

Use a user message for the query and context pack.

Use an assistant message for the expected answer.

## System message template

```text
You are Atlas Reader Mini.
Follow the Atlas Contract.
Primary lane first.
Use no more than 5 cards.
Use secondary lanes only when selected cards justify it.
Answer from evidence.
Do not invent exact commands, paths, node names, versions, licenses, or current facts.
Qualify missing or stale evidence.
```

## User message template

```text
Atlas Contract:
{contract_id}

User Query:
{user_query}

Context Pack:
{cards}

Expected routing discipline:
{routing_rule}
```

## Assistant message

This should be the actual useful answer.

Do not train final runs on assistant messages that only say:

```text
Route this to lane X.
Use selected cards.
```

Those are scaffold answers.
