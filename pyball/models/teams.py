from pyball.models.away import Away
from pyball.models.home import Home


class Teams:
    def __init__(self, home=None, away=None):
        self.home = Home(**home)
        self.away = Away(**away)
