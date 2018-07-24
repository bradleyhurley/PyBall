from dataclasses import dataclass

from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPosition


@dataclass
class Person:
    id: int
    fullName: str
    link: str
    firstName: str
    lastName: str
    primaryNumber: str
    birthDate: str
    currentAge: int
    birthCity: str
    birthStateProvince: str
    height: str
    weight: int
    active: bool
    useName: str
    middleName: str
    boxscoreName: str
    nickName: str
    draftYear: int
    mlbDebutDate: str
    nameFirstLast: str
    nameSlug: str
    firstLastName: str
    lastFirstName: str
    lastInitName: str
    initLastName: str
    fullFMLName: str
    fullLFMName: str
    pitchHand: PitchHand
    primaryPosition: PrimaryPosition
    batSide: BatSide
    birthCountry: str
    pronunciation: str
    strikeZoneTop: float
    strikeZoneBottom: float

    def __post_init__(self):
        if isinstance(self.pitchHand, dict):
            self.pitchHand = PitchHand(**self.pitchHand)

        if isinstance(self.primaryPosition, dict):
            self.primaryPosition = PrimaryPosition(**self.primaryPosition)

        if isinstance(self.batSide, dict):
            self.batSide = BatSide(**self.batSide)
