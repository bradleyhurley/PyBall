from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPosition


@dataclass
class Person:
    id: int = None
    fullName: str = None
    link: str = None
    firstName: str = None
    lastName: str = None
    primaryNumber: str = None
    birthDate: str = None
    currentAge: int = None
    birthCity: str = None
    birthStateProvince: str = None
    height: str = None
    weight: int = None
    active: bool = None
    useName: str = None
    middleName: str = None
    boxscoreName: str = None
    nickName: str = None
    draftYear: int = None
    mlbDebutDate: str = None
    nameFirstLast: str = None
    nameSlug: str = None
    firstLastName: str = None
    lastFirstName: str = None
    lastInitName: str = None
    initLastName: str = None
    fullFMLName: str = None
    fullLFMName: str = None
    pitchHand: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    primaryPosition: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    batSide: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    birthCountry: str = None
    pronunciation: str = None
    strikeZoneTop: float = None
    strikeZoneBottom: float = None

    def __post_init__(self):
        self.pitchHand = PitchHand(**self.pitchHand)
        self.primaryPosition = PrimaryPosition(**self.primaryPosition)
        self.batSide = BatSide(**self.batSide)
