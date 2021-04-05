from .model import start_game, coin_tosser, show_result

# templates

coins = {
        True: "Head",
        False: "Tail"
    }
users = {
        1:"First User",
        2:"Second User",
        3:"Third User",
        4:"Fourth User",
    }
numbers = {
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
    }

def toss_template(result):
    msg = ""
    for k in result:
        if result[k][0] == 0:
            msg = f"{msg}{users[k]} tossed no {coins[result[k][1]]}\n"
        elif result[k][0] == 1:
            msg = f"{msg}{users[k]} tossed a {coins[result[k][1]]}\n"
        elif result[k][0] > 1:
            msg = f"{msg}{users[k]} tossed {numbers[result[k][0]]} {coins[result[k][1]]}s\n"
        else:
            raise ValueError
    return msg

def winners_template(winners):
    msg = ""
    last_winner = None
    last_before_winner = None

    if len(winners) > 1:
        msg_prefix = "The winners are "
    else:
        msg_prefix = "The winner is "

    if winners:
        last_winner = winners.pop()
    else:
        raise ValueError
    if winners:
        last_before_winner = winners.pop()

    for winner in winners:
        msg = f"{msg}{users[winner]}, "
    if last_before_winner:
        msg = f"{msg}{users[last_before_winner]} and "
    msg = f"{msg}{users[last_winner]}"

    return f"{msg_prefix}{msg}"

# views

def start_view(a):
    coin_str = a["s"].value[0]
    if coin_str == "head":
        coin = True
    elif coin_str == "tail":
        coin = False
    else:
        return "Enter head or tail"

    start_game(coin)
    return "The game begins now!"

def toss_view(a):
    result = coin_tosser()
    if result is not None:
        msg = toss_template(result)
    else:
        result, winners = show_result()
        msg = toss_template(result)
        msg = f"{msg}\n{winners_template(winners)}"
    return msg

def help_view(a):
    pass
