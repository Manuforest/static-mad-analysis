# Static MAD Analysis for Codex

An evidence-first Codex skill and plugin for understanding 静止系 MAD, with provisional AMV and ASMV extensions.

It separates a shared subject-centered understanding core from media-specific adapters. The static-MAD adapter is the current supported path. AMV and ASMV adapters are exploratory extensions: they are loaded only when explicitly requested, their terminology may change, and they should not be treated as complete theories or settled standards.

## What it includes

- adaptive FFmpeg frame sampling and candidate cut detection;
- a chronological shot-by-shot MAD reading layer that verifies candidate cuts, supports dense shot clusters, and separates source contribution from editorial contribution;
- timestamped contact sheets;
- lightweight audio energy and spectral profiles;
- entity, subject-role, relation, observation, timeline, and hypothesis records;
- a three-layer interpretation workflow separating video-body evidence, original-work context, and documented creator expression;
- source-context mapping for character and route identity, original chronology, and editorial transformation without fidelity or competition scoring;
- integrated craft analysis that includes graphic design, virtual camera, motion design, 3D/spatial construction, compositing, transitions, atmosphere, and technical spectacle without forcing narrative utility;
- a static-MAD adapter for constructed motion, material treatment, typography, and compositing;
- a provisional AMV extension for separating source-footage continuity from edit-created relations;
- a provisional ASMV extension for speaker, addressee, assigned narrator, and discourse-position analysis;
- optional Qwen video analysis with an explicit upload gate, environment-only keys, token estimation, and usage reporting;
- safeguards against invented motion, imported source causality, and false speech attribution;
- intent-sensitive output for detailed reports, exposed 拉片 records, and evidence-grounded human-centered appreciation prose.

## Requirements

- Codex desktop or Codex CLI;
- Python 3.10+;
- FFmpeg and FFprobe on `PATH`, or configured with `STATIC_MAD_FFMPEG` and `STATIC_MAD_FFPROBE`;
- Python packages from `requirements.txt`;
- `yt-dlp` for acquiring authorized public video URLs;
- optionally, a user-owned Qwen/DashScope API key and video-capable model.

```powershell
python -m pip install -r requirements.txt
```

For a skill-only installation, install the requirements bundled inside the skill:

```powershell
python -m pip install -r <skill-directory>/requirements.txt
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

The default analysis order is a blind video pass, a focused original-work context pass, and a separate creator-expression pass. Ask for `video-only` when source research should be omitted.

```text
Use $analyze-static-mad to reconstruct the subjects, time-space relations,
montage, and audio-visual rhythm of this video with timestamped evidence.
```

```text
Use $analyze-static-mad to analyze this ASMV by separating the visible subject,
original speaker, assigned narrator, discourse subject, and editorial position.
```

```text
Use $analyze-static-mad to 拉片 this static MAD, then write a natural appreciation
that selects the most revealing passages instead of reproducing the full shot log.
```

For a public URL, the skill attempts the highest available resolution within the requested limit before asking for a manually downloaded file. It stores the media, selected format, actual resolution, access mode, and public metadata in the analysis workspace. Browser cookies are optional and may be used only after explicit authorization. Limits of a low-resolution or platform-transcoded copy are kept separate from evaluation of the work.

The deterministic first pass can also be run directly:

```powershell
python plugins/static-mad-analysis/skills/analyze-static-mad/scripts/prepare_analysis.py `
  input.mp4 --output-dir analysis-output
```

The same entry point accepts an authorized URL:

```powershell
python plugins/static-mad-analysis/skills/analyze-static-mad/scripts/prepare_analysis.py `
  "https://www.bilibili.com/video/BV.../" --output-dir analysis-output
```

To test URL support without downloading the media:

```powershell
python plugins/static-mad-analysis/skills/analyze-static-mad/scripts/fetch_video.py `
  "https://www.bilibili.com/video/BV.../" --output-dir analysis-output/source --metadata-only
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
