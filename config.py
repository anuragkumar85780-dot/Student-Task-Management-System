
"""
Configuration settings for the Student Task Management System.

Stores application settings such as database location,
secret key, and debug mode.
"""

import os
from pathlib import Path

# Get the directory where this project is located.
BASE_DIR = Path(__file__).resolve().parent

# Store the SQLite database in the project directory.
DATABASE = BASE_DIR / "tasks.db"

# Read the secret key from the environment when available.
SECRET_KEY = os.environ.get(
    "FLASK_SECRET_KEY",
    "local-development-key-change-before-deployment"
)

# Enable debug mode during local development.
DEBUG = True
