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
    return sum([random.randint(1, 6) for i in range(n)])
