from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    parser = argparse.ArgumentParser(description="Build timestamped contact sheets from frames.csv.")
    parser.add_argument("frames_csv")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--group-seconds", type=float, default=10.0)
    parser.add_argument("--columns", type=int, default=5)
    parser.add_argument("--thumb-width", type=int, default=320)
    args = parser.parse_args()

    with Path(args.frames_csv).open(encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    # Prefer one global overview sequence. Focus sheets are inspected separately when needed.
    overview = [row for row in rows if row["source"] == "overview"] or rows
    groups: dict[int, list[dict]] = {}
    for row in overview:
        groups.setdefault(int(float(row["time"]) // args.group_seconds), []).append(row)

    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default()
    for group_id, items in sorted(groups.items()):
        images = []
        for row in items:
            image = Image.open(row["file"]).convert("RGB")
            height = round(image.height * args.thumb_width / image.width)
            image = image.resize((args.thumb_width, height), Image.Resampling.LANCZOS)
            images.append((image, f'{float(row["time"]):07.2f}s'))
        if not images:
            continue
        cell_h = max(image.height for image, _ in images) + 22
        sheet = Image.new("RGB", (args.columns * args.thumb_width, math.ceil(len(images) / args.columns) * cell_h), "black")
        draw = ImageDraw.Draw(sheet)
        for i, (image, label) in enumerate(images):
            x = (i % args.columns) * args.thumb_width
            y = (i // args.columns) * cell_h
            sheet.paste(image, (x, y))
            draw.text((x + 5, y + image.height + 3), label, fill="white", font=font)
        start = group_id * args.group_seconds
        sheet.save(output / f"sheet_{start:06.1f}.jpg", quality=92)
    print(f"{len(groups)} contact sheets -> {output}")


if __name__ == "__main__":
    main()
