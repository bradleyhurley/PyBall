from PyBall.models import BaseModel


class Count(BaseModel):
    _fields = {
        'balls': {'default_value': None, 'field_type': int},
        'strikes': {'default_value': None, 'field_type': int},
        'outs': {'default_value': None, 'field_type': int},
    }
