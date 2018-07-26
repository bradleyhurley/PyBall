from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.position.position import Center
from pyball.models.position.position import First
from pyball.models.position.position import Left
from pyball.models.position.position import Pitcher
from pyball.models.position.position import Right
from pyball.models.position.position import Second
from pyball.models.position.position import Shortstop
from pyball.models.position.position import Third
from pyball.models.position.position import Catcher

from pyball.models.generic_team import Team


@dataclass
class Defense:
    pitcher: Union[Pitcher, Dict[str, Any]] = field(default_factory=dict)
    catcher: Union[Catcher, Dict[str, Any]] = field(default_factory=dict)
    first: Union[First, Dict[str, Any]] = field(default_factory=dict)
    second: Union[Second, Dict[str, Any]] = field(default_factory=dict)
    third: Union[Third, Dict[str, Any]] = field(default_factory=dict)
    shortstop: Union[Shortstop, Dict[str, Any]] = field(default_factory=dict)
    left: Union[Left, Dict[str, Any]] = field(default_factory=dict)
    center: Union[Center, Dict[str, Any]] = field(default_factory=dict)
    right: Union[Right, Dict[str, Any]] = field(default_factory=dict)
    team: Union[Team, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.pitcher = Pitcher(**self.pitcher)
        self.catcher = Catcher(**self.catcher)
        self.first = First(**self.first)
        self.second = Second(**self.second)
        self.third = Third(**self.third)
        self.shortstop = Shortstop(**self.shortstop)
        self.left = Left(**self.left)
        self.center = Center(**self.center)
        self.right = Right(**self.right)
        self.team = Team(**self.team)
