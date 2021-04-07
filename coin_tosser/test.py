from unittest import TestCase
from .model import start_game, toss, coin_tosser, get_result, gameOver, users, empty_result
from .model import compress_result, show_result, get_coin, declare_winner
from .model import coin_json, user_json, result_json
import json

class TestModel(TestCase):

    def test_start_game_stores_the_selected_coin_in_json_file(self):
        input_coin = True
        start_game(input_coin)
        with open(coin_json) as f:
            coin = json.load(f)["coin"]
        self.assertEqual(coin, input_coin)

        with open(user_json) as f:
            user = json.load(f)["user"]
        self.assertEqual(user, 1)

        with open(result_json) as f:
            results = json.load(f)
        self.assertEqual(results, empty_result())

    def test_coin_tossing_functionality(self):
        coin = toss()
        self.assertIn(coin, [True, False])
        
    def test_coin_tosser_alternates_users(self):

        start_game(True)
        
        for user in users:
            result = coin_tosser()
            self.assertEqual(list(result.keys())[0], user)
        for user in users:
            result = coin_tosser()
            self.assertEqual(list(result.keys())[0], user)

        with open(result_json) as f:
            results = json.load(f)

        for user in users:
            self.assertIn(str(user), results)
            self.assertEqual(2, len(results[str(user)]))

    def test_coin_tosser_game_completion(self):

        start_game(True)
        for _ in range(0, (5 * len(users))):
            self.assertEqual(len(coin_tosser()), 1)
        self.assertEqual(coin_tosser(), None)
        result = show_result()[0]
        coin = get_coin()
        self.assertTrue(all(user in result and result[user][1] == coin for user in users))

    def test_get_result(self):
        results = {str(user): [True, False, True] for user in users}
        with open(result_json, "w") as f:
            json.dump(results, f)
        results = get_result()

        for user in users:
            self.assertIn(user, results)

    def test_gameOver(self):
        results = {user: [True, False, True] for user in users}
        self.assertEqual(gameOver(results), False)
        results = {user: [True, False, True, True, False] for user in users}
        self.assertEqual(gameOver(results), True)

    def test_compress_result(self):
        results = {1: [True, True, False]}
        coin = True
        result = compress_result(results, coin)
        self.assertEqual(result[1][0], 2)
        self.assertEqual(result[1][1], coin)

    def test_declare_winner(self):
        results = {
                1: [True, True, False],
                2: [False],
            }
        coin = True
        result = compress_result(results, coin)
        self.assertEqual(declare_winner(result), [1])

        results = {
                1: [True, True, False],
                2: [False],
                3: [True, True],
            }
        coin = True
        result = compress_result(results, coin)
        self.assertEqual(declare_winner(result), [1, 3])

