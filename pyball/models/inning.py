from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.line_score import LineScore


@dataclass
class Inning:
    num: int = None
    ordinalNum: int = None
    home: Union[LineScore, Dict[str, Any]] = field(default_factory=dict)
    away: Union[LineScore, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.home = LineScore(**self.home)
        self.away = LineScore(**self.away)
