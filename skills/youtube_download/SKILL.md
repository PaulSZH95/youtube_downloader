---
name: youtube_downloads
description: download subtitles or video from youtube
---

# youtube_downloads skills

synchronous io bound download of youtube videos from youtube url

```bash
[-h] [-u URL] [-o OUTPUT] [-d OUTPUT_DIR] [-v]
usage: download [-h] [-u URL] [-o OUTPUT] [-d OUTPUT_DIR] [-v]

Download YouTube videos and subtitles

options:
  -h, --help            show this help message and exit
  -u, --url URL         YouTube video URL
  -o, --output OUTPUT   Output filename (default: test)
  -d, --output-dir OUTPUT_DIR
                        Output directory (default: ./downloads)
  -v, --video           Download video (mp4) instead of subtitles only
```

# Download youtube video with subtitles

## Examples

```powershell
  python ./src/download.py --url "https://www.youtube.com/watch?v=AHnqvZBwk0Y" `
  -o stronk -d ./downloads -v
```

```bash
  python ./src/download.py --url "https://www.youtube.com/watch?v=AHnqvZBwk0Y" \
  -o stronk -d ./downloads -v
```

# Download youtube subtitles without video

## Examples

```powershell
  python download.py --url "https://www.youtube.com/watch?v=3xjPXqawCwQ" `
  -o stronk -d ./downloads
```

```bash
  python download.py --url "https://www.youtube.com/watch?v=3xjPXqawCwQ" \
  -o stronk -d ./downloads
```

Limitations:

- only able to download 1 url at a time

Error Handling:

- if docker image not found build it with [dockerfile](./youtube_download/src/Dockerfile)
  ```
      docker build -t yt-dl:latest .
  ```
