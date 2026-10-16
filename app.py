import os
from flask import Flask, jsonify

app = Flask(__name__)

ITEMS = [{"id": 1, "name": "alpha"}, {"id": 2, "name": "beta"}]

@app.get("/")
def index():
    return jsonify(
        message="Hello from Cloud Run",
        env=os.getenv("APP_ENV", "local"),
        version=os.getenv("APP_VERSION", "dev"),
    )

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/items")
def items():
    return jsonify(ITEMS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
