from dataclasses import dataclass, field
from typing import Union, Dict, Any

from .sport import Sport
from .league import League


@dataclass
class Conference:
    id: int = None
    link: str = None
    name: str = None
    abbreviation: str = None
    hasWildcard: bool = None
    nameShort: str = None
    league: Union[League, Dict[str, Any]] = field(default_factory=dict)
    sport: Union[Sport, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.league = League(**self.league)
        self.sport = Sport(**self.sport)
