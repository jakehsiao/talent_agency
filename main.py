from buildings import *
from utils import *
from collections import defaultdict
from market_cards import *

class Game:
    def __init__(self):
        self.buildings = [Bar(), Studio(), RecordStore(self)]
        self.state = "PREPARING"
        self.players = [Player(self) for i in range(1)]
        self.round_num = 0
        self.market_volatility = 1

        self.market_cards = defaultdict(list)
        self.working_market_cards = []

        self.init_buildings()
        self.init_market_cards()

    def init_buildings(self):
        pass

    def init_market_cards(self):
        self.market_cards["public"] += get_market_cards(3)
        for player in self.players:
            amount = 3
            if len(self.players) == 1:
                amount = 3
            elif 4 <= len(self.players) <= 5:
                amount = 2
            elif len(self.players) >= 6:
                amount = 1
            self.market_cards[player] += get_market_cards(amount)

        # for play this on my own
        print("Market cards: ")
        for market_card in self.market_cards[self.players[0]]:
            print(market_card)

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
                self.uncover_market_cards()
            else:
                for building in self.buildings + [player.company for player in self.players]:
                    building.on_operation_phase_finished()
                self.clean_market_cards()
                self.init_market_cards()

    def uncover_market_cards(self):
        for player in self.market_cards:
            if player == "public":
                print("Public:")
            else:
                print(player.name, ":")

            for market_card in self.market_cards[player]:
                work = random.randint(1, 6) >= 3
                if work:
                    print("Work: {}".format(market_card))
                    self.working_market_cards.append(market_card)
                else:
                    print("Not work: {}".format(market_card))
        # TODO: add some summary to the current market

    def clean_market_cards(self):
        self.market_cards = defaultdict(list)
        self.working_market_cards = []



class Player:

    def __init__(self, game, name="Player"):
        self.money = 250000
        self.singers = []
        self.scale = 1
        self.company = Company(self)
        self.game = game
        self.name = name

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
        return "Money: {}, \nSingers: \n{}, \nPopularity: {}, \nScale: {}".format(self.money, self.singers, self.company.popularity, self.scale)


game = Game()

while True:
   game.update()
