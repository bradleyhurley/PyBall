from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.inning import Inning


@dataclass
class Innings:
    inning: Union[Inning, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.inning = Inning(**self.inning)
