from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

from fetch_video import fetch_video


def call(script: Path, *args: str) -> None:
    subprocess.run([sys.executable, str(script), *args], check=True)


def is_http_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> None:
    parser = argparse.ArgumentParser(description="Acquire if needed and prepare deterministic artifacts for a static-MAD analysis.")
    parser.add_argument("video", help="Local media path or authorized HTTP/HTTPS video URL")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--scene-threshold", default="0.22")
    parser.add_argument("--base-fps", default="1")
    parser.add_argument("--cut-fps", default="4", help="Automatic sampling rate around candidate cuts")
    parser.add_argument("--focus", action="append", default=[], help="Optional START:END:FPS interval")
    parser.add_argument("--max-height", type=int, default=1080, help="Maximum preferred height for URL acquisition")
    parser.add_argument("--cookies-from-browser", help="Use a local browser session only with explicit user authorization")
    parser.add_argument("--download-ffmpeg-location", help="Optional FFmpeg executable or directory passed to yt-dlp")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    if is_http_url(args.video):
        video_path, metadata_path, _ = fetch_video(
            args.video,
            output / "source",
            max_height=args.max_height,
            cookies_from_browser=args.cookies_from_browser,
            ffmpeg_location=args.download_ffmpeg_location,
        )
        if video_path is None:
            raise RuntimeError("URL acquisition completed without a media file.")
        video = str(video_path)
        print(f"Acquired video: {video_path}")
        print(f"Source metadata: {metadata_path}")
    else:
        video = str(Path(args.video).expanduser().resolve())
        if not Path(video).is_file():
            raise FileNotFoundError(f"Local video does not exist: {video}")
    manifest = output / "manifest.json"
    shots = output / "shots.json"
    frames = output / "frames"
    audio = output / "audio"
    evidence = output / "evidence"
    call(here / "probe_video.py", video, "--output", str(manifest))
    call(here / "detect_shots.py", video, "--manifest", str(manifest), "--output", str(shots), "--threshold", args.scene_threshold)
    sample_args = [video, "--manifest", str(manifest), "--shots", str(shots), "--output-dir", str(frames),
                   "--base-fps", args.base_fps, "--cut-fps", args.cut_fps]
    for focus in args.focus:
        sample_args += ["--focus", focus]
    call(here / "sample_frames.py", *sample_args)
    call(here / "make_contact_sheets.py", str(frames / "frames.csv"), "--output-dir", str(output / "contact_sheets"))
    call(here / "analyze_audio.py", video, "--output-dir", str(audio))
    call(here / "build_timeline.py", "--manifest", str(manifest), "--shots", str(shots),
         "--audio-profile", str(audio / "audio_profile.csv"), "--output-dir", str(evidence))
    print(f"Analysis workspace ready: {output}")


if __name__ == "__main__":
    main()
