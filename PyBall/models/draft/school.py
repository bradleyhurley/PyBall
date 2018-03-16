from PyBall.models import BaseModel


class School(BaseModel):
    _fields = {
        'name': {'default_value': None, 'field_type': str},
        'schoolClass': {'default_value': None, 'field_type': str},
        'city': {'default_value': None, 'field_type': str},
        'country': {'default_value': None, 'field_type': str},
        'state': {'default_value': None, 'field_type': str},
    }
