# Gap Audit and Vol. 2 Queue — ComfyUI Workflow API Automation and Gradio Bridge Patterns

## Current coverage

This Vol. 1 lane covers the local automation model and Gradio bridge design. It is sufficient for assistant guidance and simple app scaffolding.

## Vol. 2 expansion candidates

- complete Python client with WebSocket progress handling
- hardened upload and temp-file manager
- workflow contract generator that maps node IDs to safe UI controls
- Gradio reference app with image, mask, and video outputs
- local/LAN security patterns for phone-based control
- test harness for comparing API payloads against expected workflow outputs

## Risk notes

Hosted ComfyUI providers may wrap ComfyUI differently. For provider-specific advice, verify that provider's current API documentation before answering.
