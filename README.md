# Student Task Management System

**Yuva Intern — Junior Software Developer Internship | Week 2 Project**

A beginner-friendly task management web app built with Python, Flask, HTML, CSS, and SQLite.

## Features
- Add tasks with title, optional description, due date, and priority
- View All, Pending, and Completed tasks
- Mark tasks complete or pending
- Delete tasks with confirmation
- Dashboard summary for total, pending, and completed tasks
- Server-side validation and parameterized SQLite queries
- Responsive layout for desktop and mobile screens

## Requirements
- Python 3.10 or newer
- pip

## Run on Windows PowerShell
1. Open this folder in VS Code.
2. Create a virtual environment:
   ```powershell
   py -m venv venv
   ```
3. Activate it:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt and run:
   ```bat
   venv\Scripts\activate.bat
   ```
4. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Start the app:
   ```powershell
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.

The `tasks.db` SQLite file is created automatically when the app starts. It is excluded from Git because it contains local task data.

## Project Structure
```text
Student_Task_Management_System_Week2/
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
- Add a task with a title
- Try adding a blank title and confirm validation appears
- Add a due date and priority
- Mark a task complete, then mark it pending again
- Switch between All, Pending, and Completed filters
- Delete a task and confirm it disappears
- Confirm dashboard counts update correctly
- Restart the app and confirm tasks remain in SQLite

## Security Notes
- SQL queries use placeholders for user-provided values.
- State-changing actions use POST routes.
- Jinja auto-escapes user-entered text in templates.
- The fallback secret key is for local development only. Set `FLASK_SECRET_KEY` to a strong secret before any deployment.
- Flask debug mode is enabled only for local development. Do not expose the development server publicly.
- This demo does not include user accounts and should not store passwords or sensitive personal information.

## Scope
This is a local, single-user internship project. Authentication, multi-user access, reminders, and cloud deployment are future enhancements.
