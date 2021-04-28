from .data.strings import guessme_strings
from .data.data import StatDb as Stat

# controller

# string access

def help_msg():
    return guessme_strings["help"]

def guess_result_msg(guess_result):
    if guess_result["result"] == "match":
        message = guessme_strings["correct_guess"].format(guess_result["guesses"])
    elif guess_result["result"] == "big":
        message = guessme_strings["large_guess"]
    elif guess_result["result"] == "small":
        message = guessme_strings["small_guess"]
    else:
        raise NotGuessable
    return message

def start_msg():
    start()
    return guessme_strings["start"]

def guessme_msg(guess=None):
    result = guessme(guess)
    if result["status"] == "success":
        message = guess_result_msg(result["guess_result"])
    elif result["status"] == "already complete":
        message = guessme_strings["already_guessed"]
    elif result["status"] == "error":
        message = guessme_strings["guess_error"]
    else:
        raise NotGuessable
    return message

# logic and data access

def start():
    with Stat() as stat_store:
        stat_store.resetStat()

def guessme(guess=None):

    def build_result(guess_result, status):
        return {
            "guess_result": guess_result,
            "status": status,
        }

    with Stat() as stat_store:
        guess_me = GuessMe(stat_store.getStat())

    if guess is not None and not guess_me.hasGuessed():
        result = build_result(guess_me.guessme(guess), "success")
    elif guess_me.hasGuessed():
        result = build_result({}, "already complete")
    else:
        result = build_result({}, "error")

    with Stat() as stat_store:
        stat_store.putStat(guess_me.getStat())

    return result

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

    def hasGuessed(self):
        return self._guessed

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
            return self._guessResult(guess, "match")
        elif guess > self._secret:
            return self._guessResult(guess, "big")
        elif guess < self._secret:
            return self._guessResult(guess, "small")

    def _guessResult(self, guess, result):
        return {
            "guess": guess,
            "result": result,
            "guesses": self._guesses,
        }

    def getStat(self):
        return {
            "random_integer": self._secret,
            "guessed": self._guessed,
            "guesses": self._guesses,
        }

