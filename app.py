
"""
Main application module for the Student Task Management System.

Creates the Flask application, registers routes, and starts the server.
"""

from flask import Flask
from config import SECRET_KEY, DEBUG
from database import init_db
from routes import main

# Create the Flask application instance.
app = Flask(__name__)

# Configure the application's secret key.
app.secret_key = SECRET_KEY

# Register the main application routes.
app.register_blueprint(main)


@app.context_processor
def inject_app_name():
    """Make the application name available in all templates."""
    return {"app_name": "Student Task Management System"}


if __name__ == "__main__":
    # Initialize the database before starting the application.
    init_db()
    app.run(debug=DEBUG)
