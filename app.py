from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_characters():
    url = "https://rickandmortyapi.com/api/character/"
    params = {
        "species": "Human",
        "status": "Alive",
        "origin": "Earth"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "results" in data:
            return data["results"]
        else:
            return []
    except requests.RequestException:
        return []

@app.route("/api/characters", methods=["GET"])
def get_all_characters():
    characters = get_characters()
    return jsonify(characters)

@app.route("/api/characters/<int:char_id>", methods=["GET"])
def get_character_by_id(char_id):
    characters = get_characters()
    character = next((char for char in characters if char["id"] == char_id), None)
    if character:
        return jsonify(character)
    else:
        return jsonify({"error": "Character not found"}), 404

# Healthcheck endpoint
@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(debug=True)
