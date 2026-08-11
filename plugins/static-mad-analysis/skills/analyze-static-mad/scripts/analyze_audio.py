from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
from pathlib import Path

import numpy as np

from common import resolve_binary, write_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a lightweight audio energy and spectral profile.")
    parser.add_argument("video")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--window", type=float, default=0.5)
    parser.add_argument("--sample-rate", type=int, default=16000)
    parser.add_argument("--ffmpeg")
    args = parser.parse_args()

    ffmpeg = resolve_binary("ffmpeg", args.ffmpeg)
    cmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-i", str(Path(args.video).resolve()),
           "-vn", "-ac", "1", "-ar", str(args.sample_rate), "-f", "f32le", "-"]
    proc = subprocess.run(cmd, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode and not proc.stdout:
        error_text = proc.stderr.decode("utf-8", errors="replace")
        no_audio_markers = (
            "does not contain any stream",
            "matches no streams",
            "Output file does not contain any stream",
        )
        if not any(marker in error_text for marker in no_audio_markers):
            raise subprocess.CalledProcessError(proc.returncode, cmd, proc.stdout, proc.stderr)

        output = Path(args.output_dir).resolve()
        output.mkdir(parents=True, exist_ok=True)
        fields = ["start", "end", "rms", "dbfs", "spectral_centroid_hz", "energy_band"]
        with (output / "audio_profile.csv").open("w", newline="", encoding="utf-8-sig") as handle:
            csv.DictWriter(handle, fieldnames=fields).writeheader()
        write_json(output / "audio_summary.json", {
            "present": False,
            "window_seconds": args.window,
            "sample_rate": args.sample_rate,
            "integrated_rms_dbfs": None,
            "quiet_threshold_dbfs": None,
            "high_threshold_dbfs": None,
        })
        print(f"No audio stream -> {output}")
        return
    samples = np.frombuffer(proc.stdout, dtype=np.float32)
    size = max(1, round(args.window * args.sample_rate))
    rows = []
    for i in range(0, len(samples), size):
        chunk = samples[i:i + size]
        if len(chunk) < size // 2:
            continue
        rms = float(np.sqrt(np.mean(chunk * chunk) + 1e-12))
        dbfs = 20 * math.log10(max(rms, 1e-9))
        spectrum = np.abs(np.fft.rfft(chunk * np.hanning(len(chunk))))
        freqs = np.fft.rfftfreq(len(chunk), 1 / args.sample_rate)
        centroid = float((spectrum * freqs).sum() / max(spectrum.sum(), 1e-9))
        rows.append({"start": round(i / args.sample_rate, 3), "end": round((i + len(chunk)) / args.sample_rate, 3),
                     "rms": rms, "dbfs": round(dbfs, 3), "spectral_centroid_hz": round(centroid, 1)})

    db = np.array([row["dbfs"] for row in rows]) if rows else np.array([])
    if len(db):
        low, high = np.percentile(db, [30, 75])
        for row in rows:
            row["energy_band"] = "low" if row["dbfs"] <= low else "high" if row["dbfs"] >= high else "mid"
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    with (output / "audio_profile.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        fields = ["start", "end", "rms", "dbfs", "spectral_centroid_hz", "energy_band"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    summary = {
        "present": True,
        "window_seconds": args.window,
        "sample_rate": args.sample_rate,
        "integrated_rms_dbfs": round(20 * math.log10(max(float(np.sqrt(np.mean(samples*samples) + 1e-12)), 1e-9)), 3) if len(samples) else None,
        "quiet_threshold_dbfs": round(float(np.percentile(db, 30)), 3) if len(db) else None,
        "high_threshold_dbfs": round(float(np.percentile(db, 75)), 3) if len(db) else None,
    }
    write_json(output / "audio_summary.json", summary)
    print(output)


if __name__ == "__main__":
    main()
