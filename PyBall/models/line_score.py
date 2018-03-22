from PyBall.models import BaseModel


class LineScore(BaseModel):
    _fields = {
        'runs': {'default_value': None, 'field_type': int},
        'hits': {'default_value': None, 'field_type': int},
        'errors': {'default_value': None, 'field_type': int},
    }
