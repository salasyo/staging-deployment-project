import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        application="Staging Deployment Project",
        environment=os.getenv("APP_ENV", "development"),
    )


@app.get("/health")
def health():
    return jsonify(
        status="ok",
        environment=os.getenv("APP_ENV", "development"),
    )


@app.get("/version")
def version():
    return jsonify(
        version="1.0.0",
        commit=os.getenv("BUILD_SHA", "local"),
    )
