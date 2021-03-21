from .view import help_msg_view, start_msg_view, guessme_msg_view
from paraivari.parser import parseLog as parse

def run(args):
    return parse(args, config_data)

config_data = {
        "thedirectcommand": {
            "short_input_names": [],
            "long_input_names": {},
            "positional_arguments": [],
            "argument_value_properties": {
                    "g": [1],
                },
            "global_defaults": {},
            "boolean_params": [],
            "switches": ["h", "s"],
            "overloading": [
                            {
                    "local": ["h"],
                    "local_defaults": {},
                    "func": help_msg_view
                },
                            {
                    "local": ["s"],
                    "local_defaults": {},
                    "func": start_msg_view
                },
                            {
                    "local": ["g"],
                    "local_defaults": {},
                    "func": guessme_msg_view
                },
            ]
        }
    }

