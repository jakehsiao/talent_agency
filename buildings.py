from singer import *
from actions import *
from utils import *
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
        self.name = "Bar"

    def refresh_singer(self):
        self.singer = get_random_singer()

    @property
    def preparation_actions(self):
        return [BuySinger(self, self.singer)]

    @preparation_actions.setter
    def preparation_actions(self, val):
        # This function is used for super
        pass

    def on_operation_phase_finished(self):
        self.refresh_singer()


class Studio(Building):

    def __init__(self):
        super(Studio, self).__init__()
        self.singers = []
        self.name = "Studio"

        self.refresh_singer()

    def refresh_singer(self):
        self.singers = []
        for i in range(3):
            self.singers.append(get_random_singer())
            self.singers[-1].popularity += 2
        for i in range(3):
            self.singers.append(get_random_singer())
            self.singers[-1].popularity += 5
        for i in range(3):
            self.singers.append(get_random_singer())
            self.singers[-1].popularity += 10

    @property
    def preparation_actions(self):
        return [BidSinger(self, singer) for singer in self.singers]

    @preparation_actions.setter
    def preparation_actions(self, val):
        # For super, too
        pass

    def on_operation_phase_finished(self):
        self.refresh_singer()


class Company(Building):

    def __init__(self, owner):
        super(Company, self).__init__()
        self.name = "Company"
        self.owner = owner
        self.popularity = 0
        self.preparation_actions.append(RecordAlbum())

    def on_preparation_phase_finished(self):
        print("It is operation phase now!")

    def on_operation_phase_finished(self):
        # Clear the albums and lives
        for singer in self.owner.singers:
            singer.album = None
            singer.live = None


class RecordStore(Building):

    def __init__(self, game):
        super(RecordStore, self).__init__()
        self.name = "RecordStore"
        self.game = game
        self.operation_actions.append(ProvideRecords(self))
        self.stocks = defaultdict(int)

    def on_operation_round_finished(self):
        for album in self.stocks:
            # TODO: add promotion stuffs
            sales_volume = album.quality + roll_dices(
                (album.singer.popularity + album.singer.player.company.popularity) // 5) + roll_dices(
                album.singer.player.game.market_volatility)
            print("Origin sales volume: {}".format(sales_volume))
            sales_volume *= get_sales_volume_multiplier(album, self.game)
            if sales_volume > self.stocks[album]:
                sales_volume = self.stocks[album]
            print("Actual sales volume: {}".format(sales_volume))

            self.stocks[album] -= sales_volume
            # TODO: change this into a function to be able to share the revenue
            album.singer.player.money += 2000 * sales_volume
            album.singer.popularity += sales_volume // 10
            album.singer.player.company.popularity += sales_volume // 20

            print("Sold {} records.".format(sales_volume))

    def on_operation_phase_finished(self):
        self.stocks = defaultdict(int)
