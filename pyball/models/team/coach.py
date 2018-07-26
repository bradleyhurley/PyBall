from dataclasses import dataclass
from typing import Union, Dict, Any

from .person import Person


@dataclass
class Coach:
    person: Union[Person, Dict[str, Any]] = None
    jerseyNumber: str = None
    job: str = None
    jobId: str = None

    def __post_init__(self):
        self.person = Person(**self.person)
