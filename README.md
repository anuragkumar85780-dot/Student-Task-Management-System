
# YuvaIntern — Junior Software Developer Internship

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
- **Testing:** pytest, Flask Test Client
- **Development Environment:** Visual Studio Code / Any Python-compatible editor

## Project Structure

```text
Student_Task_Management_System/
│
├── app.py
├── config.py
├── database.py
├── routes.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_routes.py
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
- **tests/:** Contains automated test cases for application functionality.
- **tests/test_routes.py:** Tests dashboard, task creation, validation, completion, deletion, and filters.
- **templates/:** Contains HTML templates.
- **static/:** Contains CSS styling.
- **tasks.db:** Stores application task records.
- **requirements.txt:** Lists project dependencies.

## Installation and Setup

1. Clone or download the project repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open the browser and visit:

```text
http://127.0.0.1:5000
```

## Testing and Quality Assurance

The project uses pytest and Flask's test client to perform automated testing of application features and input validation.

### Testing Strategy

The testing strategy focuses on checking the correctness, reliability, and quality of the application. Individual features and application routes are tested to verify that they work as expected.

### Testing Tools

- **pytest:** Runs automated test cases and reports test results.
- **Flask Test Client:** Tests application routes without starting a live server.
- **SQLite:** Provides a temporary database for isolated test execution.

### Automated Test Cases

The test suite covers the following scenarios:

1. Dashboard loads successfully.
2. Valid task creation.
3. Empty task title validation.
4. Invalid priority validation.
5. Invalid due-date validation.
6. Task completion status update.
7. Task deletion.
8. Pending and completed task filters.

### Run Automated Tests

Install project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the automated test suite:

```bash
python -m pytest -v
```

### Test Results

All 8 automated test cases passed successfully.

The tests use a temporary SQLite database to avoid modifying the application's actual task records.

### Quality Assurance Practices

- Validate user input before database operations.
- Use isolated test data.
- Check application functionality after code changes.
- Review test results and fix identified issues.
- Verify that existing application features continue to work after updates.

## Conclusion

The Student Task Management System uses a modular code structure to separate application configuration, database operations, and route handling. Automated testing with pytest helps verify important application features and improves software quality, reliability, and maintainability.

---

## Coding Standards and Guidelines

The Student Task Management System follows basic Python coding standards to keep the source code clean, readable, and maintainable.

### 1. Naming Conventions

- Use `snake_case` for variables and function names.
- Use `UPPER_CASE` for constants.
- Use `PascalCase` for class names.
- Use meaningful and descriptive names.

### 2. Code Formatting

- Follow PEP 8 Python style guidelines.
- Use four spaces for indentation.
- Keep code properly organized and readable.
- Separate functions with blank lines.

### 3. Documentation and Comments

- Add module-level docstrings to explain each Python file.
- Add function docstrings to describe the purpose of functions.
- Use meaningful comments for important logic.
- Keep comments clear, short, and relevant.

### 4. Error Handling and Security

- Validate user input before saving data.
- Use parameterized SQL queries to help prevent SQL injection.
- Handle invalid dates and missing task information.
- Keep configuration settings in `config.py`.

### 5. Documentation Tools

- **Pydoc:** Can generate documentation from Python modules and docstrings.
- **Sphinx:** Can create structured project documentation in HTML and other formats.

### 6. Code Maintenance

- Keep database operations in `database.py`.
- Keep application routes in `routes.py`.
- Keep application settings in `config.py`.
- Keep the main Flask application setup in `app.py`.
- Keep automated tests in the `tests/` directory.
- Test the application after code changes.
