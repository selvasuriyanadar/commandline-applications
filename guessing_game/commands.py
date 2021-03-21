from .controller import help_msg_cntrl, start_msg_cntrl, guessme_msg_cntrl

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
                    "func": help_msg_cntrl
                },
                            {
                    "local": ["s"],
                    "local_defaults": {},
                    "func": start_msg_cntrl
                },
                            {
                    "local": ["g"],
                    "local_defaults": {},
                    "func": guessme_msg_cntrl
                },
            ]
        }
    }

