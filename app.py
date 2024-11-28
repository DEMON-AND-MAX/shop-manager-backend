import flask
from flask import Flask, request, jsonify
from flask_cors import CORS

APP_NAME = "Shop Manager Backend"
APP_DEV = "Amalia Matioc, Maximilian Todea, Ariana Radu"

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def app_base():
    return "Hello world! " + APP_NAME

@app.route('/get', methods=['GET'])
def app_get():
    response = jsonify({
        "message": "Response from " + APP_NAME + " by " + APP_DEV + "."
        })
    return response

@app.route('/post', methods=['POST'])
def app_post():
    data = request.get_json()
    print(data)
    response = jsonify({
        "message": "Response from " + APP_NAME + " by " + APP_DEV + ".",
        "data": data,
    })
    return response

if __name__ == '__main__':
    app.run(debug=True)