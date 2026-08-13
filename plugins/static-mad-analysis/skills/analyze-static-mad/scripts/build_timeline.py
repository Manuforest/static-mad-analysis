from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from common import read_json, write_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Create evidence-first analysis templates.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--shots", required=True)
    parser.add_argument("--audio-profile")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    manifest = read_json(Path(args.manifest))
    shot_data = read_json(Path(args.shots))
    audio = []
    if args.audio_profile:
        with Path(args.audio_profile).open(encoding="utf-8-sig") as handle:
            audio = list(csv.DictReader(handle))
    timeline = {
        "source": manifest["source"],
        "duration_seconds": manifest["duration_seconds"],
        "analysis_state": "blind_read",
        "shots": shot_data["shots"],
        "audio_windows": audio,
        "music_sections": [],
        "chapters": [],
        "shot_clusters": [],
        "shot_reading": {
            "state": "candidate_boundaries_unreviewed",
            "covered_intervals": [],
            "unresolved_intervals": [],
        },
        "unresolved_questions": [],
    }
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "timeline.json", timeline)
    write_json(output / "entities.json", {"entities": [], "identity_conflicts": []})
    write_json(output / "relations.json", {"relations": []})
    write_json(output / "hypotheses.json", {"hypotheses": [], "external_context_used": False})
    (output / "observations.jsonl").write_text("", encoding="utf-8")
    shot_rows = []
    for shot in shot_data["shots"]:
        shot_rows.append({
            "shot_id": shot["shot_id"],
            "times": [shot["start"], shot["end"]],
            "chapter_id": None,
            "cluster_id": None,
            "unit_type": "shot",
            "boundary_status": "candidate_unreviewed",
            "visible_content": None,
            "momentary_subject": None,
            "music": {"section": None, "event": None, "lyric_or_speech": None},
            "edit_operations": [],
            "relation_to_previous": [],
        })
    shot_reading = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in shot_rows)
    (output / "shot_reading.jsonl").write_text(shot_reading, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
