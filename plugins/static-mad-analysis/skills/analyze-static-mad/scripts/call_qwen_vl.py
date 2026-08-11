from __future__ import annotations

import argparse
import base64
import json
import math
import os
import urllib.error
import urllib.request
from pathlib import Path

from common import resolve_binary, run, write_json


DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"


def video_duration(video: Path, ffprobe: str | None) -> float:
    binary = resolve_binary("ffprobe", ffprobe)
    proc = run([
        binary,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(video),
    ])
    return float(proc.stdout.strip())


def estimate(duration: float, fps: float, tokens_per_frame: float) -> dict[str, float | int]:
    sampled_frames = math.ceil(duration * fps)
    return {
        "duration_seconds": round(duration, 3),
        "fps": fps,
        "estimated_sampled_frames": sampled_frames,
        "estimated_video_tokens": math.ceil(sampled_frames * tokens_per_frame),
        "assumed_tokens_per_frame": tokens_per_frame,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Estimate or send a video to a Qwen OpenAI-compatible multimodal endpoint."
    )
    parser.add_argument("video")
    parser.add_argument("--prompt-file")
    parser.add_argument("--fps", type=float, default=1.0)
    parser.add_argument("--model", default=os.environ.get("QWEN_MODEL", "qwen3.6-flash"))
    parser.add_argument("--base-url", default=os.environ.get("QWEN_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--max-output-tokens", type=int, default=1800)
    parser.add_argument("--tokens-per-frame", type=float, default=225.0)
    parser.add_argument("--confirm-above-video-tokens", type=int, default=50_000)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--ffprobe")
    parser.add_argument("--output")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--yes", action="store_true", help="Confirm an estimate above the safety threshold")
    args = parser.parse_args()

    if args.fps <= 0 or args.tokens_per_frame <= 0:
        parser.error("--fps and --tokens-per-frame must be positive")
    if args.dry_run and args.send:
        parser.error("choose either --dry-run or --send")

    video = Path(args.video).resolve()
    if not video.is_file():
        parser.error(f"video not found: {video}")

    duration = video_duration(video, args.ffprobe)
    budget = estimate(duration, args.fps, args.tokens_per_frame)
    preflight = {
        "mode": "preflight",
        "video_name": video.name,
        "input_file_bytes": video.stat().st_size,
        "model": args.model,
        "base_url": args.base_url,
        "estimate": budget,
        "warning": "Empirical token estimate only; provider billing and Credits may differ.",
    }

    if args.dry_run or not args.send:
        print(json.dumps(preflight, ensure_ascii=False, indent=2))
        return

    if not args.prompt_file:
        parser.error("--prompt-file is required with --send")
    estimated_tokens = int(budget["estimated_video_tokens"])
    if estimated_tokens > args.confirm_above_video_tokens and not args.yes:
        raise SystemExit(
            f"Estimated video tokens ({estimated_tokens}) exceed the safety threshold "
            f"({args.confirm_above_video_tokens}). Obtain user approval, then rerun with --yes."
        )

    key = os.environ.get("QWEN_API_KEY") or os.environ.get("DASHSCOPE_API_KEY")
    if not key:
        raise SystemExit("Set QWEN_API_KEY or DASHSCOPE_API_KEY in the environment before --send.")

    prompt_path = Path(args.prompt_file).resolve()
    if not prompt_path.is_file():
        parser.error(f"prompt file not found: {prompt_path}")
    prompt = prompt_path.read_text(encoding="utf-8")
    encoded_video = base64.b64encode(video.read_bytes()).decode("ascii")
    payload = {
        "model": args.model,
        "messages": [{
            "role": "user",
            "content": [
                {
                    "type": "video_url",
                    "video_url": {"url": f"data:video/mp4;base64,{encoded_video}"},
                    "fps": args.fps,
                },
                {"type": "text", "text": prompt},
            ],
        }],
        "enable_thinking": False,
        "temperature": 0.1,
        "max_tokens": args.max_output_tokens,
    }
    request = urllib.request.Request(
        f"{args.base_url.rstrip('/')}/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Qwen request failed with HTTP {error.code}: {detail}") from error
    finally:
        key = ""

    output = {
        "request": preflight,
        "response": {
            "model": result.get("model"),
            "usage": result.get("usage"),
            "content": ((result.get("choices") or [{}])[0].get("message") or {}).get("content"),
        },
    }
    if args.output:
        write_json(Path(args.output).resolve(), output)
        print(Path(args.output).resolve())
    else:
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
