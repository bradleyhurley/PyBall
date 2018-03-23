from PyBall.models.base_model import BaseModel
from PyBall.models.pitch_hand import PitchHand
from PyBall.models.bat_side import BatSide
from PyBall.models.primary_position import PrimaryPostion


class Person(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'fullName': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
        'firstName': {'default_value': None, 'field_type': str},
        'lastName': {'default_value': None, 'field_type': str},
        'primaryNumber': {'default_value': None, 'field_type': str},
        'birthDate': {'default_value': None, 'field_type': str},
        'currentAge': {'default_value': None, 'field_type': int},
        'birthCity': {'default_value': None, 'field_type': str},
        'birthStateProvince': {'default_value': None, 'field_type': str},
        'height': {'default_value': None, 'field_type': str},
        'weight': {'default_value': None, 'field_type': int},
        'active': {'default_value': None, 'field_type': bool},
        'useName': {'default_value': None, 'field_type': str},
        'middleName': {'default_value': None, 'field_type': str},
        'boxscoreName': {'default_value': None, 'field_type': str},
        'nickName': {'default_value': None, 'field_type': str},
        'draftYear': {'default_value': None, 'field_type': int},
        'mlbDebutDate': {'default_value': None, 'field_type': str},
        'nameFirstLast': {'default_value': None, 'field_type': str},
        'nameSlug': {'default_value': None, 'field_type': str},
        'firstLastName': {'default_value': None, 'field_type': str},
        'lastFirstName': {'default_value': None, 'field_type': str},
        'lastInitName': {'default_value': None, 'field_type': str},
        'initLastName': {'default_value': None, 'field_type': str},
        'fullFMLName': {'default_value': None, 'field_type': str},
        'fullLFMName': {'default_value': None, 'field_type': str},
        'pitchHand': {'default_value': {}, 'field_type': PitchHand},
        'primaryPosition': {'default_value': {}, 'field_type': PrimaryPostion},
        'batSide': {'default_value': {}, 'field_type': BatSide},
    }
