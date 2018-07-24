from dataclasses import dataclass, field

from pyball.models.sport import Sport
from pyball.models.generic_league import League
from pyball.models.venue import Venue
from pyball.models.division import Division


@dataclass
class Team:
    id: int = field(default=None)
    link: str = field(default=None)
    name: str = field(default=None)
    venue: Venue = field(default=None)
    teamCode: str = field(default=None)
    fileCode: str = field(default=None)
    abbreviation: str = field(default=None)
    teamName: str = field(default=None)
    locationName: str = field(default=None)
    firstYearOfPlay: str = field(default=None)
    league: League = field(default=None)
    division: Division = field(default=None)
    sport: Sport = field(default=None)
    shortName: str = field(default=None)
    active: bool = field(default=None)
    parentOrgId: int = field(default=None)
    parentOrgName: str = field(default=None)

    def __post_init__(self):
        if isinstance(self.venue, dict):
            self.venue = Venue(**self.venue)

        if isinstance(self.league, dict):
            self.league = League(**self.league)

        if isinstance(self.division, dict):
            self.division = Division(**self.division)

        if isinstance(self.sport, dict):
            self.sport = Sport(**self.sport)
