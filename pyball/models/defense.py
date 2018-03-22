from pyball.models.position.position import Center
from pyball.models.position.position import First
from pyball.models.position.position import Left
from pyball.models.position.position import Pitcher
from pyball.models.position.position import Right
from pyball.models.position.position import Second
from pyball.models.position.position import Shortstop
from pyball.models.position.position import Third
from pyball.models.position.position import Catcher

from pyball.models.team import Team


class Defense:
    def __init__(self, pitcher=None, catcher=None, first=None, second=None, third=None,
                 shortstop=None, left=None, center=None, right=None, team=None):
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
