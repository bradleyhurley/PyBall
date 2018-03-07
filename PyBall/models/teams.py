from PyBall.models.away import Away
from PyBall.models.home import Home


class Teams:
    def __init__(self, home=None, away=None):
        self.home = Home(**home)
        self.away = Away(**away)
