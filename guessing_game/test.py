from .model import start_msg, guessme_msg, help_msg, GuessMe, Stat
from .data.string import guessme_strings
import json
import unittest

class TestModel(unittest.TestCase):
    
    def test_help_function_message_output(self):
        self.assertEqual(help_msg(), guessme_strings["help"])

    def test_initialisation_of_random_integer(self):
        stat_store = Stat()
        start_msg()
        stat = stat_store.getStat()
        self.assertIn("random_integer", stat)
        self.assertIn("guessed", stat)
        self.assertIn("guesses", stat)

    def test_start_function_message_output(self):
        self.assertEqual(start_msg(), guessme_strings["start"])

    def test_GuessMe_class_serialisation(self):
        guess_me = GuessMe({
                "random_integer":40,
                "guessed":False,
                "guesses":0
            })
        stat = guess_me.getStat()
        self.assertIn("random_integer", stat)
        self.assertIn("guessed", stat)
        self.assertIn("guesses", stat)

    def test_guessme_msg_function_small_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(guessme_msg(secret+1), guessme_strings["large_guess"])

    def test_guessme_msg_function_small_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(guessme_msg(secret-1), guessme_strings["small_guess"])

    def test_guessme_msg_function_small_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(
            guessme_msg(secret),
            guessme_strings["correct_guess"].format(1)
        )

    def test_guessme_msg_function_small_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(
            guessme_msg(secret),
            guessme_strings["correct_guess"].format(1)
        )
        self.assertEqual(guessme_msg(1000), guessme_strings["already_guessed"])

class TestController(unittest.TestCase):
    
    def test_guessme_input_and_output(self):
        pass

