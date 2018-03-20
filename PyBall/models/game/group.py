from PyBall.models import BaseModel


class Group(BaseModel):
    _fields = {
        'displayName': {'default_value': None, 'field_type': str},
    }
