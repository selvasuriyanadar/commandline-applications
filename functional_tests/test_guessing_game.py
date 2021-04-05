from guessing_game.commands import run
from guessing_game.model import Stat
from unittest import TestCase
import json

class TestGuessingGame(TestCase):

    def play_game_knowing_secret(self, secret):

        # She guessed a small number

        if secret:
            args = ["-g", str(secret-1)]
            output = run(args)
            self.assertIn("Oww! try again you can reach me. Push it a little further!", output)

        # She guessed a large number

        args = ["-g", str(secret+1)]
        output = run(args)
        self.assertIn("Opps! you went a little further, but were just there. Come on don't giveup now!", output)

        # She suddenly inputted a non number

        args = ["-g", "g"]
        output = run(args)
        self.assertIn("Your guess is expected to be a number only. Please try again.", output)

        # She guessed the correct number

        args = ["-g", str(secret)]
        output = run(args)
        self.assertIn("Yey! you have guessed my secret. I am so happy for you.", output)

        # She just like that inputted a non number

        args = ["-g", "g"]
        output = run(args)
        self.assertIn("Don't worry we are together. We will always be together!", output)

        # She inputted a number after successfully completing the game
        # in a mood to explore.

        args = ["-g", str(secret)]
        output = run(args)
        self.assertIn("Don't worry we are together. We will always be together!", output)

        # She just like that inputted a big number

        args = ["-g", str(100000)]
        output = run(args)
        self.assertIn("Don't worry we are together. We will always be together!", output)

    def test_getting_help_about_the_game_play(self):
        # Sana wonders what the command line game is about
        # and how to play it.
        # She runs the app with h option in hope to get some help

        args = ["-h"]
        output = run(args)
        self.assertIn("Try to guess the number I am thinking of!", output)

    def test_gameplay_with_start_step(self):
        # Sana starts the game

        args = ["-s"]
        output = run(args)
        self.assertIn("Now the game begins. Come on start your guesses, you have to get to me!", output)

        with Stat() as stat_store:
            secret = stat_store.getStat()["random_integer"]

        # Then she enters a guess

        self.play_game_knowing_secret(secret)

        # She resets the game and plays again

        args = ["-s"]
        output = run(args)
        with Stat() as stat_store:
            secret = stat_store.getStat()["random_integer"]
        self.play_game_knowing_secret(secret)

    def test_gameplay_skipping_the_start_step(self):
        with Stat() as stat_store:
            stat_store.resetStat()
            secret = stat_store.getStat()["random_integer"]
        
        # Sana quikly enters a guess

        self.play_game_knowing_secret(secret)

