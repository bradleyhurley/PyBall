from PyBall.models import BaseModel


class Result(BaseModel):
    _fields = {
        'type': {'default_value': None, 'field_type': str},
        'event': {'default_value': None, 'field_type': str},
        'description': {'default_value': None, 'field_type': str},
        'rbi': {'default_value': None, 'field_type': int},
    }
