from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                priority TEXT NOT NULL DEFAULT 'Medium',
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.route("/")
def index():
    status = request.args.get("status", "all")
    with get_connection() as connection:
        if status == "pending":
            tasks = connection.execute(
                "SELECT * FROM tasks WHERE completed = 0 ORDER BY id DESC"
            ).fetchall()
        elif status == "completed":
            tasks = connection.execute(
                "SELECT * FROM tasks WHERE completed = 1 ORDER BY id DESC"
            ).fetchall()
        else:
            status = "all"
            tasks = connection.execute(
                "SELECT * FROM tasks ORDER BY id DESC"
            ).fetchall()

        total = connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        completed = connection.execute(
            "SELECT COUNT(*) FROM tasks WHERE completed = 1"
        ).fetchone()[0]
    return render_template(
        "index.html", tasks=tasks, status=status, total=total, completed=completed
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    due_date = request.form.get("due_date", "").strip()
    priority = request.form.get("priority", "Medium")
    if priority not in {"Low", "Medium", "High"}:
        priority = "Medium"

    if not title:
        flash("Please enter a task title.", "error")
        return redirect(url_for("index"))

    with get_connection() as connection:
        connection.execute(
            "INSERT INTO tasks (title, description, due_date, priority) VALUES (?, ?, ?, ?)",
            (title, description, due_date or None, priority),
        )
    flash("Task added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    with get_connection() as connection:
        task = connection.execute(
            "SELECT completed FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
        if task is not None:
            new_status = 0 if task["completed"] else 1
            connection.execute(
                "UPDATE tasks SET completed = ? WHERE id = ?", (new_status, task_id)
            )
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    with get_connection() as connection:
        connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    flash("Task deleted.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
