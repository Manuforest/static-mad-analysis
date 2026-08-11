from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path


def resolve_binary(name: str, explicit: str | None = None) -> str:
    candidates = [explicit, os.environ.get(f"STATIC_MAD_{name.upper()}"), shutil.which(name)]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(Path(candidate).resolve())
    raise FileNotFoundError(
        f"Cannot find {name}. Pass --{name}, set STATIC_MAD_{name.upper()}, or add it to PATH."
    )


def run(args: list[str], *, capture: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=capture,
    )


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))
