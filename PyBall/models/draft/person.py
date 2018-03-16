from PyBall.models import BaseModel
from PyBall.models.pitch_hand import PitchHand
from PyBall.models.bat_side import BatSide
from PyBall.models.primary_position import PrimaryPostion


class Person(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': str},
        'fullName': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
        'firstName': {'default_value': None, 'field_type': str},
        'lastName': {'default_value': None, 'field_type': str},
        'birthDate': {'default_value': None, 'field_type': str},
        'birthCountry': {'default_value': None, 'field_type': str},
        'primaryPosition': {'default_value': {}, 'field_type': PrimaryPostion},
        'batSide': {'default_value': {}, 'field_type': BatSide},
        'pitchHand': {'default_value': {}, 'field_type': PitchHand},
        'nameSlug': {'default_value': None, 'field_type': str},
    }
