from dataclasses import dataclass, field
from .sport import Sport
from .league import League


@dataclass
class Conference:
    id: int = field(default=None)
    link: str = field(default=None)
    name: str = field(default=None)
    abbreviation: str = field(default=None)
    hasWildcard: bool = field(default=None)
    nameShort: str = field(default=None)
    league: League = field(default=None)
    sport: Sport = field(default=None)

    def __post_init__(self):
        if isinstance(self.league, dict):
            self.league = League(**self.league)

        if isinstance(self.sport, dict):
            self.sport = Sport(**self.sport)
