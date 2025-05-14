from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.get_json()
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