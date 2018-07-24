from dataclasses import dataclass, field

from pyball.models.draft.home import Home
from pyball.models.draft.school import School
from pyball.models.draft.person import Person


@dataclass
class Pick:
    person: Person = field(default=None)
    bisPlayerId: int = field(default=None)
    draftPlayerId: int = field(default=None)
    pickRound: int = field(default=None)
    pickNumber: int = field(default=None)
    rank: int = field(default=None)
    pickedTeamCode: str = field(default=None)
    home: Home = field(default=None)
    scoutingReport: str = field(default=None)
    photoFlag: bool = field(default=None)
    school: School = field(default=None)
    comments: str = field(default=None)

    def __post_init__(self):
        if isinstance(self.person, dict):
            self.person = Person(**self.person)

        if isinstance(self.home, dict):
            self.home = Home(**self.home)

        if isinstance(self.school, dict):
            self.school = School(**self.school)
