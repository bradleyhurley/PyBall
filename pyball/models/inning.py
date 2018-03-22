from pyball.models.away import Away
from pyball.models.home import Home


class Inning:
    def __init__(self, num=None, ordinalNum=None, home=None, away=None):
        self.num = num
        self.ordinalNum = ordinalNum
        self.home = Home(**home)
        self.away = Away(**away)
