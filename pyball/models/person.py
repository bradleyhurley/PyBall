from dataclasses import dataclass, field

from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPosition


@dataclass
class Person:
    id: int = field(default=None)
    fullName: str = field(default=None)
    link: str = field(default=None)
    firstName: str = field(default=None)
    lastName: str = field(default=None)
    primaryNumber: str = field(default=None)
    birthDate: str = field(default=None)
    currentAge: int = field(default=None)
    birthCity: str = field(default=None)
    birthStateProvince: str = field(default=None)
    height: str = field(default=None)
    weight: int = field(default=None)
    active: bool = field(default=None)
    useName: str = field(default=None)
    middleName: str = field(default=None)
    boxscoreName: str = field(default=None)
    nickName: str = field(default=None)
    draftYear: int = field(default=None)
    mlbDebutDate: str = field(default=None)
    nameFirstLast: str = field(default=None)
    nameSlug: str = field(default=None)
    firstLastName: str = field(default=None)
    lastFirstName: str = field(default=None)
    lastInitName: str = field(default=None)
    initLastName: str = field(default=None)
    fullFMLName: str = field(default=None)
    fullLFMName: str = field(default=None)
    pitchHand: PitchHand = field(default=None)
    primaryPosition: PrimaryPosition = field(default=None)
    batSide: BatSide = field(default=None)
    birthCountry: str = field(default=None)
    pronunciation: str = field(default=None)
    strikeZoneTop: float = field(default=None)
    strikeZoneBottom: float = field(default=None)

    def __post_init__(self):
        if isinstance(self.pitchHand, dict):
            self.pitchHand = PitchHand(**self.pitchHand)

        if isinstance(self.primaryPosition, dict):
            self.primaryPosition = PrimaryPosition(**self.primaryPosition)

        if isinstance(self.batSide, dict):
            self.batSide = BatSide(**self.batSide)
