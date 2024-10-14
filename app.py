from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {'id': 1, 'title': 'book1', 'author': 'p1'},
    {'id': 2, 'title': 'book2', 'author': 'p2'},
    {'id': 3, 'title': 'book3', 'author': 'p3'}
]


# retrieve all books  1st endpoint
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# retrieve book by id  2rd endpoint
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for item in books:
        if item['id'] == id:
           book = item
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404

# add a new book  3th endpoint
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if books:
        new_book['id'] = books[-1]['id'] + 1
    else:
        new_book['id'] = 1
    books.append(new_book)
    return jsonify(new_book), 201

# update an existing book  4th endpoint
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    for item in books:
        if item['id'] == id:
            book = item
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404

# delete a book or a journal  5th endpoint
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    if id in [book['id'] for book in books]:
        books = [book for book in books if book['id'] != id]
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
