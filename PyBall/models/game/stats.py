from PyBall.models import BaseModel
from .stat import Stat


class Stats(BaseModel):
    _fields = {
        'stats': {'default_value': [], 'field_type': Stat},
    }
