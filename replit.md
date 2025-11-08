# SAINI DRM Bot - Telegram Text Downloader Bot

## Overview
This is a Telegram bot that can extract videos and PDFs from text files and upload them to Telegram. It includes DRM support with a minimum quality of 360p and features a Flask web interface.

## Project Structure
- **Flask Web App (Frontend)**: Runs on port 5000, displays bot information
- **Telegram Bot (Backend)**: Processes text files, downloads videos/PDFs, handles user interactions
- **modules/**: Contains all bot logic and handlers
  - `main.py`: Main bot entry point
  - `text_handler.py`: Handles text file processing
  - `html_handler.py`: HTML conversion features
  - `drm_handler.py`: DRM video handling
  - `youtube_handler.py`: YouTube download functionality
  - `commands.py`, `features.py`, `settings.py`, etc.

## Setup Instructions

### 1. Environment Variables
You need to set up the following environment variables in the Replit Secrets:

**Required:**
- **API_ID**: Get from https://my.telegram.org/apps
- **API_HASH**: Get from https://my.telegram.org/apps
- **BOT_TOKEN**: Get from @BotFather on Telegram
- **OWNER**: Your Telegram user ID (numeric)

**Optional:**
- **CREDIT**: Your name/credit to display (default: SAINI BOTS)
- **AUTH_USERS**: Comma-separated list of authorized user IDs
- **TOTAL_USERS**: Comma-separated list of all users

**For Classplus/DRM Support:**
- **Note**: The Classplus token (`cptoken`) in `modules/globals.py` expires periodically and needs to be updated manually when it expires. If you see errors about "Invalid response - token may be expired", you'll need to get a fresh Classplus token.

### 2. Getting Your Credentials

#### Telegram API Credentials:
1. Go to https://my.telegram.org/apps
2. Log in with your phone number
3. Create a new application
4. Copy the **API_ID** and **API_HASH**

#### Bot Token:
1. Open Telegram and search for @BotFather
2. Send `/newbot` and follow the instructions
3. Copy the bot token provided

#### Your User ID:
1. Search for @userinfobot on Telegram
2. Send `/start` to get your user ID

### 3. Current Status
- ✅ Python 3.12 installed
- ✅ System dependencies installed (ffmpeg-full)
- ✅ All Python dependencies installed from requirements.txt
- ✅ Flask app configured for port 5000
- ✅ Workflow created to run both Flask and bot
- ✅ Required secrets configured (API_ID, API_HASH, BOT_TOKEN, OWNER)
- ✅ .gitignore updated for Python project
- ✅ VM deployment configured
- ✅ **Bot is running successfully**

### 4. Using the Bot
Your Telegram bot is now live! Here's how to use it:
1. Open Telegram and search for your bot
2. Send `/start` to begin
3. All features (including premium features) are enabled for your user ID
4. Upload text files with video/PDF links to download them
5. Use the various commands listed above for different features

## Features
- Text file processing and video extraction
- PDF download support
- DRM-protected video download (min 360p)
- YouTube video/audio download
- Text to HTML conversion
- User authorization system
- Broadcast messaging
- Settings management

## Bot Commands
- `/start` - Start the bot
- `/stop` - Stop ongoing process
- `/id` - Get your Telegram ID
- `/info` - Check your information
- `/cookies` - Upload YouTube cookies
- `/y2t` - YouTube to .txt converter
- `/ytm` - YouTube to .mp3 downloader
- `/t2t` - Text to .txt generator
- `/t2h` - .txt to .html converter
- `/logs` - View bot activity (owner only)

## Technical Details
- **Language**: Python 3.12
- **Frameworks**: Pyrogram (Telegram), Flask (Web)
- **Dependencies**: See requirements.txt
- **System Tools**: FFmpeg (for video processing)
- **Deployment Options**:
  - **Replit**: VM deployment (always running) - Current setup
  - **Railway**: Dockerfile-based deployment - High speed (35-50 MB/s)
  - **Koyeb**: Dockerfile-based deployment - Unlimited free tier (30-45 MB/s)
  - **Render**: Docker deployment - Basic free tier (12-25 MB/s)
  - **Heroku**: Buildpack deployment - Traditional hosting (15-30 MB/s)

## Architecture
The application runs both:
1. Flask web server on 0.0.0.0:5000 (public-facing)
2. Telegram bot (background worker)

Both processes are managed by a single workflow using `start.sh`.

## Recent Changes
- 2025-10-27: Fresh GitHub import setup for Replit environment
  - **Security Fix**: Removed hardcoded sensitive defaults from modules/vars.py
    - API_ID, API_HASH, BOT_TOKEN, OWNER now strictly require environment variables
    - No fallback default values for security credentials
  - Installed Python 3.12 (already present in environment)
  - All Python dependencies from requirements.txt installed successfully
  - Created comprehensive .gitignore for Python project (excludes session files, logs, sensitive data)
  - Configured workflow "Bot" to run both Flask app (port 5000) and Telegram bot via start.sh
  - Set up required environment secrets (API_ID, API_HASH, BOT_TOKEN, OWNER) via Replit Secrets
  - Configured VM deployment for production use (maintains persistent Telegram connection)
  - Removed old bot.session file to fix AUTH_KEY_DUPLICATED error
  - Both Flask web server and Telegram bot running successfully
  - Verified web interface is accessible and displaying correctly
  - **Updated PW (Physics Wallah) Download API**: Changed endpoint from `0e5a3f512dec` to `25261acd1521` subdomain in modules/drm_handler.py
  - **Improved /stop command functionality**: 
    - Enhanced feedback message to explain stop behavior clearly
    - Added cancel checks after each file download completes (before upload)
    - Stop command now responds faster - interrupts between files instead of waiting for entire batch
    - Properly cleans up downloaded files when stopping

- 2025-10-16: Added Railway and Koyeb deployment support
  - Created `railway.json` for Railway platform deployment configuration
  - Created `koyeb.yaml` for Koyeb platform deployment (unlimited free tier)
  - Added `.python-version` file for platform compatibility
  - Updated README.md with comprehensive deployment guides for Railway, Koyeb, Render, and Heroku
  - Fixed Koyeb port configuration (8000 for Gunicorn) to ensure health checks pass
  - Added performance optimization notes and expected download speeds per platform
  - All deployment configurations verified and architect-reviewed

## Previous Changes
- 2025-10-10: YouTube Download Filename Fix (saini.py, youtube_handler.py)
  - **Fixed YouTube MP3 download failures** caused by special characters in filenames
  - **Added filename sanitization**: Removes problematic characters (parentheses, brackets, invalid path chars)
  - **Fixed duration extraction**: Now handles filenames with spaces and special characters without crashing
  - **Improved error handling**: Returns default duration (60s) if ffprobe fails instead of crashing
  - Filenames like "002) Class-02 Tense.mp3" now download successfully

- 2025-10-10: URL Parsing and Download Fixes (drm_handler.py)
  - **Fixed title extraction for new link formats**: Now supports `[number. title] - full title (extra) : URL` format
  - **Fixed URL protocol handling**: URLs now correctly preserve `https://` protocol without duplication
  - **Fixed image download failures**: Properly extracts file extensions from URLs with query parameters (fixes PHOTO_EXT_INVALID error)
  - **Fixed audio download handling**: Same extension extraction fix applied to MP3/WAV/M4A files
  - **Improved URL parsing**: Uses regex to accurately extract URLs from various text formats
  - Supports multiple title/URL formats:
    - `title:URL` (original format)
    - `[number. title] - full title (extra) : URL` (new format)
    - Title on previous line, URL on next line (legacy format)

- 2025-10-10: Classplus API Error Handling Fix (drm_handler.py)
  - **Fixed 'url' error message bug** when processing Classplus files
  - Added proper error handling for Classplus API calls (tencdn, videos, media-cdn)
  - Now shows meaningful error messages instead of just 'url' when API fails
  - Detects expired Classplus tokens and provides clear instructions
  - Prevents crash when API response doesn't contain expected 'url' field

- 2025-10-10: Range Input Handling Improvements (drm_handler.py)
  - Fixed crash when users enter range inputs like "001-002" or "001-079"
  - **New Range Support**:
    - Single number (e.g., "5"): Downloads from index 5 to end of list (original behavior)
    - Range format (e.g., "5-10"): Downloads only items 5 through 10 (new feature)
  - Improved input validation with proper error messages
  - Added validation to reject invalid ranges (start > end)
  - Fixed success count calculation for both single-number and range downloads
  - Added proper handling for leading zeros in inputs (e.g., "001" → 1, "001-079" → 1-79)
  - Fixed vars.py to handle empty environment variables gracefully

- 2025-10-10: GitHub import setup in Replit environment
  - Installed Python 3.11 and ffmpeg-full
  - Fixed requirements.txt (removed invalid 'ffmpeg' package)
  - Installed all Python dependencies
  - Created .gitignore for Python project
  - Removed conflicting bot.session file
  - Created workflow for combined Flask + Bot execution via start.sh
  - Configured deployment settings for VM deployment
  - Both Flask server (port 5000) and Telegram bot running successfully
