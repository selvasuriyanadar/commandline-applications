from random import randint
from paraivari.parser import parse
import sys
import json

# view

config_data = {
        "thedirectcommand": {
            "short_input_names": [],
            "long_input_names": {},
            "positional_arguments": [],
            "argument_value_properties": {},
            "global_defaults": {},
            "boolean_params": [],
            "switches": ["h"],
            "overloading": [
                            {
                    "local": ["h"],
                    "local_defaults": {},
                    "func": lambda a: "Try to guess the number I am thinking of!"
                }
            ]
        }
    }

# control

parse(sys.argv[1:], config_data)

def start_cntrl(a):
    pass

def guessme_cntrl(a):
    pass
    
# model

def guessme():
    guessed = False
    number = randint(0, 100)
    guesses = 0

def start():
    pass
