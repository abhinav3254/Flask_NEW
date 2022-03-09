
from flask import Flask,Request,jsonify, request


app = Flask(__name__)

books_list = [
    {
        'name':'java',
        'pages':'150',
        'id':0
    },
    {
        'name':'python',
        'pages':'100',
        'id':1

    },
    {
        'name':'c',
        'pages':'10',
        'id':2
    },
    {
        'name':'c++',
        'pages':'70',
        'id':3
    }
]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if len(books_list)>0:
            return jsonify(books_list)

    if request.method == 'POST':
        new_name = request.form['name']
        new_pages = request.form['pages']
        iD = books_list[-1]['id']+1

        new_obj = {
            'name':new_name,
            'pages':new_pages,
            'id':iD
        }
        books_list.append(new_obj)
        return jsonify(books_list)

@app.route('/books/<int:id>',methods=['GET','PUT','DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['name'] = request.form['name']
                book['pages'] = request.form['pages']

                update_book = {
                    'name':book['name'],
                    'pages':book['pages'],
                    'id':id
                }

                return jsonify(update_book)

    if request.method == 'DELETE':
        for index , book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)


if __name__ == '__main__':
    app.run()