from singer import *
from actions import *
from collections import defaultdict

class Building:

    def __init__(self):
        self.preparation_actions = []
        self.operation_actions = []
        self.price = 10000
        self.name = ""

    def __repr__(self):
        return self.name

    def on_preparation_round_finished(self):
        pass

    def on_operation_round_finished(self):
        pass

    def on_preparation_phase_finished(self):
        pass

    def on_operation_phase_finished(self):
        pass


class Bar(Building):

    def __init__(self):
        super(Bar, self).__init__()
        self.singer = get_random_singer()
        self.preparation_actions.append(BuySinger(self, self.singer))
        self.name = "Bar"

    def refresh_singer(self):
        self.singer = get_random_singer()
        # Now only the head of the list can be BuySinger, no others
        self.preparation_actions[0] = BuySinger(self, self.singer)

class Company(Building):

    def __init__(self, owner):
        super(Company, self).__init__()
        self.name = "Company"
        self.owner = owner
        self.preparation_actions.append(RecordAlbum())

    def on_preparation_phase_finished(self):
        print("It is operation phase now!")

    def on_operation_phase_finished(self):
        # Clear the albums and lives
        for singer in self.owner.singers:
            singer.album = None
            singer.live = None


class RecordStore(Building):

    def __init__(self):
        super(RecordStore, self).__init__()
        self.name = "RecordStore"
        self.operation_actions.append(ProvideRecords(self))
        self.stocks = defaultdict(int)

    def on_operation_round_finished(self):
        for album in self.stocks:
            # TODO: add promotion stuffs
            sales_volume = album.quality + roll_dices(album.singer.popularity // 5) + roll_dices(album.singer.player.game.market_volatility)
            if sales_volume > self.stocks[album]:
                sales_volume = self.stocks[album]

            self.stocks[album] -= sales_volume
            # TODO: change this into a function
            album.singer.player.money += 2000 * sales_volume

            print("Sold {} records.".format(sales_volume))

    def on_operation_phase_finished(self):
        self.stocks = defaultdict(int)

