"""demo-petstore: a tiny Flask app for the agent-SDLC demo.

Not a real product. This exists so an agent can make a small, visible code
change in front of an audience, build it, and ship it through staging/prod
namespaces on a kind cluster.
"""
from flask import Flask, jsonify

app = Flask(__name__)

PETS = [
    {"id": 1, "name": "Biscuit", "species": "Dog", "emoji": "\U0001F436"},
    {"id": 2, "name": "Marmalade", "species": "Cat", "emoji": "\U0001F408"},
    {"id": 3, "name": "Pip", "species": "Rabbit", "emoji": "\U0001F430"},
    {"id": 4, "name": "Nimbus", "species": "Bird", "emoji": "\U0001F426"},
]


@app.get("/")
def index():
    from flask import render_template
    return render_template("index.html", pets=PETS)


@app.get("/api/pets")
def api_pets():
    return jsonify(PETS)


@app.get("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
