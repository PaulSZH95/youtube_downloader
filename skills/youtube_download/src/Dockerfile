FROM python:3.13-slim

# Install dependencies + tools in a single RUN layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    xz-utils \
    ca-certificates \
    unzip \
    gnupg \
    # Install Node.js LTS vi NodeSource
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && npm install -g deno \
    && curl -L https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz -o /tmp/ffmpeg.tar.xz \
    && tar -xf /tmp/ffmpeg.tar.xz -C /tmp \
    && cp /tmp/ffmpeg-master-latest-linux64-gpl/bin/* /usr/local/bin/ \
    && python3 -m pip install --no-cache-dir --upgrade pip \
    && python3 -m pip install --no-cache-dir "yt-dlp[yt-dlp-ejs]" \
    && python3 -m pip install "yt-dlp[default,curl-cffi]" \
    && rm -rf /tmp/ffmpeg.tar.xz /tmp/ffmpeg-master-latest-linux64-gpl \
    && apt-get purge -y --auto-remove curl xz-utils unzip gnupg \
    && rm -rf /var/lib/apt/lists/*c

WORKDIR /app
CMD ["sleep", "inf"]