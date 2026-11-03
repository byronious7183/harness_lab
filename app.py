"""Small Flask app used for the Harness Sales Engineer candidate lab."""
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

# Shown by /version so you can tell canary and stable releases apart.
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")


def add(a, b):
    return a + b


@app.route("/")
def index():
    return jsonify(message="Hello from the Harness lab app!", version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/version")
def version():
    return jsonify(version=APP_VERSION)


@app.route("/add")
def add_route():
    try:
        a = float(request.args["a"])
        b = float(request.args["b"])
    except KeyError:
        return jsonify(error="Query parameters 'a' and 'b' are required"), 400
    except ValueError:
        return jsonify(error="'a' and 'b' must be numbers"), 400
    return jsonify(result=add(a, b))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
