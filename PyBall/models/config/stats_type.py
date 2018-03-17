from PyBall.models import BaseModel


class StatsType(BaseModel):
    _fields = {
        'displayName': {'default_value': None, 'field_type': str},
    }
