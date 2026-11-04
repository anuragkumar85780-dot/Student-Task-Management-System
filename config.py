import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASE = BASE_DIR / "tasks.db"

SECRET_KEY = os.environ.get(
    "FLASK_SECRET_KEY",
    "local-development-key-change-before-deployment"
)

DEBUG = True