from pyball.models.position.position import Batter
from pyball.models.position.position import InHole
from pyball.models.position.position import OnDeck
from pyball.models.position.position import Pitcher
from pyball.models.team import Team


class Offense:
    def __init__(self, batter=None, onDeck=None, inHole=None, pitcher=None, team=None):
        self.batter = Batter(**batter)
        self.onDeck = OnDeck(**onDeck)
        self.inHole = InHole(**inHole)
        self.pitcher = Pitcher(**pitcher)
        self.team = Team(**team)
