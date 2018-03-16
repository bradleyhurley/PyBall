from PyBall.models import BaseModel


class RosterType(BaseModel):
    _fields = {
        'description': {'default_value': None, 'field_type': str},
        'lookupName': {'default_value': None, 'field_type': str},
        'parameter': {'default_value': None, 'field_type': str},
    }
