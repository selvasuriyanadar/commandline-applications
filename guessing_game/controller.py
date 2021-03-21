from .model import start_msg, guessme_msg
from .data.strings import guessme_help_strings

def start_msg_cntrl(a):
    return start_msg()

def guessme_msg_cntrl(a):
    try:
        guess = int(a["g"].value[0])
        message = guessme_msg(guess)
        
    except ValueError as e:
        message = guessme_help_strings["guess_error"]

    return message

def help_msg_cntrl(a):
    return guessme_help_strings["help"]

