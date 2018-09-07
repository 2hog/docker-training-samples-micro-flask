from flask import Flask, request
from flask import render_template
import sec


AUTH_USER = sec.load("AUTH_USER", "antonis")
AUTH_PASSWORD = sec.load("AUTH_PASSWORD", "kalipetis")

app = Flask(__name__)


@app.route("/")
def home():
    greeting = request.args.get("greeting")
    authorization = request.authorization or {"username": None, "password": None}
    username = authorization["username"]
    password = authorization["password"]

    if username != AUTH_USER or password != AUTH_PASSWORD:
        return render_template("not-authorized.html"), 401

    return render_template("index.html", greeting=greeting)
