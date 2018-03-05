from models.batter import Batter
from models.on_deck import OnDeck
from models.in_hole import InHole
from models.pitcher import Pitcher
from models.team import Team


class Offense:
    def __init__(self, batter=None, onDeck=None, inHole=None, pitcher=None, team=None):
        self.batter = Batter(**batter)
        self.onDeck = OnDeck(**onDeck)
        self.inHole = InHole(**inHole)
        self.pitcher = Pitcher(**pitcher)
        self.team = Team(**team)
