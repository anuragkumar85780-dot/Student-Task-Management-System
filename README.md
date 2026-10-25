# Student Task Management System

A simple web application for students to organize study tasks, track deadlines, set priority, and mark work as complete. This project is built with Python, Flask, SQLite, HTML, and CSS.

## Features

- Add tasks with a title, optional description, due date, and priority
- View all tasks, only pending tasks, or completed tasks
- Mark tasks as complete or pending
- Delete tasks
- Dashboard summary showing total, completed, and pending tasks
- SQLite database stores tasks locally

## Technology Stack

- Python 3
- Flask
- SQLite
- HTML5 and CSS3

## Requirements

- Python 3.10 or newer
- pip

## Run locally (Windows PowerShell)

1. Extract or open this project folder in VS Code.
2. Create a virtual environment:

   ```powershell
   py -m venv venv
   ```

3. Activate it:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the application:

   ```powershell
   python app.py
   ```

6. Open the local address shown in the terminal, normally http://127.0.0.1:5000.

The SQLite database file `tasks.db` is created automatically when the app starts. It is intentionally excluded from version control because it contains local task data.

## Project Structure

```text
Student_Task_Management_System/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Basic Test Checklist

- Add a task with a title.
- Try adding a task without a title; the app should show a validation message.
- Add a task with a due date and priority.
- Mark a task as complete, then mark it pending again.
- Switch between All, Pending, and Completed filters.
- Delete a task and confirm it disappears.

## Scope and Limitations

This version is intended as a beginner internship project and runs locally. It does not include user accounts, cloud hosting, email reminders, or multi-user access. Do not use real passwords or sensitive personal information in this demo.

## Future Improvements

- User login and separate task lists
- Search and sort tasks
- Calendar view and reminders
- Automated unit tests
- Deployment to a hosting service

## Author

Prepared by Anurag Kumar  
Role: Junior Software Developer Intern  
Organization: Yuva Intern  
Project: Student Task Management System
