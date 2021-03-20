from .model import start
import json
import unittest

class TestModel(unittest.TestCase):
    
    def test_initialisation_of_random_integer(self):
        start()
        with open("guessing_game/data/random_integer.json") as f:
            self.assertIn("random_integer", json.load(f))

