from flask import Flask

app = Flask(__name__) 

@app.route('/')
def index():
    return 'Flask API'

# Dynamic Routing 

@app.route('/<name>')
def print_name(name):
    return 'Hi , {}'.format(name)

app.run(debug=True)