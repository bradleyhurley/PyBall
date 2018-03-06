from models.pitch_hand import PitchHand
from models.bat_side import BatSide
from models.primary_position import PrimaryPostion
class People:
    def __init__(self, id=None, fullName=None, link=None, firstName=None, lastName=None, primaryNumber=None,
                 birthDate=None, currentAge=None, birthCity=None, birthStateProvince=None, birthCountry=None,
                 height=None, weight=None, active=None, useName=None, middleName=None, boxscoreName=None, nickName=None,
                 draftYear=None, mlbDebutDate=None, nameFirstLast=None, nameSlug=None, firstLastName=None,
                 lastFirstName=None, lastInitName=None, initLastName=None, fullFMLName=None, fullLFMName=None,
                 pitchHand=None, primaryPosition=None, batSide=None):
        self.id = id
        self.fullName = fullName
        self.link = link
        self.firstName = firstName
        self.lastName = lastName
        self.primaryNumber = primaryNumber
        self.birthDate = birthDate
        self.currentAge = currentAge
        self.birthCity = birthCity
        self.birthStateProvince = birthStateProvince
        self.birthCountry = birthCountry
        self.height = height
        self.weight = weight
        self.active = active
        self.useName = useName
        self.middleName = middleName
        self.boxscoreName = boxscoreName
        self.nickName = nickName
        self.draftYear = draftYear
        self.mlbDebutDate = mlbDebutDate
        self.nameFirstLast = nameFirstLast
        self.nameSlug = nameSlug
        self.firstLastName = firstLastName
        self.lastFirstName = lastFirstName
        self.lastInitName = lastInitName
        self.initLastName = initLastName
        self.fullFMLName = fullFMLName
        self.fullLFMName = fullLFMName
        self.pitchHand = PitchHand(**pitchHand)
        self.primaryPosition = PrimaryPostion(**primaryPosition)
        self.batSide = BatSide(**batSide)
