from dataclasses import dataclass, field
from typing import Union, Dict, Any

from .game import Game
from .event import Event


@dataclass
class Schedule:
    date: str = None
    totalItems: int = None
    totalEvents: int = None
    totalGames: int = None
    totalGamesInProgress: int = None
    games: Union[Game, Dict[str, Any]] = field(default_factory=dict)
    events: Union[Event, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.games = [Game(**g) for g in self.games]
        self.events = Event()
