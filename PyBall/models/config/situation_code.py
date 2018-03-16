from PyBall.models import BaseModel


class SituationCode(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': str},
        'sortOrder': {'default_value': None, 'field_type': int},
        'navigationMenu': {'default_value': None, 'field_type': str},
        'description': {'default_value': None, 'field_type': str},
        'team': {'default_value': None, 'field_type': bool},
        'batting': {'default_value': None, 'field_type': bool},
        'fielding': {'default_value': None, 'field_type': bool},
    }
