from dataclasses import dataclass, field
from typing import List, Union, Dict, Any

from pyball.models.config.valid_sport import ValidSport


@dataclass
class LeagueLeaderType:
    displayName: str = None
    hasMinimums: bool = None
    validSports: List[Union[ValidSport, Dict[str, Any]]] = field(default_factory=list)

    def __post_init__(self):
        self.validSports = [
            ValidSport(**sport)
            for sport
            in self.validSports
        ]
