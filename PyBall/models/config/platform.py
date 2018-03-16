from PyBall.models import BaseModel


class Platform(BaseModel):
    _fields = {
        'platformCode': {'default_value': None, 'field_type': str},
        'platformDescription': {'default_value': None, 'field_type': str},
    }
