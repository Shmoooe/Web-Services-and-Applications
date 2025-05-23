from flask import Flask, jsonify, request
import dao
from spotify import get_access_token

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

@app.route("/api/artists", methods=["GET"])
def get_artists():
    return jsonify(dao.all_artists())

@app.route("/api/artists", methods=["POST"])
def add_artist():
    name = request.get_json().get("name")
    data = search_artist(name)
    
    new_book = {"id": len(books)+1, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == "__main__":
    app.run(debug=True)
    