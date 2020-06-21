from dataclasses import dataclass, field
from typing import Union, Dict, Any

from .status import Status
from .teams import Teams
from .content import Content
from pyball.models.venue import Venue


@dataclass
class Game:
    gamePk: int = None
    link: str = None
    gameType: str = None
    season: int = None
    gameDate: str = None
    gameNumber: int = None
    publicFacing: bool = None
    doubleHeader: str = None
    gamedayType: str = None
    tiebreaker: str = None
    calendarEventID: str = None
    seasonDisplay: str = None
    dayNight: str = None
    description: str = None
    scheduledInnings: int = None
    gamesInSeries: int = None
    seriesGameNumber: int = None
    seriesDescription: str = None
    recordSource: str = None
    ifNecessary: str = None
    ifNecessaryDescription: str = None
    rescheduledFrom: str = None
    startTimeTBD: str = None
    status: Union[Status, Dict[str, Any]] = field(default_factory=dict)
    teams: Union[Teams, Dict[str, Any]] = field(default_factory=dict)
    venue: Union[Venue, Dict[str, Any]] = field(default_factory=dict)
    content: Union[Content, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.status = Status(**self.status)
        self.teams = Teams(**self.teams)
        self.venue = Venue(**self.venue)
        self.content = Content(**self.content)
