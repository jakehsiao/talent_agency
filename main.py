from buildings import *
from utils import *

class Game:
    def __init__(self):
        self.buildings = [Bar(), RecordStore()]
        self.state = "PREPARING"
        self.players = [Player(self) for i in range(1)]
        self.round_num = 0
        self.market_volatility = 1

        self.init_buildings()

    def init_buildings(self):
        pass

    def get_buildings(self, player):
        return [player.company] + self.buildings

    def update(self):
        self.round_num += 1
        if ((self.round_num - 1) // 6) % 2 == 0:
            self.state = "PREPARING"
        else:
            self.state = "OPERATING"
        print()
        print("Round {}".format(self.round_num))
        print("State: {}".format(self.state))
        for player in self.players:
            player.act()

        if self.state == "PREPARING":
            for building in self.buildings + [player.company for player in self.players]:
                building.on_preparation_round_finished()
        else:
            for building in self.buildings + [player.company for player in self.players]:
                building.on_operation_round_finished()

        if self.round_num % 6 == 0:
            if self.state == "PREPARING":
                for building in self.buildings + [player.company for player in self.players]:
                    building.on_preparation_phase_finished()
            else:
                for building in self.buildings + [player.company for player in self.players]:
                    building.on_operation_phase_finished()



class Player:

    def __init__(self, game):
        self.money = 250000
        self.singers = []
        self.scale = 1
        self.company = Company(self)
        self.game = game

    def act(self):
        for i in range(self.scale):
            print()
            print(self)
            building_of_choice = choose_from_list(self.game.get_buildings(self))
            if building_of_choice:
                if self.game.state == "PREPARING":
                    action_of_choice = choose_from_list((building_of_choice.preparation_actions))
                else:
                    action_of_choice = choose_from_list((building_of_choice.operation_actions))
                if action_of_choice:
                    action_of_choice.act(self)

    def __repr__(self):
        return "Money: {}, \nSingers: \n{}, \nScale: {}".format(self.money, self.singers, self.scale)


game = Game()

while True:
   game.update()
