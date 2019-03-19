from buildings import *

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

class Game:
    def __init__(self):
        self.buildings = [Bar()]

        self.init_buildings()

    def init_buildings(self):
        pass

    def get_buildings(self, player):
        return [player.company] + self.buildings


class Player:

    def __init__(self, game):
        self.money = 250000
        self.singers = []
        self.scale = 1
        self.company = Company()
        self.game = game

    def act(self):
        for i in range(self.scale):
            print()
            print(self)
            building_of_choice = choose_from_list(self.game.get_buildings(self))
            if building_of_choice:
                action_of_choice = choose_from_list((building_of_choice.available_actions))
                if action_of_choice:
                    action_of_choice.act(self)

    def __repr__(self):
        return "Money: {}, \nSingers: \n{}, \nScale: {}".format(self.money, self.singers, self.scale)


game = Game()
players = [Player(game) for i in range(1)]

round_num = 0
while True:
    round_num += 1
    print()
    print("Round {}".format(round_num))
    for player in players:
        player.act()
