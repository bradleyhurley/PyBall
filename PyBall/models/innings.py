from models.inning import Inning


class Innings:
    def __init__(self, inning=None):
        self.inning = Inning(**inning)
