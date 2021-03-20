from random import randint
import json
from .data.string import guessme_strings

# logic

class GuessMe:

    def __init__(self, stat):
        self.secret = stat["random_integer"]
        self.guessed = stat["guessed"]
        self.guesses = stat["guesses"]

    def isGuessLarge(self, guess):
        return self.secret < guess

    def isGuessSmall(self, guess):
        return self.secret > guess

    def hasGuessed(self):
        return self.guessed

    def guessme(self, guess):
        self.newGuess(guess)
        return self.matchGuess(guess)

    def newGuess(self, guess):
        self.guesses+=1

    def matchGuess(self, guess):
        if guess == self.secret:
            self.guessed = True
            return True
        return False

    def getStat(self):
        return {
                "random_integer": self.secret,
                "guessed": self.guessed,
                "guesses": self.guesses,
            }


# string access

def help_msg():
    return guessme_strings["help"]

# string and data access

def start_msg():
    putStat(
        {
            "random_integer": randint(0, 100),
            "guessed": False,
            "guesses": 0,
        }
    )
    return guessme_strings["start"]

# string, data and logic access

def guessme_msg(guess):
    guess_me = GuessMe(getStat())
    if not guess_me.hasGuessed():

        if guess_me.guessme(guess):
            putStat(guess_me.getStat())
            message = guessme_strings["correct_guess"].format(guess_me.guesses)

        elif guess_me.isGuessLarge(guess):
            putStat(guess_me.getStat())
            message = guessme_strings["large_guess"]

        else:
            putStat(guess_me.getStat())
            message = guessme_strings["small_guess"]
    else:
        message = guessme_strings["already_guessed"]

    return message 


# direct data access

def getStat():
    with open("guessing_game/data/random_integer.json") as f:
        return json.load(f)

def putStat(stat):
    with open("guessing_game/data/random_integer.json", "w") as f:
        json.dump(
            stat,
            f
        )

