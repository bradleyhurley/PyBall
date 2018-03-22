from pyball.models.team import Team
from pyball.models.defense import Defense
from pyball.models.offense import Offense
from pyball.models.innings import Innings


class Game:
    def __init__(self, currentInning=None, currentInningOrdinal=None, inningHalf=None,
                 isTopInning=None, scheduledInnings=None, innings=None, teams=None, defense=None,
                 offense=None, balls=None, strikes=None, outs=None):
        self.currentInning = currentInning
        self.currentInningOrdinal = currentInningOrdinal
        self.inningHalf = inningHalf
        self.isTopInning = isTopInning
        self.scheduledInnings = scheduledInnings
        self.innings = Innings(**innings)
        self.team = Team(**teams)
        self.defense = Defense(**defense)
        self.offense = Offense(**offense)
        self.balls = balls
        self.strikes = strikes
        self.outs = outs
