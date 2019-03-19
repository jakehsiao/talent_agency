from singer import *
from actions import *

class Building:

    def __init__(self):
        self.available_actions = []
        self.price = 10000
        self.name = ""

    def __repr__(self):
        return self.name

class Bar(Building):

    def __init__(self):
        super(Bar, self).__init__()
        self.singer = get_random_singer()
        self.available_actions.append(BuySinger(self, self.singer))
        self.name = "Bar"

    def refresh_singer(self):
        self.singer = get_random_singer()
        # Now only the head of the list can be BuySinger, no others
        self.available_actions[0] = BuySinger(self, self.singer)

class Company(Building):

    def __init__(self):
        super(Company, self).__init__()
        self.name = "Company"

