"""
AI BET BOT v3
Global configuration
"""

from pathlib import Path
import os

# ==========================
# PROJECT
# ==========================

PROJECT_NAME = "AI BET BOT v3"
VERSION = "3.0.0"

ROOT_DIR = Path(__file__).resolve().parent

DATA_DIR = ROOT_DIR / "data"
MODEL_DIR = ROOT_DIR / "models"
LOG_DIR = ROOT_DIR / "logs"

DATA_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# ==========================
# API FOOTBALL
# ==========================

API_KEY = os.getenv("API_FOOTBALL_KEY", "")

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3

RETRY_DELAY = 2

# ==========================
# MATCHES
# ==========================

LOAD_TODAY = True
LOAD_TOMORROW = True

TIMEZONE = "Europe/Kyiv"

# ==========================
# AI
# ==========================

MODEL_FILE = MODEL_DIR / "football_ai.pkl"

MIN_CONFIDENCE = 70

# ==========================
# CACHE
# ==========================

CACHE_ENABLED = True

CACHE_EXPIRE_MINUTES = 30

# ==========================
# LOGGING
# ==========================

LOG_FILE = LOG_DIR / "ai_bet_bot.log"

LOG_LEVEL = "INFO"

# ==========================
# REPORTS
# ==========================

REPORT_FOLDER = ROOT_DIR / "reports"

REPORT_FOLDER.mkdir(exist_ok=True)

# ==========================
# DEBUG
# ==========================

DEBUG = False
