
"""
Automated tests for the Student Task Management System.

Tests task creation, validation, filtering, completion, and deletion.
"""

import sqlite3

import pytest

import database
from app import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    """Create a Flask test client with a temporary test database."""

    test_database = tmp_path / "test_tasks.db"

    # Use a separate database so real project data is not changed.
    monkeypatch.setattr(database, "DATABASE", test_database)

    database.init_db()

    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def get_task_count():
    """Return the number of tasks in the test database."""

    with database.get_connection() as connection:
        return connection.execute(
            "SELECT COUNT(*) FROM tasks"
        ).fetchone()[0]


def add_sample_task(client, title="Test Task"):
    """Add a sample task for testing."""

    return client.post("/add", data={
        "title": title,
        "description": "Testing description",
        "due_date": "2026-11-10",
        "priority": "Medium",
    })


def test_dashboard_loads(client):
    """Check that the dashboard opens successfully."""

    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Task Management System" in response.data


def test_add_task_success(client):
    """Check that a valid task is added."""

    response = add_sample_task(client)

    assert response.status_code == 302
    assert get_task_count() == 1


def test_empty_task_title_rejected(client):
    """Check that an empty task title is rejected."""

    client.post("/add", data={"title": "   "})

    assert get_task_count() == 0


def test_invalid_priority_rejected(client):
    """Check that an unsupported priority is rejected."""

    client.post("/add", data={
        "title": "Invalid Priority Task",
        "priority": "Urgent",
    })

    assert get_task_count() == 0


def test_invalid_due_date_rejected(client):
    """Check that an invalid due date is rejected."""

    client.post("/add", data={
        "title": "Invalid Date Task",
        "priority": "Medium",
        "due_date": "invalid-date",
    })

    assert get_task_count() == 0


def test_task_completion(client):
    """Check that a pending task can be marked completed."""

    add_sample_task(client)

    with database.get_connection() as connection:
        task_id = connection.execute(
            "SELECT id FROM tasks"
        ).fetchone()["id"]

    client.post(f"/toggle/{task_id}")

    with database.get_connection() as connection:
        task = connection.execute(
            "SELECT completed FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

    assert task["completed"] == 1


def test_task_deletion(client):
    """Check that a task can be deleted."""

    add_sample_task(client)

    with database.get_connection() as connection:
        task_id = connection.execute(
            "SELECT id FROM tasks"
        ).fetchone()["id"]

    client.post(f"/delete/{task_id}")

    assert get_task_count() == 0


def test_task_filters(client):
    """Check that pending and completed filters work."""

    add_sample_task(client, "Filter Test Task")

    with database.get_connection() as connection:
        task_id = connection.execute(
            "SELECT id FROM tasks"
        ).fetchone()["id"]

    client.post(f"/toggle/{task_id}")

    completed_response = client.get("/?status=completed")
    pending_response = client.get("/?status=pending")

    assert b"Filter Test Task" in completed_response.data
    assert b"Filter Test Task" not in pending_response.data
