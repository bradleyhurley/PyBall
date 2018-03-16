from PyBall.models import BaseModel


class Position(BaseModel):
    _fields = {
        'shortName': {'default_value': None, 'field_type': str},
        'fullName': {'default_value': None, 'field_type': str},
        'abbrev': {'default_value': None, 'field_type': str},
        'code': {'default_value': None, 'field_type': str},
        'type': {'default_value': None, 'field_type': str},
        'outfield': {'default_value': None, 'field_type': bool},
        'pitcher': {'default_value': None, 'field_type': bool},
        'fielder': {'default_value': None, 'field_type': bool},
        'displayName': {'default_value': None, 'field_type': str},
    }
