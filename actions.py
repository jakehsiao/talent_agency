import random

class Action:

    def act(self, player):
        raise NotImplementedError

class BuySinger(Action):

    def __init__(self, bar, singer):
        self.bar = bar
        self.singer = singer

    def act(self, player):
        if player.money <= self.singer.price:
            print("Not enough money.")
            return False

        player.money -= self.singer.price
        player.singers.append(self.singer)
        self.bar.refresh_singer()

        print("Singer bought!")

    def __repr__(self):
        return "Buy singer: {}".format(self.singer)