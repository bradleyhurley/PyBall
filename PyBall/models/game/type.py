from PyBall.models import BaseModel


class Type(BaseModel):
    _fields = {
        'displayName': {'default_value': None, 'field_type': str},
    }
