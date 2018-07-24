from dataclasses import dataclass, field
from typing import List, Union, Dict, Any

from pyball.models.draft.pick import Pick


@dataclass
class Round:
    roundNumber: int = None
    round: int = None
    picks: List[Union[Pick, Dict[str, Any]]] = field(default_factory=list)

    def __post_init__(self):
        self.picks = [
            Pick(**pick)
            for pick
            in self.picks
        ]
