from flask import Flask, jsonify
from flask_cors import CORS
import os
import time

app = Flask(__name__)
CORS(app)

VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/health")
def health():
    return "OK", 200

@app.route("/version")
def version():
    return jsonify({"version": VERSION})

@app.route("/pay", methods=["POST"])
def pay():
    if VERSION == "v2":
        time.sleep(3)
        return jsonify({
            "status": "FAILED",
            "message": "Buggy version detected"
        }), 500

    return jsonify({
        "status": "SUCCESS",
        "message": "Payment processed"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

