from __future__ import annotations

import argparse
import re
from pathlib import Path

from common import read_json, resolve_binary, run, write_json


PTS = re.compile(r"pts_time:([0-9.]+)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect candidate cuts with FFmpeg scene scores.")
    parser.add_argument("video")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--threshold", type=float, default=0.22)
    parser.add_argument("--min-gap", type=float, default=0.10)
    parser.add_argument("--ffmpeg")
    args = parser.parse_args()

    ffmpeg = resolve_binary("ffmpeg", args.ffmpeg)
    manifest = read_json(Path(args.manifest))
    duration = float(manifest["duration_seconds"])
    proc = run([
        ffmpeg, "-hide_banner", "-i", str(Path(args.video).resolve()),
        "-vf", f"select='gt(scene,{args.threshold})',showinfo", "-an", "-f", "null", "-"
    ])
    times = [0.0]
    for line in proc.stderr.splitlines():
        match = PTS.search(line)
        if match:
            value = float(match.group(1))
            if value - times[-1] >= args.min_gap and value < duration:
                times.append(value)
    if duration > times[-1]:
        times.append(duration)
    shots = []
    for index, (start, end) in enumerate(zip(times, times[1:]), 1):
        shots.append({
            "shot_id": index,
            "start": round(start, 3),
            "end": round(end, 3),
            "duration": round(end - start, 3),
            "representative_time": round((start + end) / 2, 3),
            "status": "candidate",
        })
    payload = {"threshold": args.threshold, "cut_times": times[1:-1], "shots": shots}
    write_json(Path(args.output), payload)
    print(f"{len(shots)} candidate shots -> {Path(args.output).resolve()}")


if __name__ == "__main__":
    main()
