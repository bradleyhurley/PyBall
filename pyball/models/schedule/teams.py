from dataclasses import dataclass, field
from typing import Union, Dict, Any

from .home import Home
from .away import Away


@dataclass
class Teams:
    away: Union[Away, Dict[str, Any]] = field(default_factory=dict)
    home: Union[Home, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.away = Away(**self.away)
        self.home = Home(**self.home)
