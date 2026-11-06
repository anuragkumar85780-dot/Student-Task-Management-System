
"""
Database module for the Student Task Management System.

Handles SQLite database connections and table initialization.
"""

import sqlite3
from config import DATABASE


def get_connection():
    """Create and return a SQLite database connection."""
    connection = sqlite3.connect(DATABASE)

    # Return database rows in a dictionary-like format.
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the tasks table if it does not already exist."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL CHECK(length(trim(title)) > 0),
                description TEXT,
                due_date TEXT,
                priority TEXT NOT NULL DEFAULT 'Medium'
                    CHECK(priority IN ('Low', 'Medium', 'High')),
                completed INTEGER NOT NULL DEFAULT 0
                    CHECK(completed IN (0, 1)),
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Save the database table initialization.
        connection.commit()
