from .model import start_msg, guessme_msg, GuessMe, Stat
from .view import guessme_msg_view
from .data.strings import guessme_strings
from paraivari.payanam.koththisarukku.ArgumentExtractionLib import Argument
import json, unittest
from importlib import resources

class TestGuessMeLogicClass(unittest.TestCase):

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

class TestStatDataClass(unittest.TestCase):

    def test_does_the_random_integer_json_file_exists(self):
        with resources.path(
                "guessing_game.data",
                "random_integer.json"
            ) as path:
            pass

    def test_getStat_when_file_has_invalid_json(self):
        stat_store = Stat()
        with open(stat_store._path, "w") as f:
            f.write("")
            stat_store.assertEquivalent(stat_store.getStat(), stat_store.defaultStat())

    def test_getStat_when_file_has_invalid_stat(self):
        stat_store = Stat()
        with open(stat_store._path, "w") as f:
            f.write("{}")
            stat_store.assertEquivalent(stat_store.getStat(), stat_store.defaultStat())

    def test_if_file_is_correctly_updated_after_a_putStat(self):
        stat_store = Stat()
        stat = {
            "random_integer":40,
            "guessed":True,
            "guesses":40
        }
        stat_store.putStat(stat)
        stat_store.assertEquivalent(stat_store.getStat(), stat)

class TestModel(unittest.TestCase):
    
    def test_initialisation_of_random_integer(self):
        stat_store = Stat()
        start_msg()
        stat = stat_store.getStat()
        self.assertIn("random_integer", stat)
        self.assertIn("guessed", stat)
        self.assertIn("guesses", stat)

    def test_start_function_message_output(self):
        self.assertEqual(start_msg(), guessme_strings["start"])

    def test_guessme_msg_function_large_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(guessme_msg(secret+1), guessme_strings["large_guess"],
            f"the secret is {secret}")

    def test_guessme_msg_function_small_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(guessme_msg(secret-1), guessme_strings["small_guess"],
            f"the secret is {secret}")

    def test_guessme_msg_function_correct_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(
            guessme_msg(secret),
            guessme_strings["correct_guess"].format(1),
            f"the secret is {secret}"
        )

    def test_guessme_msg_function_guess_after_correct_guess(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertEqual(
            guessme_msg(secret),
            guessme_strings["correct_guess"].format(1),
            f"the secret is {secret}"
        )
        self.assertEqual(guessme_msg(1000), guessme_strings["already_guessed"])

class TestController(unittest.TestCase):
    
    def test_guessme_input_and_output(self):
        stat_store = Stat()
        start_msg()
        secret = stat_store.getStat()["random_integer"]
        self.assertTrue(isinstance(
            guessme_msg_view(
                {"g": Argument("g", [secret+1], 1)}
            ),
            str
        ))
        self.assertEqual(
            guessme_msg_view(
                {"g": Argument("g", ["g"], 1)}
            ),
            guessme_strings["guess_error"]
        )

