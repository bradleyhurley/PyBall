from pyball.models import BaseModel
from pyball.models.pitch_hand import PitchHand
from pyball.models.bat_side import BatSide
from pyball.models.primary_position import PrimaryPosition


class Person(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': str},
        'fullName': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
        'firstName': {'default_value': None, 'field_type': str},
        'lastName': {'default_value': None, 'field_type': str},
        'birthDate': {'default_value': None, 'field_type': str},
        'birthCountry': {'default_value': None, 'field_type': str},
        'primaryPosition': {'default_value': {}, 'field_type': PrimaryPosition},
        'batSide': {'default_value': {}, 'field_type': BatSide},
        'pitchHand': {'default_value': {}, 'field_type': PitchHand},
        'nameSlug': {'default_value': None, 'field_type': str},
    }
