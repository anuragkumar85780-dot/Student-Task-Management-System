from flask import Flask
from config import SECRET_KEY, DEBUG
from database import init_db
from routes import main

app = Flask(__name__)

app.secret_key = SECRET_KEY

app.register_blueprint(main)


@app.context_processor
def inject_app_name():
    return {"app_name": "Student Task Management System"}


if __name__ == "__main__":
    init_db()
    app.run(debug=DEBUG)