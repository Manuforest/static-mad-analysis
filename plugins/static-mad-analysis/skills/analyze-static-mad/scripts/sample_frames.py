from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from common import read_json, resolve_binary, run


def extract_segment(ffmpeg: str, video: Path, target: Path, start: float, end: float, fps: float, prefix: str) -> list[dict]:
    target.mkdir(parents=True, exist_ok=True)
    pattern = target / f"{prefix}_%06d.jpg"
    run([
        ffmpeg, "-hide_banner", "-loglevel", "error", "-ss", f"{start:.3f}",
        "-i", str(video), "-t", f"{max(0.001, end-start):.3f}", "-vf", f"fps={fps}",
        "-q:v", "2", str(pattern)
    ])
    rows = []
    files = sorted(target.glob(f"{prefix}_*.jpg"))
    for i, file in enumerate(files):
        rows.append({"file": str(file.resolve()), "time": round(start + i / fps, 3), "fps": fps, "source": prefix})
    return rows


def parse_focus(value: str) -> tuple[float, float, float]:
    match = re.fullmatch(r"([0-9.]+):([0-9.]+):([0-9.]+)", value)
    if not match:
        raise argparse.ArgumentTypeError("focus must be START:END:FPS")
    return tuple(map(float, match.groups()))


def main() -> None:
    parser = argparse.ArgumentParser(description="Create global and adaptive frame samples.")
    parser.add_argument("video")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--shots")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-fps", type=float, default=1.0)
    parser.add_argument("--cut-fps", type=float, default=4.0)
    parser.add_argument("--cut-radius", type=float, default=0.5)
    parser.add_argument("--focus", action="append", type=parse_focus, default=[])
    parser.add_argument("--ffmpeg")
    args = parser.parse_args()

    video = Path(args.video).resolve()
    output = Path(args.output_dir).resolve()
    manifest = read_json(Path(args.manifest))
    duration = float(manifest["duration_seconds"])
    ffmpeg = resolve_binary("ffmpeg", args.ffmpeg)
    rows = extract_segment(ffmpeg, video, output / "overview", 0, duration, args.base_fps, "overview")

    focus = list(args.focus)
    if args.shots:
        shot_data = read_json(Path(args.shots))
        for cut in shot_data.get("cut_times", []):
            focus.append((max(0, cut - args.cut_radius), min(duration, cut + args.cut_radius), args.cut_fps))

    for index, (start, end, fps) in enumerate(focus, 1):
        if end <= start:
            continue
        rows.extend(extract_segment(ffmpeg, video, output / "focus", start, end, fps, f"focus_{index:04d}"))

    rows.sort(key=lambda row: (row["time"], row["source"]))
    with (output / "frames.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "time", "fps", "source"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} sampled frames -> {output}")


if __name__ == "__main__":
    main()
