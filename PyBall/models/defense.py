from models.position.position import Center
from models.position.position import First
from models.position.position import Left
from models.position.position import Pitcher
from models.position.position import Right
from models.position.position import Second
from models.position.position import Shortstop
from models.position.position import Third
from models.position.position import Catcher

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
