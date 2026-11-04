**YuvaIntern — Junior Software Developer Internship

# Student Task Management System

## Project Overview
Student Task Management System is a web-based application developed using Python, Flask, HTML, CSS, and SQLite. It helps students organize, manage, and track their daily academic tasks.

## Features
- Add new tasks with title and description.
- Set task due dates.
- Assign Low, Medium, and High priorities.
- Mark tasks as completed or pending.
- Filter tasks by All, Pending, and Completed status.
- Delete tasks.
- Store task data persistently using SQLite.
- Display task statistics on the dashboard.

## Technology Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Development Environment:** Visual Studio Code / Any Python-compatible editor

## Project Structure

```text
Student_Task_Management_System/
│
├── app.py
├── app_backup.py
├── config.py
├── database.py
├── routes.py
├── tasks.db
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

## Module Description
- **app.py:** Initializes the Flask application and registers routes.
- **config.py:** Stores application configuration and database settings.
- **database.py:** Handles SQLite database connections and table initialization.
- **routes.py:** Manages task operations and application routes.
- **templates/:** Contains HTML templates.
- **static/:** Contains CSS styling.
- **tasks.db:** Stores task records.
- **requirements.txt:** Lists project dependencies.

## Installation and Setup

1. Clone or download the project repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open the browser and visit:

```text
http://127.0.0.1:5000
```

## Testing
The following functionalities have been tested:
- Application startup.
- Adding new tasks.
- Updating task completion status.
- Filtering tasks.
- Deleting tasks.
- SQLite data persistence.

## Conclusion
The project uses a modular code structure to separate application configuration, database operations, and route handling. This improves readability, maintainability, and future extensibility.