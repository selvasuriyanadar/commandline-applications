from .view import start_view, toss_view, help_view
from paraivari.parser import parseLog as parse

def run(args):
    return parse(args, config_data)

config_data = {
        "thedirectcommand": {
            "short_input_names": [],
            "long_input_names": {},
            "positional_arguments": [],
            "argument_value_properties": {
                "s": [1],
            },
            "global_defaults": {},
            "boolean_params": [],
            "switches": ["h", "t"],
            "overloading": [
                            {
                    "local": ["h"],
                    "local_defaults": {},
                    "func": help_view
                },
                            {
                    "local": ["s"],
                    "local_defaults": {},
                    "func": start_view
                },
                            {
                    "local": ["t"],
                    "local_defaults": {},
                    "func": toss_view
                },
            ]
        }
    }

