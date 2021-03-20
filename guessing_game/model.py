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
    stat_store = Stat()
    stat_store.resetStat()
    return guessme_strings["start"]

# string, data and logic access

def guessme_msg(guess):
    stat_store = Stat()
    guess_me = GuessMe(stat_store.getStat())
    if not guess_me.hasGuessed():

        if guess_me.guessme(guess):
            stat_store.putStat(guess_me.getStat())
            message = guessme_strings["correct_guess"].format(guess_me.guesses)

        elif guess_me.isGuessLarge(guess):
            stat_store.putStat(guess_me.getStat())
            message = guessme_strings["large_guess"]

        else:
            stat_store.putStat(guess_me.getStat())
            message = guessme_strings["small_guess"]

    else:
        message = guessme_strings["already_guessed"]

    return message 


# data

class Stat:

    def __init__(self):
        self.path = "guessing_game/data/random_integer.json"

    def getStat(self):
        with open(self.path) as f:
            try:
                stat = json.load(f)

                if not self.validateStat(stat):
                    stat = self.defaultStat()
    
            except JSONDecodeError as e:
                stat = self.defaultStat()

            return stat

    def putStat(self, stat):
        with open(self.path, "w") as f:
            json.dump(stat, f)
    
    def resetStat(self):
        self.putStat(self.defaultStat())
    
    def defaultStat(self):
        return {
                "random_integer": randint(0, 100),
                "guessed": False,
                "guesses": 0,
            }

    def validateStat(self, stat):
        isvalid = False
        if all(k in stat for k in ["random_integer", "guessed", "guesses"]):
            if (isinstance(stat["random_integer"], int) and
                isinstance(stat["guessed"], bool) and
                isinstance(stat["guesses"], int)):
                isvalid = True
        return isvalid
