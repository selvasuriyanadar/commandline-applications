from random import randint
import json
from json import JSONDecodeError
from .data.strings import guessme_strings
from importlib import resources

# drivers

# string

def help_msg():
    return guessme_strings["help"]

# string and data access

def start_msg():
    stat_store = Stat()
    stat_store.resetStat()

    return guessme_strings["start"]

def guessme_msg(guess=None):
    stat_store = Stat()
    guess_me = GuessMe(stat_store.getStat())

    if guess is not None and not guess_me.hasGuessed():
        message = guessme(guess_me, guess)
    elif guess_me.hasGuessed():
        message = guessme_strings["already_guessed"]
    else:
        message = guessme_strings["guess_error"]

    stat_store.putStat(guess_me.getStat())
    return message 

# string and logic access

def guessme(guess_me, guess):
    if guess_me.guessme(guess):
        message = guessme_strings["correct_guess"].format(guess_me.getGuesses())

    elif guess_me.isGuessLarge(guess):
        message = guessme_strings["large_guess"]

    elif guess_me.isGuessSmall(guess):
        message = guessme_strings["small_guess"]

    else:
        raise NotGuessable
    return message


# logic

class AlreadyGuessed(Exception):
    pass

class NotGuessable(Exception):
    pass

class GuessMe:
    """
    fields:
       secret is immutable integer.
       guessed which is initially False, is toggleable only once when the
    guess received matches the secret.
       guesses(initially zero) is incremented every once when a guess is
    received.

    incomming:
       guess an integer.
    """
    def __init__(self, stat):
        self._secret = stat["random_integer"]
        self._guessed = stat["guessed"]
        self._guesses = stat["guesses"]

    def isGuessLarge(self, guess):
        return self._secret < guess

    def isGuessSmall(self, guess):
        return self._secret > guess

    def hasGuessed(self):
        return self._guessed

    def getGuesses(self):
        return self._guesses

    def guessme(self, guess):
        if not self.hasGuessed():
            self._newGuess(guess)
            return self._matchGuess(guess)
        else:
            raise AlreadyGuessed

    def _newGuess(self, guess):
        self._guesses+=1

    def _matchGuess(self, guess):
        if guess == self._secret:
            self._guessed = True
            return True
        return False

    def getStat(self):
        return {
                "random_integer": self._secret,
                "guessed": self._guessed,
                "guesses": self._guesses,
            }


# data

class StatMisformed(Exception):
    pass

class StatsNotEquivalent(Exception):
    pass

class Stat:
    """
    storage:
       path holds the path of a json file.

    value:
       random_integer an int which defaults to any random integer.
       guessed is a bool, default is False.
       guesses is an int, default is 0.

    getStat:
       if a valid stat is not get then returns default stat
    """
    def __init__(self):
        with resources.path(
                "guessing_game.data",
                "random_integer.json"
            ) as path:
            self._path = path

    def getStat(self):
        try:
            with open(self._path) as f:
                stat = json.load(f)
            self.validateStat(stat)

        except (FileNotFoundError, JSONDecodeError, StatMisformed) as e:
            stat = self.defaultStat()

        return stat

    def putStat(self, stat):
        with open(self._path, "w") as f:
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
        if all(k in stat for k in ["random_integer", "guessed", "guesses"]):
            if (isinstance(stat["random_integer"], int) and
                isinstance(stat["guessed"], bool) and
                isinstance(stat["guesses"], int)):
                return True
        raise StatMisformed

    def assertEquivalent(self, stat1, stat2):
        self.validateStat(stat1)
        self.validateStat(stat2)
        if (stat1["guessed"] is stat2["guessed"] and
            stat1["guesses"] is stat2["guesses"]):
            return True
        raise StatsNotEquivalent

