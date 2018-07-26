from dataclasses import dataclass
from typing import Dict, Any, Union

from pyball.models import Person


@dataclass
class Official:
    officialType: str = None
    official: Union[Person, Dict[str, Any]] = None

    def __post_init__(self):
        self.official = Person(**self.official)
