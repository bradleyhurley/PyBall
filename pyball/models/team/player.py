from dataclasses import dataclass
from typing import Union, Dict, Any

from .person import Person
from .status import Status


@dataclass
class Player:
    person: Union[Person, Dict[str, Any]] = None
    jerseyNumber: str = None
    status: Union[Status, Dict[str, Any]] = None
    parentTeamId: int = None
    position: str = None

    def __post_init__(self):
        self.person = Person(**self.person)
        self.status = Status(**self.status)
