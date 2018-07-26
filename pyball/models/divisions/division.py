from dataclasses import dataclass, field
from typing import Union, Dict, Any

from .league import League
from .sport import Sport


@dataclass
class Division:
    id: int = None
    name: str = None
    nameShort: str = None
    link: str = None
    abbreviation: str = None
    league: Union[League, Dict[str, Any]] = field(default_factory=dict)
    sport: Union[Sport, Dict[str, Any]] = field(default_factory=dict)
    hasWildcard: bool = None

    def __post_init__(self):
        self.league = League(**self.league)
        self.sport = Sport(**self.sport)
