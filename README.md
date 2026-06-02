# 🎥 YouTube Downloader Pro

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Linux%20%7C%20Windows-lightgrey)

**YouTube Downloader Pro** is a professional, smart, and lightweight Command-Line Interface (CLI) tool written in Python. It allows users to download YouTube videos in high quality (up to 1080p Full HD) or extract audio seamlessly with an advanced progress bar and a beautiful text-based user interface.

---

## ✨ Features

* **⚡ Dynamic Dependency Check:** Automatically detects and installs missing Python libraries (`yt-dlp`, `rich`) on the first run.
* **🔍 Smart Environment Verification:** Checks for system-level tools like `FFmpeg` and guides the user with clear instructions if missing.
* **🎬 High-Quality Video Downloads:** Supports downloading specific formats and resolutions including Full HD (1080p), HD (720p), and Eco qualities.
* **🎵 Advanced Audio Extraction:** Allows downloading audio-only tracks with custom bitrates (320kbps, 192kbps, 128kbps) converted automatically to MP3.
* **📊 Rich Terminal UI:** Powered by `rich` library featuring a customized ASCII logo, colored tables, and an interactive real-time download progress bar (showing speed, percentage, and ETA).
* **🤖 Android-Optimized:** Pre-configured to automatically detect Android environments (Termux) and save files directly to the device's shared `Download` folder.

---

## 🛠️ System Requirements

For downloading high-quality videos (1080p+) or merging/extracting audio, **FFmpeg** is required by the core engine (`yt-dlp`).

### Quick Installation Guide:

* **Android (Termux):**
    ```bash
    pkg update && pkg install ffmpeg nodejs -y
    ```
* **Linux (Ubuntu/Debian):**
    ```bash
    sudo apt update && sudo apt install ffmpeg nodejs -y
    ```
* **macOS (via Homebrew):**
    ```bash
    brew install ffmpeg node
    ```
* **Windows:**
    Download FFmpeg from the official site and add its `bin` folder to your system's Environment Variables (PATH).

---

## 🚀 How to Run

1. **Clone the repository** (or download the script):
   ```bash
   git clone [https://github.com/sadikmahedi88/YouTube-Downlonder.git]([https://github.com/sadikmahedi88/YouTube-Downlonder.git)
   cd YouTube-Downlonder 


2. Run the script:

python Download.py


(Note: The script will automatically handle the installation of required python packages like rich and yt-dlp upon launch!)


📖 Usage Preview

Upon launching, the tool presents an interactive guide:

Paste the YouTube URL.

Select Media Type: Video or Audio Only.

Choose preferred Quality (e.g., Full HD 1080p or 320kbps Studio Audio).

Select the container output format (MP4 / MKV).

Watch the beautiful real-time progress bar handle the download and merge safely!

⚖️ Legal Disclaimer

This project is intended solely for educational purposes and personal use. Please respect local copyright laws and YouTube's Terms of Service. The developer does not condone or assume liability for any misuse or unauthorized distribution of copyrighted material.

👑 Credits & Support

Developer: Murphy >_

GitHub: https://github.com/sadikmahedi88

Telegram: https://t.me/Murphython

Feel free to ⭐ star this repository if you found it helpful!

