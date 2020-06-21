from dataclasses import dataclass, field
from typing import Union, Dict, Any

from .league_record import LeagueRecord
from .team import Team


@dataclass
class Away:
    splitSquad: bool = None
    seriesNumber: int = None
    leagueRecord: Union[LeagueRecord, Dict[str, Any]] = field(default_factory=dict)
    team: Union[Team, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.leagueRecord = LeagueRecord(**self.leagueRecord)
        self.team = Team(**self.team)
