from dataclasses import dataclass, field
from typing import Dict, Any, Union

from pyball.models.sport import Sport
from pyball.models.generic_league import League
from pyball.models.venue import Venue
from pyball.models.division import Division


@dataclass
class Team:
    id: int = None
    link: str = None
    name: str = None
    venue: Union[Venue, Dict[str, Any]] = field(default_factory=dict)
    teamCode: str = None
    fileCode: str = None
    abbreviation: str = None
    teamName: str = None
    locationName: str = None
    firstYearOfPlay: str = None
    league: Union[League, Dict[str, Any]] = field(default_factory=dict)
    division: Union[Division, Dict[str, Any]] = field(default_factory=dict)
    sport: Union[Sport, Dict[str, Any]] = field(default_factory=dict)
    shortName: str = None
    active: bool = None
    parentOrgId: int = None
    parentOrgName: str = None
    allStarStatus: str = None
    springLeague: Union[League, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.venue = Venue(**self.venue)
        self.league = League(**self.league)
        self.division = Division(**self.division)
        self.sport = Sport(**self.sport)
        self.springLeague = League(**self.springLeague)
