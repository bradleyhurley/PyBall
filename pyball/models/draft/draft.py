from dataclasses import dataclass, field
from typing import List

from pyball.models.draft.round import Round


@dataclass
class Draft:
    draftYear: int = field(default=None)
    rounds: List[Round] = field(default=None)

    def __post_init__(self):
        if self.rounds and isinstance(self.rounds[0], dict):
            self.rounds = [
                Round(**round)
                for round
                in self.rounds
            ]
