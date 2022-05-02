from flask import jsonify
from warchest import app, errors

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_personal(name):
    return f"Hello, {name}"

@app.route('/do_something', methods=["POST"])
def do_something():
    return jsonify({"message": "I did a thing"})
