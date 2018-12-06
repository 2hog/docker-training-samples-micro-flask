import os

from flask import Flask, request
from flask import render_template
import sec


ENVIRONMENT = os.getenv("ENVIRONMENT", "production")
AUTH_USER = sec.load("AUTH_USER", "antonis")
AUTH_PASSWORD = sec.load("AUTH_PASSWORD", "kalipetis")

app = Flask(__name__)


@app.route("/")
def home():
    greeting = request.args.get("greeting")
    authorization = request.authorization or {"username": None, "password": None}
    username = authorization["username"]
    password = authorization["password"]
    context = {
        'greeting': greeting,
        'environment': ENVIRONMENT,
    }

    if username != AUTH_USER or password != AUTH_PASSWORD:
        headers = {
            'WWW-Authenticate':'Basic realm="Login Required"',
        }
        return render_template("not-authorized.html", **context), 401, headers

    return render_template("index.html", **context)
