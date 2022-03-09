from flask import Flask,Request,jsonify, request


app = Flask(__name__)

books_list = [
    {
        'name':'java',
        'pages':'150'
    },
    {
        'name':'python',
        'pages':'100'
    },
    {
        'name':'c',
        'pages':'10'
    },
    {
        'name':'c++',
        'pages':'70'
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

        new_obj = {
            'name':new_name,
            'pages':new_pages
        }
        books_list.append(new_obj)
        return jsonify(books_list)

if __name__ == '__main__':
    app.run()