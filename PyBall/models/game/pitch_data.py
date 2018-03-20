from PyBall.models import BaseModel

from .coordinates import Coordinates
from .breaks import Break


class PitchData(BaseModel):
    _fields = {
        'startSpeed': {'default_value': None, 'field_type': float},
        'endSpeed': {'default_value': None, 'field_type': float},
        'nastyFactor': {'default_value': None, 'field_type': float},
        'strikeZoneTop': {'default_value': None, 'field_type': float},
        'strikeZoneBottom': {'default_value': None, 'field_type': float},
        'coordinates': {'default_value': {}, 'field_type': Coordinates},
        'breaks': {'default_value': {}, 'field_type': Break},
    }
