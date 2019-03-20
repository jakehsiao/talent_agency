import random

def generate_name():
    surname = "赵 李 王 张 杨 陈 孙 刘 黄 郭 何".split(" ")
    name1 = "大 小 伟 建 志 泽 宇 明 俊 天 昊 浩 明 博 思 心 若 诗 春 秋 雨 子 文 德 家".split(" ")
    name2 = "伟 国 民 昊 浩 轩 宁 航 心 春 秋 杰 俊 文 泽 睿 豪 虎 刚 强 翔 哲".split(" ")
    return random.choice(surname) + random.choice(name1) + random.choice(name2)


class Singer:

    def __init__(self, name="", strength=1, popularity=3):
        self.name = name
        self.strength = strength
        self.popularity = popularity
        self.price = self.strength * random.randint(8, 12) * 1000 + self.popularity * 2000 + int(
            random.normalvariate(0, 1) * 10) * 1000
        self.player = None
        self.album = None
        self.live = None

    def __repr__(self):
        return "Name: {}, Strength: {}, Popularity: {}, Price: {}, \nAlbum: {}, \n".format(self.name, self.strength, self.popularity,
                                                                            self.price, self.album)

def get_random_singer():
    return Singer(name=generate_name(), strength=random.choice([1, 1, 1, 2, 2, 3]),
                  popularity=random.randint(1, 6))
