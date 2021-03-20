from .model import help_msg, start_msg, guessme_msg

def start_msg_cntrl(a):
    return start_msg()

def guessme_msg_cntrl(a):
    return guessme_msg(int(a["g"].value[0]))

def help_msg_cntrl(a):
    return help_msg()

