from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash

from database import get_connection

main = Blueprint("main", __name__)

ALLOWED_PRIORITIES = {"Low", "Medium", "High"}
ALLOWED_STATUSES = {"all", "pending", "completed"}


@main.route("/")
def index():
    status = request.args.get("status", "all").lower()

    if status not in ALLOWED_STATUSES:
        status = "all"

    with get_connection() as connection:
        if status == "pending":
            tasks = connection.execute(
                "SELECT * FROM tasks WHERE completed = 0 ORDER BY "
                "CASE WHEN due_date IS NULL OR due_date = '' THEN 1 ELSE 0 END, due_date, id DESC"
            ).fetchall()

        elif status == "completed":
            tasks = connection.execute(
                "SELECT * FROM tasks WHERE completed = 1 ORDER BY id DESC"
            ).fetchall()

        else:
            tasks = connection.execute(
                "SELECT * FROM tasks ORDER BY completed ASC, "
                "CASE WHEN due_date IS NULL OR due_date = '' THEN 1 ELSE 0 END, due_date, id DESC"
            ).fetchall()

        total = connection.execute(
            "SELECT COUNT(*) FROM tasks"
        ).fetchone()[0]

        completed = connection.execute(
            "SELECT COUNT(*) FROM tasks WHERE completed = 1"
        ).fetchone()[0]

        pending = total - completed

    return render_template(
        "index.html",
        tasks=tasks,
        status=status,
        total=total,
        completed=completed,
        pending=pending,
        today=date.today().isoformat(),
    )


@main.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    due_date = request.form.get("due_date", "").strip()
    priority = request.form.get("priority", "Medium").strip()

    if not title:
        flash("Please enter a task title.", "error")
        return redirect(url_for("main.index"))

    if len(title) > 120:
        flash("Task title must be 120 characters or fewer.", "error")
        return redirect(url_for("main.index"))

    if priority not in ALLOWED_PRIORITIES:
        flash("Please select a valid priority.", "error")
        return redirect(url_for("main.index"))

    if due_date:
        try:
            date.fromisoformat(due_date)
        except ValueError:
            flash("Please enter a valid due date.", "error")
            return redirect(url_for("main.index"))

    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO tasks (title, description, due_date, priority)
            VALUES (?, ?, ?, ?)
            """,
            (title, description or None, due_date or None, priority),
        )
        connection.commit()

    flash("Task added successfully.", "success")
    return redirect(url_for("main.index"))


@main.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    with get_connection() as connection:
        task = connection.execute(
            "SELECT completed FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        if task is None:
            flash("Task not found.", "error")
        else:
            new_status = 0 if task["completed"] else 1

            connection.execute(
                "UPDATE tasks SET completed = ? WHERE id = ?",
                (new_status, task_id),
            )
            connection.commit()

            flash("Task status updated.", "success")

    return redirect(url_for("main.index"))


@main.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        connection.commit()

    if cursor.rowcount:
        flash("Task deleted successfully.", "success")
    else:
        flash("Task not found.", "error")

    return redirect(url_for("main.index"))