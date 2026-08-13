from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from common import write_json


MEDIA_EXTENSIONS = {".avi", ".flv", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".ts", ".webm"}


def require_yt_dlp() -> Any:
    try:
        import yt_dlp
    except ImportError as exc:
        requirements = Path(__file__).resolve().parent.parent / "requirements.txt"
        command = f'"{sys.executable}" -m pip install -r "{requirements}"'
        raise RuntimeError(f"yt-dlp is not installed. Install the skill dependencies with: {command}") from exc
    return yt_dlp


def validate_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("The input must be an HTTP or HTTPS video URL.")
    return url


def format_selector(max_height: int | None) -> str:
    if max_height is None:
        return "bestvideo+bestaudio/best"
    return (
        f"bestvideo[height<={max_height}]+bestaudio/"
        f"best[height<={max_height}]/bestvideo+bestaudio/best"
    )


def selected_formats(info: dict[str, Any]) -> list[dict[str, Any]]:
    raw = info.get("requested_downloads") or info.get("requested_formats") or [info]
    keys = ("format_id", "format_note", "ext", "width", "height", "fps", "vcodec", "acodec", "filesize", "filesize_approx")
    return [{key: item.get(key) for key in keys if item.get(key) is not None} for item in raw]


def selected_video_format(formats: list[dict[str, Any]]) -> dict[str, Any]:
    return next((item for item in formats if item.get("vcodec") not in (None, "none")), {})


def public_metadata(info: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "id",
        "title",
        "fulltitle",
        "description",
        "extractor",
        "extractor_key",
        "webpage_url",
        "original_url",
        "uploader",
        "uploader_id",
        "channel",
        "channel_id",
        "duration",
        "timestamp",
        "upload_date",
        "release_date",
        "availability",
        "age_limit",
        "categories",
        "tags",
        "chapters",
        "subtitles",
        "automatic_captions",
    )
    return {key: info.get(key) for key in keys if info.get(key) is not None}


