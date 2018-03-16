from PyBall.models import BaseModel


class StandingType(BaseModel):
    _fields = {
        'name': {'default_value': None, 'field_type': str},
        'description': {'default_value': None, 'field_type': str},
    }
