from dataclasses import dataclass, field
from typing import List

from pyball.models.draft.pick import Pick


@dataclass
class Round:
    roundNumber: int = field(default=None)
    picks: List[Pick] = field(default=None)

    def __post_init__(self):
        if self.picks and isinstance(self.picks[0], dict):
            self.picks = [
                Pick(**pick)
                for pick
                in self.picks
            ]
