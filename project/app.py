from flask import Flask, jsonify, request
import dao
from spotify import get_access_token, search_artist

app = Flask(__name__)

# Prepare my artists table before handling other requests, function imported from dao
@app.before_request
def prepare_db():
    dao.init_tables()

# Receive an access token and return it as JSON
@app.route("/spotify-token")
def spotify_token():
    try:
        token = get_access_token()
        return jsonify({"access_token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Search for an artist by typing their id as a parameter   
@app.route("/api/artists/<int:artist_id>", methods=["GET"])
def find_by_id(artist_id):
    return jsonify(dao.find_by_id)

# Returns all artists in database
@app.route("/api/artists", methods=["GET"])
def get_artists():
    return jsonify(dao.all_artists())

# Insert an artist into database using spotify API search by name
@app.route("/api/artists", methods=["POST"])
def add_artist():
    name = request.get_json().get("name")
    try:
        data = search_artist(name)
        artist_id = dao.insert_artist(data["name"], data["genre"], data["popularity"], data["spotify_id"])
        return jsonify({"id": artist_id, **data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete an artist by ID  
@app.route("/api/artists/<int:artist_id>", methods=["DELETE"])
def delete_artist(artist_id):
    deleted = dao.delete_artist(artist_id)
    if deleted:
        return jsonify({"message": "Artist deleted"})
    else:
        return jsonify({"error": "Artist not found"}), 404

# Testing
if __name__ == "__main__":
    app.run(debug=True)
    