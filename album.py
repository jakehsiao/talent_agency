import random
from utils import *

# EH: change this to "Work" in order to remove redundant code of album and live
class Album:

    def __init__(self, singer):
        self.singer = singer
        self.quality = roll_dices(self.singer.strength)
        self.genre = singer.genre
        self.style = singer.style  # EH: can choose genre and style when singer knows plenty
        singer.album = self
        print("Get new album!")
        print(self)

    def __repr__(self):
        return "Quality: {}, Genre: {}, Style: {}".format(self.quality, self.genre, self.style)
