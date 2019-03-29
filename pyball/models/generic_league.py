from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.league import SeasonDate
from pyball.models.sport import Sport


@dataclass
class League:
    id: int = None
    name: str = None
    link: str = None
    abbreviation: str = None
    seasonState: str = None
    hasWildCard: bool = None
    hasSplitSeason: bool = None
    hasPlayoffPoints: bool = None
    numTeams: int = None
    seasonDateInfo: Union[SeasonDate, Dict[str, Any]] = field(default_factory=dict)
    orgCode: str = None
    conferencesInUse: bool = None
    divisionsInUse: bool = None
    sport: Union[Sport, Dict[str, Any]] = field(default_factory=dict)
    sortOrder: int = None

    def __post_init__(self):
        self.seasonDateInfo = SeasonDate(**self.seasonDateInfo)
        self.sport = Sport(**self.sport)
