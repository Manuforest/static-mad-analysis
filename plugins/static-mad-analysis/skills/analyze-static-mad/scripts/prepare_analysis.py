from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def call(script: Path, *args: str) -> None:
    subprocess.run([sys.executable, str(script), *args], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare deterministic artifacts for a static-MAD analysis.")
    parser.add_argument("video")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--scene-threshold", default="0.22")
    parser.add_argument("--base-fps", default="1")
    parser.add_argument("--cut-fps", default="4", help="Automatic sampling rate around candidate cuts")
    parser.add_argument("--focus", action="append", default=[], help="Optional START:END:FPS interval")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest = output / "manifest.json"
    shots = output / "shots.json"
    frames = output / "frames"
    audio = output / "audio"
    evidence = output / "evidence"
    call(here / "probe_video.py", args.video, "--output", str(manifest))
    call(here / "detect_shots.py", args.video, "--manifest", str(manifest), "--output", str(shots), "--threshold", args.scene_threshold)
    sample_args = [args.video, "--manifest", str(manifest), "--shots", str(shots), "--output-dir", str(frames),
                   "--base-fps", args.base_fps, "--cut-fps", args.cut_fps]
    for focus in args.focus:
        sample_args += ["--focus", focus]
    call(here / "sample_frames.py", *sample_args)
    call(here / "make_contact_sheets.py", str(frames / "frames.csv"), "--output-dir", str(output / "contact_sheets"))
    call(here / "analyze_audio.py", args.video, "--output-dir", str(audio))
    call(here / "build_timeline.py", "--manifest", str(manifest), "--shots", str(shots),
         "--audio-profile", str(audio / "audio_profile.csv"), "--output-dir", str(evidence))
    print(f"Analysis workspace ready: {output}")


if __name__ == "__main__":
    main()
