from .controller import help_msg_cntrl

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
                    "func": help_msg_cntrl
                }
            ]
        }
    }

