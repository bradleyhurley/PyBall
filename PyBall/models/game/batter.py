from PyBall.models import BaseModel


class Batter(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'fullName': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
    }
