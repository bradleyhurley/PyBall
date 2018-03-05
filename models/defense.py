from models.pitcher import Pitcher
from models.catcher import Catcher
from models.first import First
from models.second import Second
from models.third import Third
from models.shortstop import Shortstop
from models.left import Left
from models.center import Center
from models.right import Right
from models.team import Team


class Defense:
    def __init__(self, pitcher=None, catcher=None, first=None, second=None, third=None, shortstop=None, left=None,
                 center=None, right=None, team=None):
        self.pitcher = Pitcher(**pitcher)
        self.catcher = Catcher(**catcher)
        self.first = First(**first)
        self.second = Second(**second)
        self.third = Third(**third)
        self.shortstop = Shortstop(**shortstop)
        self.left = Left(**left)
        self.center = Center(**center)
        self.right = Right(**right)
        self.team = Team(**team)
