from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.generic_team import Team
from pyball.models.defense import Defense
from pyball.models.offense import Offense
from pyball.models.innings import Innings


@dataclass
class Game:
    currentInning: int = None
    currentInningOrdinal: int = None
    inningHalf: str = None
    isTopInning: bool = None
    scheduledInnings: str = None
    innings:  Union[Innings, Dict[str, Any]] = field(default_factory=dict)
    team:  Union[Team, Dict[str, Any]] = field(default_factory=dict)
    defense:  Union[Defense, Dict[str, Any]] = field(default_factory=dict)
    offense:  Union[Offense, Dict[str, Any]] = field(default_factory=dict)
    balls: int = None
    strikes: int = None
    outs: int = None

    def __post_init__(self):
        self.innings = Innings(**self.innings)
        self.team = Team(**self.team)
        self.defense = Defense(**self.defense)
        self.offense = Offense(**self.offense)
