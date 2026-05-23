# Canonical Overview — Agent Systems, Tool Use, and MCP

Agent systems are not just chatbots with bigger prompts. They are stateful software systems where the model selects tools, receives tool outputs, and continues reasoning. MCP is an open standard for connecting AI applications to data sources and tools through clients and servers. The adapter should prefer explicit tool schemas, validation, limited permissions, and state-machine orchestration over unbounded autonomous loops.

## Practitioner framing
This lane should be used as a decision-support layer, not as an isolated essay. It maps concepts to concrete AIWF use cases: local-first assistants, Atlas systems, Gradio tools, ComfyUI support agents, dataset QA, and small-model augmentation.

## Core concepts
- tool calling
- function calling
- structured output
- JSON schema
- MCP server
- MCP client
- resources
- prompts
- planner
- executor
- ReAct
- Plan-and-Execute
- LangGraph
- stateful agent
- human approval gate

## Source-backed anchors
- Anthropic Model Context Protocol announcement: https://www.anthropic.com/news/model-context-protocol
- OpenAI function calling guide: https://developers.openai.com/api/docs/guides/function-calling
- OpenAI structured outputs guide: https://developers.openai.com/api/docs/guides/structured-outputs
- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangChain project: https://github.com/langchain-ai/langchain

## Freshness policy
- Foundational concepts are `stable` or `slow_changing`.
- Current tools, model families, security advisories, and platform behavior are `fast_moving` or `volatile`.
- If a user asks for latest versions, prices, benchmarks, vulnerabilities, or release status, the assistant should verify current sources before finalizing the answer.
