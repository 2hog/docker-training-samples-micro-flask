import os

from flask import Flask, request
from flask import render_template
import sec


AUTH_USER = sec.load("AUTH_USER", "antonis")
AUTH_PASSWORD = sec.load("AUTH_PASSWORD", "kalipetis")

DEBUG = os.getenv("FLASK_DEBUG") == "1"
ENVIRONMENT = os.getenv("FLASK_ENV", "development")

app = Flask(__name__)


@app.route("/")
def home():
    greeting = request.args.get("greeting", "Hello")
    authorization = request.authorization or {"username": None, "password": None}
    username = authorization["username"]
    password = authorization["password"]
    context = {"greeting": greeting, "environment": ENVIRONMENT, "debug": DEBUG}

    if username != AUTH_USER or password != AUTH_PASSWORD:
        headers = {"WWW-Authenticate": 'Basic realm="Login Required"'}
        return render_template("not-authorized.html", **context), 401, headers

    return render_template("index.html", **context)
