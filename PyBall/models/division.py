from PyBall.models import BaseModel


class Division(BaseModel):
        _fields = {
            'id': {'default_value': None, 'field_type': int},
            'name': {'default_value': None, 'field_type': str},
            'link': {'default_value': None, 'field_type': str},
        }
