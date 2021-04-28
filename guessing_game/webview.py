from .model import guessme, start
from flask import Flask, request

app = Flask(__name__)

# API

@app.route("/api/guessme", methods=['PUT'])
def start_api_view():
    start()
    return {'status': 'success'}

@app.route("/api/guessme", methods=['POST'])
def guessme_msg_view():
    try:
        guess = int(request.get_json()['guess'])
        result = guessme(guess)

    except ValueError as e:
        result = guessme()

    return result
