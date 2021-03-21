from .model import start_msg, guessme_msg, help_msg

def start_msg_view(a):
    return start_msg()

def guessme_msg_view(a):
    try:
        guess = int(a["g"].value[0])
        message = guessme_msg(guess)

    except ValueError as e:
        message = guessme_msg()

    return message

def help_msg_view(a):
    return help_msg()

