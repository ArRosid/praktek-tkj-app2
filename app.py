import os
import socket
from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "App2")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def index():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        hostname=socket.gethostname(),
        now=datetime.now().strftime("%d %b %Y, %H:%M:%S"),
    )


@app.route("/health")
def health():
    return jsonify(status="ok", app=APP_NAME, version=APP_VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5001)), debug=True)
