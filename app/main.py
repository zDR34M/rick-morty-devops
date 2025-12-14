from flask import Flask, jsonify
from rick_morty import fetch_characters, write_csv

app = Flask(__name__)

characters = fetch_characters()
write_csv(characters)

@app.route("/characters")
def get_characters():
    return jsonify(characters)

@app.route("/healthcheck")
def healthcheck():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
