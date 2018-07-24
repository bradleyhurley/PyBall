from dataclasses import dataclass, field
from typing import List, Union, Dict, Any

from pyball.models.draft.round import Round


@dataclass
class Draft:
    draftYear: int = None
    rounds: List[Union[Round, Dict[str, Any]]] = field(default_factory=list)

    def __post_init__(self):
        self.rounds = [
            Round(**r)
            for r
            in self.rounds
        ]
