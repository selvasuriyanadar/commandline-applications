from unittest import TestCase
from .model import start_game, toss, coin_tosser
import json

class TestModel(TestCase):

    def test_start_game_stores_the_selected_coin_in_json_file(self):
        input_coin = True
        start_game(input_coin)
        with open("coin_tosser/coin.json") as f:
            coin = json.load(f)["coin"]
        self.assertEqual(coin, input_coin)

        with open("coin_tosser/user.json") as f:
            user = json.load(f)["user"]
        self.assertEqual(user, 1)

        with open("coin_tosser/results.json") as f:
            results = json.load(f)
        self.assertEqual(results, {})

    def test_coin_tossing_functionality(self):
        coin = toss()
        self.assertIn(coin, [True, False])
        
    def test_coin_tosser_alternates_users(self):

        start_game(True)
        
        result = coin_tosser()
        self.assertEqual(list(result.keys())[0], 1)

        result = coin_tosser()
        self.assertEqual(list(result.keys())[0], 2)

        result = coin_tosser()
        self.assertEqual(list(result.keys())[0], 1)

        result = coin_tosser()
        self.assertEqual(list(result.keys())[0], 2)

        with open("coin_tosser/results.json") as f:
            results = json.load(f)
        print(results)
