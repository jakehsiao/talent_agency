import random
from utils import *
from album import *

# EH: add them to "settings"
PRICE_RECORD_ALBUM = 50000

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
        self.singer.player = player
        self.bar.refresh_singer()

        print("Singer bought!")

    def __repr__(self):
        return "Buy singer: {}".format(self.singer)

class BidSinger(Action):

    def __init__(self, studio, singer):
        self.studio = studio
        self.singer = singer

    def act(self, player):
        if player.money <= self.singer.price:
            print("Not enough money.")
            return False

        player.money -= self.singer.price
        player.singers.append(self.singer)
        self.studio.singers.remove(self.singer)
        self.singer.player = player

        print("Singer bought!")

    def __repr__(self):
        return "Bid singer: {}".format(self.singer)


class RecordAlbum(Action):

    def __repr__(self):
        return "Record the album"

    def act(self, player):
        if player.money < PRICE_RECORD_ALBUM:
            print("Not enough money")
            return False
        singer = choose_from_list(player.singers)  # EH: make this fit AI better
        if singer:
            Album(singer)
            player.money -= PRICE_RECORD_ALBUM

class ProvideRecords(Action):

    def __init__(self, store):
        super(ProvideRecords, self).__init__()
        self.store = store

    def __repr__(self):
        return "Provide records"

    def act(self, player):
        singer = choose_from_list([singer for singer in player.singers if singer.album])
        if not singer:
            return False

        album = singer.album
        amount = input("Enter the amount of records to distribute:")
        if amount.isdigit():
            amount = int(amount)
            if amount * 1000 > player.money:
                print("Not enough money")
                return False
            player.money -= amount * 1000
            self.store.stocks[album] += amount



