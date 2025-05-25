from flask import Flask, jsonify, request
import dao
from spotify import get_access_token, search_artist

app = Flask(__name__)

@app.before_request
def prepare_db():
    dao.init_tables()

@app.route("/spotify-token")
def spotify_token():
    try:
        token = get_access_token()
        return jsonify({"access_token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/api/artists/<int:artist_id>", methods=["GET"])
def find_by_id():
    return jsonify(dao.find_by_id)

@app.route("/api/artists", methods=["GET"])
def get_artists():
    return jsonify(dao.all_artists())

@app.route("/api/artists", methods=["POST"])
def add_artist():
    name = request.get_json().get("name")
    try:
        data = search_artist(name)
        artist_id = dao.insert_artist(data["name"], data["genre"], data["popularity"], data["spotify_id"])
        return jsonify({"id": artist_id, **data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/api/artists/<int:artist_id>", methods=["DELETE"])
def delete_artist(artist_id):
    deleted = dao.delete_artist(artist_id)
    if deleted:
        return jsonify({"message": "Artist deleted"})
    else:
        return jsonify({"error": "Artist not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
    