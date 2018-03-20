from PyBall.models import BaseModel


class Call(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': str},
        'description': {'default_value': None, 'field_type': str},
    }
