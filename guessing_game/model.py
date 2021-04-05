from .data.strings import guessme_strings
from .data.data import StatDb as Stat

# controller

# string

def help_msg():
    return guessme_strings["help"]

# string and data access

def start_msg():
    with Stat() as stat_store:
        stat_store.resetStat()

    return guessme_strings["start"]

def guessme_msg(guess=None):
    with Stat() as stat_store:
        guess_me = GuessMe(stat_store.getStat())

    if guess is not None and not guess_me.hasGuessed():
        message = guessme(guess_me, guess)
    elif guess_me.hasGuessed():
        message = guessme_strings["already_guessed"]
    else:
        message = guessme_strings["guess_error"]

    with Stat() as stat_store:
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

