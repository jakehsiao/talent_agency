import random

def choose_from_list(choices):
    choices = ["No action"] + choices
    for i, c in enumerate(choices):
        print("{}: {}".format(i, c))
    choice = input("Enter the choice: ")
    if choice.isdigit():
        choice = int(choice)
        if choice != 0 and choice < len(choices):
            return choices[choice]
    return False

def roll_dices(n):
    return sum([random.randint(1, 6) for i in range(int(n))])

def get_sales_volume_multiplier(work, game):
    multiplier = 1
    for market_card in game.working_market_cards:
        if market_card.card_type == "genre":
            if market_card.obj == work.genre:
                multiplier += market_card.value
        elif market_card.card_type == "style":
            if market_card.obj == work.style:
                multiplier += market_card.value

    return multiplier

