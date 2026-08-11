# Static MAD Analysis for Codex

An evidence-first Codex skill and plugin for understanding 静止系 MAD, manga MAD, image-based AMV/MV, and other highly edited narrative video.

It treats video understanding as reconstruction rather than frame captioning: coarse-to-fine sampling, subject and identity tracking, shot-relation classification, five separate clocks, montage grammar, audio profiling, alternative hypotheses, and timestamped evidence.

## What it includes

- adaptive FFmpeg frame sampling and candidate cut detection;
- timestamped contact sheets;
- lightweight audio energy and spectral profiles;
- entity, relation, observation, timeline, and hypothesis records;
- a static-MAD critique rubric;
- optional Qwen video analysis with an explicit upload gate, environment-only keys, token estimation, and usage reporting;
- safeguards against turning cuts, crops, parallax, and typography into invented character motion.

## Requirements

- Codex desktop or Codex CLI;
- Python 3.10+;
- FFmpeg and FFprobe on `PATH`, or configured with `STATIC_MAD_FFMPEG` and `STATIC_MAD_FFPROBE`;
- Python packages from `requirements.txt`;
- optionally, a user-owned Qwen/DashScope API key and video-capable model.

```powershell
python -m pip install -r requirements.txt
```

## Install the plugin

Clone the repository, register it as a local marketplace, and install the plugin:

```powershell
git clone https://github.com/Manuforest/static-mad-analysis.git
codex plugin marketplace add ./static-mad-analysis
codex plugin add static-mad-analysis@static-mad-analysis
```

Start a new Codex task after installation.

## Install only the skill

Ask Codex:

```text
Use $skill-installer to install analyze-static-mad from
https://github.com/Manuforest/static-mad-analysis/tree/main/plugins/static-mad-analysis/skills/analyze-static-mad
```

Alternatively, copy `plugins/static-mad-analysis/skills/analyze-static-mad` into a Codex user or repository skill directory.

## Use

Invoke `$analyze-static-mad` with a local video or an authorized video URL. Typical requests:

```text
Use $analyze-static-mad to reconstruct the subjects, time-space relations,
montage, and audio-visual rhythm of this video with timestamped evidence.
```

```text
Use $analyze-static-mad to critique this static MAD and explain every score deduction.
```

The deterministic first pass can also be run directly:

```powershell
python plugins/static-mad-analysis/skills/analyze-static-mad/scripts/prepare_analysis.py `
  input.mp4 --output-dir analysis-output
```

## Optional Qwen pass

Do not put keys in scripts, command-line arguments, prompt files, or the repository. Set one only in the current process environment:

```powershell
$env:QWEN_API_KEY = "your-own-key"
$env:QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
$env:QWEN_MODEL = "your-video-capable-model"
```

Estimate before uploading:

```powershell
python plugins/static-mad-analysis/skills/analyze-static-mad/scripts/call_qwen_vl.py `
  input.mp4 --fps 1 --dry-run
```

Only after reviewing the estimate and authorizing the external upload:

```powershell
python plugins/static-mad-analysis/skills/analyze-static-mad/scripts/call_qwen_vl.py `
  input.mp4 --prompt-file prompt.txt --fps 1 --send --output qwen-result.json
```

The token estimate is empirical and is not a provider price quote. Qwen responses remain hypotheses until checked against local adjacent frames and shot boundaries.

## Privacy and copyright

The local preparation scripts do not upload video. The optional Qwen script uploads the selected video to the endpoint configured by the user only when `--send` is present. Users are responsible for authorization to access, download, process, and upload each video. No videos, cookies, account sessions, API keys, or extracted test frames are included in this repository.

## License

MIT. See [LICENSE](LICENSE).
