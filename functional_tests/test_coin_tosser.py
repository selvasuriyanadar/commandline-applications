from unittest import TestCase
from coin_tosser.model import show_result
from coin_tosser.commands import run
users = ["first user", "second user", "third user", "fourth user"]
coins = ["head", "tail"]

class TestCoinTosser(TestCase):

    def test_coin_tosser(self):
        # prakash starts the game he sets head to be the winner declarer
        args = ["-s", "head"]
        self.assertIn("The game begins now!", run(args))

        args = ["-s", "tail"]
        self.assertIn("The game begins now!", run(args))

        args = ["-s", "had"]
        self.assertIn("Enter head or tail", run(args))

        # He tosses the coin
        # He can see his tossed coin
        args = ["-t"]
        result = run(args).lower()
        self.assertTrue(users[0] in result)
        self.assertTrue(any(coin in result for coin in coins))

        # then his friend Kottai tosses the coin
        # he can also see his tossed coin
        args = ["-t"]
        result = run(args).lower()
        self.assertTrue(users[1] in result)
        self.assertTrue(any(coin in result for coin in coins))

        # They play for five turns each, one after the other changing turns
        for _ in range(0, 5*len(users)-2):
            args = ["-t"]
            run(args)

        # then they can see the result of their game
        # Either prakash or kottai scored the most of the head or tail as set
        # on the start of the game and the player with the greater points is
        # declared the winner
        args = ["-t"]
        result = run(args).lower()
        self.assertTrue(all(user in result for user in users))
        self.assertIn("winner", result)
        if len(show_result()[1]) > 1:
            self.assertIn("winners", result)
            self.assertIn("are", result)
        else:
            self.assertIn("is", result)
