# Video Downloader Web App

This is a simple web application for downloading videos or audio from YouTube, Instgram, Facebook, Tiktok... . It supports multiple formats, provides download progress tracking, and allows multiple users to start downloads concurrently. The backend is written in Python using Flask and `yt_dlp`. The frontend is a basic HTML page with a progress bar and format selection.

## Features

- Download videos or audio in formats such as MP4, WEBM, or MP3
- Real-time download progress updates
- Supports multiple users by running each download in a separate thread
- Modular code structure
- Dockerized for easy deployment

## How to Run

You can run the app using Docker or locally.

---

### Option 1: Run with Docker

Make sure Docker is installed on your system.

```bash
docker build -t video-downloader .
docker run -p 5000:5000 video-downloader

```
### Option 2: Run Locally (without Docker)
You need Python 3 installed and the dependencies found in ``requirments.txt`` and *FFmpeg*

```bash
pip install requirments.txt

```
#### Install FFmpeg:
- On Ubuntu/Debian:

```bash
Copy code
sudo apt install ffmpeg
- On MacOS (with Homebrew):
```
```bash
Copy code
brew install ffmpeg
```
- On Windows:
Download FFmpeg from ffmpeg.org, and add it to your system PATH.

Run the app:
```bash
Copy code
python app.py
The app will start a local server, accessible at http://localhost:5000
```
### Usage
- Open the app in your browser.

- Paste a video URL (e.g., from YouTube).

- Select a format.

- Click "Download".

- Monitor progress via the progress bar.

- Once complete, the file will be available for download.

### Notes
- Each download runs in a separate thread, allowing multiple users to start downloads at the same time.

- Downloads are saved to a downloads/ directory in the current working directory.