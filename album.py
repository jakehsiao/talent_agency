import random
from utils import *

class Album:

    def __init__(self, singer):
        self.singer = singer
        self.quality = roll_dices(self.singer.strength)
        singer.album = self
        print("Get new album!")
        print(self)

    def __repr__(self):
        return "Quality: {}".format(self.quality)
