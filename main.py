import random

def choose_from_list(choices):
    choices = ["No action"] + choices
    for i, c in enumerate(choices):
        print("{}: {}".format(i, c))
    choice = input("Enter the choice: ")
    if choice.isdigit():
        choice = int(choice)
        if choice != 0 and choice < len(choices):
            return choices[choice]
    return False

def generate_name():
    surname = "赵 李 王 张 杨 陈 孙 刘 黄 郭 何".split(" ")
    name1 = "大 小 伟 建 志 泽 宇 明 俊 天 昊 浩 明 博 思 心 若 诗 春 秋 雨 子 文 德 家".split(" ")
    name2 = "伟 国 民 昊 浩 轩 宁 航 心 春 秋 杰 俊 文 泽 睿 豪 虎 刚 强 翔 哲".split(" ")
    return random.choice(surname)+random.choice(name1)+random.choice(name2)


class Singer:

    def __init__(self, name="", strength=1, popularity=3):
        self.name = name
        self.strength = strength
        self.popularity = popularity
        self.price = self.strength * random.randint(8, 12) * 1000 + self.popularity * 2000 + int(random.normalvariate(0, 1) * 10) * 1000

    def __repr__(self):
        return "Name: {}, Strength: {}, Popularity: {}, Price: {}\n".format(self.name, self.strength, self.popularity, self.price)

def get_random_singer():
    return Singer(name=generate_name(), strength=random.choice([1, 1, 1, 2, 2, 3]), popularity=random.choice(range(1, 7)))


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


class Game:
    def __init__(self):
        self.buildings = [Bar()]

        self.init_buildings()

    def init_buildings(self):
        pass

    def get_buildings(self, player):
        return [player.company] + self.buildings


class Player:

    def __init__(self, game):
        self.money = 250000
        self.singers = []
        self.scale = 1
        self.company = Company()
        self.game = game

    def act(self):
        for i in range(self.scale):
            print()
            print(self)
            building_of_choice = choose_from_list(self.game.get_buildings(self))
            if building_of_choice:
                action_of_choice = choose_from_list((building_of_choice.available_actions))
                if action_of_choice:
                    action_of_choice.act(self)

    def __repr__(self):
        return "Money: {}, \nSingers: \n{}, \nScale: {}".format(self.money, self.singers, self.scale)

game = Game()
players = [Player(game) for i in range(1)]

round = 0
while True:
    round += 1
    print()
    print("Round {}".format(round))
    for player in players:
        player.act()
