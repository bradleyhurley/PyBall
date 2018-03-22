from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPostion


class Person:
    def __init__(self, id=None, fullName=None, link=None, firstName=None, lastName=None,
                 birthDate=None, birthCountry=None, primaryPosition=None, batSide=None,
                 pitchHand=None, nameSlug=None):
        self.id = id
        self.fullName = fullName
        self.link = link
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.birthCountry = birthCountry
        self.primaryPosition = PrimaryPostion(**primaryPosition)
        self.batSide = BatSide(**batSide)
        self.pitchHand = PitchHand(**pitchHand)
        self.nameSlug = nameSlug
