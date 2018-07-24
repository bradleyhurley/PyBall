from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.draft.home import Home
from pyball.models.draft.school import School
from pyball.models.person import Person
from pyball.models.generic_team import Team


@dataclass
class Pick:
    person: Union[Person, Dict[str, Any]] = field(default_factory=dict)
    bisPlayerId: int = None
    draftPlayerId: int = None
    pickRound: int = None
    pickNumber: int = None
    rank: int = None
    pickedTeamCode: str = None
    home: Union[Home, Dict[str, Any]] = field(default_factory=dict)
    scoutingReport: str = None
    photoFlag: bool = None
    school: Union[School, Dict[str, Any]] = field(default_factory=dict)
    comments: str = None
    blurb: str = None
    headshotLink: str = None
    team: Union[Team, Dict[str, Any]] = field(default_factory=dict)
    isDrafted: bool = None
    isPass: bool = None

    def __post_init__(self):
        self.person = Person(**self.person)
        self.home = Home(**self.home)
        self.school = School(**self.school)
