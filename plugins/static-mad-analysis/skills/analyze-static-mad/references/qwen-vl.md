# Optional Qwen video-language model

Use Qwen as a provisional observer for OCR, coarse chaptering, recurring objects, and candidate intervals. Local frames, audio, and evidence records remain authoritative.

## Configuration

Set secrets only in the caller's environment:

```powershell
$env:QWEN_API_KEY = "your-own-key"
$env:QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
$env:QWEN_MODEL = "your-video-capable-model"
```

Token Plan users can override `QWEN_BASE_URL` with the endpoint supplied by their subscription. Do not embed a key, read another user's key file, or commit `.env` files.

## Cost gate

Always run `call_qwen_vl.py --dry-run` first. Its estimate is deliberately conservative and empirical, not provider pricing: approximately 225 video tokens per sampled 480p frame was observed in one August 2026 test. Resolution, codec, provider preprocessing, and model revisions can change this value.

Ask for confirmation before `--send`, especially when the estimate exceeds 50,000 video tokens. The API response's `usage` object reports tokens, but subscription Credits may use a separate dynamic conversion.

## Recommended passes

1. Whole video at 0.5–1 fps: provisional entities, chapters, OCR, motifs, and uncertainty only.
2. Local contact sheets: verify subject identity and locate true shot boundaries.
3. Short intervals at 2–4 fps: inspect edits that remain ambiguous.
4. Original-rate local frames around ±0.5 seconds: verify inserts, match cuts, and action phase.

Do not send an entire video at 4–8 fps merely because the first pass was uncertain.

## Reliability rules

- Reject an asserted continuous action when intervening frames show composition, background, or source-image changes.
- Separate a character's action from crop, pan, zoom, parallax, masking, blur, and typography.
- Treat VLM names and source-plot claims as provisional until grounded in visible text or multiple anchors.
- If the VLM description conflicts with the contact sheet, preserve the conflict and prefer directly inspected frames.
- Ask the VLM for observations and alternatives before asking for a polished narrative.