def resolve_media_path(ydl: Any, info: dict[str, Any]) -> Path:
    candidates: list[Path] = []
    for value in (info.get("filepath"), info.get("_filename")):
        if value:
            candidates.append(Path(value))

    requested = info.get("requested_downloads") or []
    for item in requested:
        value = item.get("filepath") or item.get("filename")
        if value:
            candidates.append(Path(value))

    prepared = Path(ydl.prepare_filename(info))
    candidates.append(prepared)
    for extension in MEDIA_EXTENSIONS:
        candidates.append(prepared.with_suffix(extension))

    for candidate in candidates:
        resolved = candidate.expanduser().resolve()
        if resolved.is_file() and resolved.suffix.lower() in MEDIA_EXTENSIONS:
            return resolved

    siblings = sorted(
        (
            path.resolve()
            for path in prepared.parent.glob(f"{prepared.stem}.*")
            if path.is_file() and path.suffix.lower() in MEDIA_EXTENSIONS
        ),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if siblings:
        return siblings[0]
    raise FileNotFoundError("yt-dlp completed, but the downloaded media file could not be resolved.")


def classify_download_error(message: str) -> str:
    lower = message.lower()
    if any(token in lower for token in ("ffmpeg is not installed", "ffmpeg not found")):
        return "missing_dependency"
    if any(token in lower for token in ("sign in", "login", "cookie", "authentication", "会员", "登录")):
        return "authentication_required"
    if any(token in lower for token in ("geo", "region", "country", "地区")):
        return "region_restricted"
    if "drm" in lower:
        return "drm_protected"
    if any(token in lower for token in ("unsupported url", "no suitable extractor")):
        return "unsupported_url"
    if any(token in lower for token in ("timed out", "network", "connection", "unable to download")):
        return "network_error"
    return "download_failed"


def fetch_video(
    url: str,
    output_dir: Path,
    *,
    max_height: int | None = 1080,
    cookies_from_browser: str | None = None,
    ffmpeg_location: str | None = None,
    metadata_only: bool = False,
) -> tuple[Path | None, Path, Path]:
    yt_dlp = require_yt_dlp()
    url = validate_url(url)
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    options: dict[str, Any] = {
        "format": format_selector(max_height),
        "outtmpl": str(output_dir / "%(extractor_key)s_%(id)s.%(ext)s"),
        "noplaylist": True,
        "overwrites": False,
        "continuedl": True,
        "windowsfilenames": True,
        "merge_output_format": "mp4",
        "socket_timeout": 30,
        "retries": 5,
        "fragment_retries": 5,
        "file_access_retries": 3,
    }
    if cookies_from_browser:
        options["cookiesfrombrowser"] = (cookies_from_browser,)
    configured_ffmpeg = ffmpeg_location or os.environ.get("STATIC_MAD_FFMPEG")
    if configured_ffmpeg:
        options["ffmpeg_location"] = configured_ffmpeg

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=not metadata_only)
            if info is None:
                raise RuntimeError("yt-dlp returned no video information.")
            if "entries" in info:
                entries = [entry for entry in info.get("entries") or [] if entry]
                if len(entries) != 1:
                    raise RuntimeError("The URL resolved to a playlist or multiple videos; provide one video URL.")
                info = entries[0]
            video_path = None if metadata_only else resolve_media_path(ydl, info)
    except yt_dlp.utils.DownloadError as exc:
        message = " ".join(str(exc).split())
        code = classify_download_error(message)
        raise RuntimeError(f"{code}: {message}") from exc

    metadata_path = output_dir / "metadata.json"
    manifest_path = output_dir / "download-manifest.json"
    formats = selected_formats(info)
    video_format = selected_video_format(formats)
    selected_height = video_format.get("height") or info.get("height")
    write_json(metadata_path, public_metadata(info))
    write_json(
        manifest_path,
        {
            "input_url": url,
            "resolved_url": info.get("webpage_url") or url,
            "extractor": info.get("extractor_key") or info.get("extractor"),
            "video_id": info.get("id"),
            "requested_max_height": max_height,
            "access_mode": "authorized_browser_session" if cookies_from_browser else "public",
            "selected_formats": formats,
            "selected_video": {
                "format_id": video_format.get("format_id") or info.get("format_id"),
                "width": video_format.get("width") or info.get("width"),
                "height": selected_height,
                "fps": video_format.get("fps") or info.get("fps"),
                "codec": video_format.get("vcodec") or info.get("vcodec"),
            },
            "fine_detail_review_limited": bool(selected_height and selected_height < 720),
            "metadata_only": metadata_only,
            "video_path": str(video_path) if video_path else None,
            "metadata_path": str(metadata_path),
            "acquired_at": datetime.now(timezone.utc).isoformat(),
        },
    )
    return video_path, metadata_path, manifest_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Acquire an authorized public video URL for local MAD analysis.")
    parser.add_argument("url")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-height", type=int, default=1080, help="Maximum preferred video height; default: 1080")
    parser.add_argument("--cookies-from-browser", help="Read a local browser session only with explicit user authorization")
    parser.add_argument("--ffmpeg-location", help="Optional FFmpeg executable or directory for yt-dlp")
    parser.add_argument("--metadata-only", action="store_true", help="Resolve metadata without downloading media")
    args = parser.parse_args()

    try:
        video_path, metadata_path, manifest_path = fetch_video(
            args.url,
            Path(args.output_dir),
            max_height=args.max_height,
            cookies_from_browser=args.cookies_from_browser,
            ffmpeg_location=args.ffmpeg_location,
            metadata_only=args.metadata_only,
        )
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"FETCH_ERROR={exc}", file=sys.stderr)
        raise SystemExit(2) from exc

    if video_path:
        print(f"VIDEO_PATH={video_path}")
    print(f"METADATA_PATH={metadata_path}")
    print(f"DOWNLOAD_MANIFEST_PATH={manifest_path}")


if __name__ == "__main__":
    main()
