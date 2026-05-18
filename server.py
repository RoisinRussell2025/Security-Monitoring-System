#/bin/bash
#Author:Roisin Russell
# Program Description: Import flask to receive

import json
import os
from flask import Flask, request, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
DATA_PATH = os.path.join(DATA_DIR, "data.json")

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json

    # Save latest event to file (so dashboard can read it)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f)

    print("Received data:", data)
    return {"status": "ok"}


def load_latest_event():
    try:
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        print("Error reading data.json:", e)
        return None


@app.route("/", methods=["GET"])
def dashboard():
    last_event = load_latest_event()
    return render_template("status.html", last_event=last_event)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
