# Media Downloader Bot

Telegram bot to download videos/audio from Instagram & YouTube, extract audio, and identify songs.

## Quickstart

1. Copy env
   cp .env.example .env
   # set BOT_TOKEN and CHANNEL_USERNAME

2. Install deps
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt

3. Ensure ffmpeg is installed

4. Run bot
   python -m src.main

