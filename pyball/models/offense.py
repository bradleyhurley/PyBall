from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.position.position import Batter
from pyball.models.position.position import InHole
from pyball.models.position.position import OnDeck
from pyball.models.position.position import Pitcher
from pyball.models.generic_team import Team


@dataclass
class Offense:
    batter: Union[Batter, Dict[str, Any]] = field(default_factory=dict)
    onDeck: Union[OnDeck, Dict[str, Any]] = field(default_factory=dict)
    inHole: Union[InHole, Dict[str, Any]] = field(default_factory=dict)
    pitcher: Union[Pitcher, Dict[str, Any]] = field(default_factory=dict)
    team: Union[Team, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.batter = Batter(**self.batter)
        self.onDeck = OnDeck(**self.onDeck)
        self.inHole = InHole(**self.inHole)
        self.pitcher = Pitcher(**self.pitcher)
        self.team = Team(**self.team)
