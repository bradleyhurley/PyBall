from PyBall.models import BaseModel


class StatsGroup(BaseModel):
    _fields = {
        'displayName': {'default_value': None, 'field_type': str},
    }
