from dataclasses import dataclass, field
from typing import Union, Dict, Any

from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPosition


@dataclass
class Person:
    id: str = None
    fullName: str = None
    link: str = None
    firstName: str = None
    lastName: str = None
    birthDate: str = None
    birthCountry: str = None
    pitchHand: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    primaryPosition: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    batSide: Union[PitchHand, Dict[str, Any]] = field(default_factory=dict)
    nameSlug: str = None

    def __post_init__(self):
        self.pitchHand = PitchHand(**self.pitchHand)
        self.primaryPosition = PrimaryPosition(**self.primaryPosition)
        self.batSide = BatSide(**self.batSide)