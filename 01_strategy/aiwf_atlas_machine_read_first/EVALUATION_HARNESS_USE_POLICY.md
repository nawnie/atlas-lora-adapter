# Evaluation Harness Use Policy

The evaluation harness is the proof layer for the AIWF Atlas. Use it to compare adapter-backed answers against raw-file retrieval and no-RAG baselines.

## Use It For

- checking whether Atlas cards improve answer quality
- testing citation discipline
- testing beginner-safe troubleshooting
- checking whether AIWF voice improves clarity without covering weak facts in confetti
- catching stale, unsupported, or overconfident claims

## Do Not Use It For

- replacing source verification
- treating a passing answer as permanent truth
- scoring humor higher than accuracy
- hiding uncertainty behind mascot energy

## Required Rule

If an answer fails on source grounding, version awareness, or safety, it fails the evaluation even if it sounds helpful. A charming hallucination is still a hallucination wearing a tiny tool belt.
