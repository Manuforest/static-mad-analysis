from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path

from common import resolve_binary, run, write_json


def ratio(value: str | None) -> float | None:
    if not value or value == "0/0":
        return None
    return float(Fraction(value))


def main() -> None:
    parser = argparse.ArgumentParser(description="Probe a video and write a compact analysis manifest.")
    parser.add_argument("video")
    parser.add_argument("--output", required=True)
    parser.add_argument("--ffprobe")
    args = parser.parse_args()

    video = Path(args.video).resolve()
    ffprobe = resolve_binary("ffprobe", args.ffprobe)
    result = run([
        ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(video)
    ])
    import json
    raw = json.loads(result.stdout)
    visual = next((s for s in raw.get("streams", []) if s.get("codec_type") == "video"), {})
    audio = next((s for s in raw.get("streams", []) if s.get("codec_type") == "audio"), {})
    duration = float(raw.get("format", {}).get("duration") or visual.get("duration") or 0)
    manifest = {
        "source": str(video),
        "duration_seconds": duration,
        "video": {
            "codec": visual.get("codec_name"),
            "width": visual.get("width"),
            "height": visual.get("height"),
            "fps": ratio(visual.get("avg_frame_rate")),
            "frame_count": int(visual["nb_frames"]) if visual.get("nb_frames", "").isdigit() else None,
            "pixel_format": visual.get("pix_fmt"),
        },
        "audio": {
            "present": bool(audio),
            "codec": audio.get("codec_name"),
            "sample_rate": int(audio["sample_rate"]) if audio.get("sample_rate") else None,
            "channels": audio.get("channels"),
        },
    }
    write_json(Path(args.output), manifest)
    print(Path(args.output).resolve())


if __name__ == "__main__":
    main()
