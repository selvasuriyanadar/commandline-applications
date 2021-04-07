import json
from json import JSONDecodeError
import random
from importlib import resources

user1 = 1
user2 = 2
user3 = 3
user4 = 4
users = [user1, user2, user3, user4]

# data access

def start_game(coin):
    coin_store(coin)
    user_store(users[0])
    reset_result()

# logic and data access

def coin_tosser():
    results = get_result()
    if not gameOver(results):
        user = get_user()
        coin = toss()
        result_store(user, coin)

        results = get_result()
        if not gameOver(results):
            user_store(rotateUser(user))

        result = {user: [1, coin]}

    else:
        result = None

    return result

def show_result():
    results = get_result()
    result = compress_result(results, get_coin())
    return result, declare_winner(result)

# logic and string access


# logic

def declare_winner(result):
    max_count = 0
    for user in result:
        if result[user][0] > max_count:
            max_count = result[user][0]
    return [user for user in result if result[user][0] == max_count]

def compress_result(results, coin):
    fresult = {}
    for user in results:
        coins = [r for r in results[user] if r == coin]
        fresult[user] = [len(coins), coin]
    return fresult

def toss():
    return bool(random.getrandbits(1))

def rotateUser(user):
    i = users.index(user)
    if i >= 0 and i <= len(users)-2:
        result = users[i+1]
    elif i == len(users)-1:
        result = users[0]
    else:
        raise IndexError

    return result

def gameOver(results):
    return all(len(results[user]) == 5 for user in users)

# data

with resources.path(
        "coin_tosser.data",
        "coin.json"
    ) as path:
    coin_json = path

def coin_store(coin):
    with open(coin_json, "w") as f:
        json.dump({"coin": coin}, f)

def get_coin():
    with open(coin_json) as f:
        return json.load(f)["coin"]

with resources.path(
        "coin_tosser.data",
        "user.json"
    ) as path:
    user_json = path

def user_store(user):
    with open(user_json, "w") as f:
        json.dump({"user": user}, f)

def get_user():
    with open(user_json) as f:
        return json.load(f)["user"]

with resources.path(
        "coin_tosser.data",
        "results.json"
    ) as path:
    result_json = path

def result_store(user, result):
    try:
        with open(result_json) as f:
            results = json.load(f)
    except (JSONDecodeError) as e:
        results = empty_result()

    if str(user) in results:
        results[str(user)].append(result)
    else:
        raise KeyError

    with open(result_json, "w") as f:
        json.dump(results, f)

def get_result():
    with open(result_json) as f:
        results = json.load(f)
        for k in list(results.keys()):
            results[int(k)] = results.pop(k)
        return results

def reset_result():
    with open(result_json, "w") as f:
        json.dump(empty_result(), f)

def empty_result():
    return {str(user): [] for user in users}

