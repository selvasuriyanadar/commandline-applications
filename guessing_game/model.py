from random import randint
import json

def guessme():
    guessed = False
    guesses = 0

def start():
    with open("guessing_game/data/random_integer.json", "w") as f:
        json.dump({"random_integer": randint(0, 100)}, f)

def help_msg():
    return "Try to guess the number I am thinking of!"

