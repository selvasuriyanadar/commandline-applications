import json
from json import JSONDecodeError
import random

user1 = 1
user2 = 2
users = [user1, user2]

def start_game(coin):
    with open("coin_tosser/coin.json", "w") as f:
        json.dump({"coin": coin}, f)
    user_store(user1)
    reset_result()

def coin_tosser():
    with open("coin_tosser/user.json") as f:
        user = json.load(f)["user"]
    result = toss()
    result_store(user, result)
    result = {user: result}

    user = rotateUser(user)
    user_store(user)
    return result

# logic

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
    

# data

def user_store(user):
    with open("coin_tosser/user.json", "w") as f:
        json.dump({"user": user}, f)

def result_store(user, result):
    try:
        with open("coin_tosser/results.json") as f:
            results = json.load(f)
    except (JSONDecodeError) as e:
        results = {}

    if str(user) in results:
        results[str(user)].append(result)
    else:
        results[str(user)] = [result]

    with open("coin_tosser/results.json", "w") as f:
        json.dump(results, f)

def reset_result():
    with open("coin_tosser/results.json", "w") as f:
        json.dump({}, f)
