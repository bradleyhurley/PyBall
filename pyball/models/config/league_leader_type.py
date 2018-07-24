from dataclasses import dataclass, field
from typing import List

from pyball.models.config.valid_sport import ValidSport


@dataclass
class LeagueLeaderType:
    displayName: str = field(default=None)
    hasMinimums: bool = field(default=None)
    validSports: List[ValidSport] = field(default_factory=List)

    def __post_init__(self):
        if self.validSports and isinstance(self.validSports[0], dict):
            self.validSports = [
                ValidSport(**sport)
                for sport
                in self.validSports
            ]
