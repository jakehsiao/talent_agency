import random

def get_market_cards(n):
    market_cards = []
    for i in range(n):
        market_cards.append(get_random_market_card())
    return market_cards

def get_random_market_card():
    card_type = random.choice(["genre", "style"])
    obj = ""
    if card_type == "genre":
        obj = random.choice(["Rock", "Country", "Jazz", "EDM", "R&B", "HipHop"])
    elif card_type == "style":
        obj = random.choice(["fresh", "manic", "powerful", "lyric"])
    value = 0.5
    if random.random() <= 0.3:
        value = -0.5
    return MarketCard(card_type, obj, value)



class MarketCard:

    def __init__(self, card_type="genre", obj="rock", value=0.5):
        ## type: genre, style, form, volatility, building(in the future)
        self.card_type = card_type
        self.obj = obj
        self.value = value

    def __repr__(self):
        return "{} {} will {} {}".format(self.obj, self.card_type, "improve" if self.value >= 0 else "decline", abs(self.value))

    def on_effect(self):
        # TODO: implement this for popularity market cards and building market cards
        pass
