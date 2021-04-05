from .model import start_msg, guessme_msg, help_msg
from .view import start_msg_view, help_msg_view, guessme_msg_view
from flask import Flask, render_template, request

app = Flask(__name__)

# VIEW

@app.route("/")
def home_view():
    return render_template('home.html')

@app.route("/game")
def game_view():
    return render_template('game.html')

@app.route("/help")
def help_view():
    return render_template('help.html')

# API

@app.route("/api/start", methods=['POST'])
def start_api_view():
    return start_msg_view(None)

@app.route("/api/guess", methods=['POST'])
def guessme_msg_view():
    try:
        guess = int(request.get_json()['guess'])
        message = guessme_msg(guess)

    except ValueError as e:
        message = guessme_msg()

    return message

@app.route("/api/help")
def help_api_view():
    return help_msg_view(None)

