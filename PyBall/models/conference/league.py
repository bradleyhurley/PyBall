from PyBall.models.base_model import BaseModel


class League(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'link': {'default_value': None, 'field_type': str},
    }
