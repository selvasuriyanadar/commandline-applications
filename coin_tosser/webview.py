from .model import start_game
from .view import toss_view, help_view
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/start', methods=['POST'])
def start_api_view():
    coin_str = request.get_json()['head_or_tail']
    if coin_str == "head":
        coin = True
    elif coin_str == "tail":
        coin = False
    else:
        return "Enter head or tail"

    start_game(coin)
    return "The game begins now!"

@app.route('/api/toss', methods=['POST'])
def toss_api_view():
    return toss_view(None)

@app.route('/api/help')
def help_api_view():
    return help_view(None)

