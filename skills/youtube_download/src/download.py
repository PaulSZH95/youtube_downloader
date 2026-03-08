"""YouTube video and subtitle downloader CLI."""

import argparse
import subprocess
import sys
from pathlib import Path


def download_video(
    url: str,
    output_dir: Path,
    output_name: str = "test",
    video: bool = False,
) -> int:
    """
    Download YouTube video and/or subtitles.

    Args:
        url: YouTube video URL
        output_dir: Directory to save downloads
        output_name: Output filename (without extension)
        video: If True, download video (mp4). If False, subtitles only.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{output_dir.absolute()}:/app/downloads",
        "yt-dl",
        "yt-dlp",
        "--remote-components",
        "ejs:npm",
    ]

    if video:
        cmd.extend(["-f", "best[ext=mp4]"])
    else:
        cmd.append("--skip-download")

    cmd.extend(
        [
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang",
            "en",
            "--sub-format",
            "ttml",
            "--convert-subs",
            "srt",
            "--output",
            f"/app/downloads/{output_name}.%(ext)s",
            url,
        ]
    )

    print(f"Downloading {'video' if video else 'subtitles'} from: {url}")
    print(f"Output directory: {output_dir.absolute()}\n")

    try:
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error: Download failed with exit code {e.returncode}", file=sys.stderr)
        if e.stderr:
            print(e.stderr.decode(), file=sys.stderr)
        return e.returncode
    except FileNotFoundError:
        print(
            "Error: Docker not found. Please install Docker Desktop.", file=sys.stderr
        )
        return 1


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="unveil download",
        description="Download YouTube videos and subtitles",
    )
    parser.add_argument(
        "-u",
        "--url",
        help="YouTube video URL",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="test",
        help="Output filename (default: test)",
    )
    parser.add_argument(
        "-d",
        "--output-dir",
        type=Path,
        default=Path.cwd() / "downloads",
        help="Output directory (default: ./downloads)",
    )
    parser.add_argument(
        "-v",
        "--video",
        action="store_true",
        help="Download video (mp4) instead of subtitles only",
    )

    args = parser.parse_args(argv)

    return download_video(
        url=args.url,
        output_dir=args.output_dir,
        output_name=args.output,
        video=args.video,
    )


if __name__ == "__main__":
    sys.exit(main())
