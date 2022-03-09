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

@app.route('/books/<int:id>')

if __name__ == '__main__':
    app.run()