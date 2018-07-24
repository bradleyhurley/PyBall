from dataclasses import dataclass, field

from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPosition


@dataclass
class Person:
    id: str = field(default=None)
    fullName: str = field(default=None)
    link: str = field(default=None)
    firstName: str = field(default=None)
    lastName: str = field(default=None)
    birthDate: str = field(default=None)
    birthCountry: str = field(default=None)
    primaryPosition: PrimaryPosition = field(default=None)
    batSide: BatSide = field(default=None)
    pitchHand: PitchHand = field(default=None)
    nameSlug: str = field(default=None)

    def __post_init__(self):
        if isinstance(self.pitchHand, dict):
            self.pitchHand = PitchHand(**self.pitchHand)

        if isinstance(self.primaryPosition, dict):
            self.primaryPosition = PrimaryPosition(**self.primaryPosition)

        if isinstance(self.batSide, dict):
            self.batSide = BatSide(**self.batSide)