from PyBall.models import BaseModel

from .coordinates import Coordinates


class HitData(BaseModel):
    _fields = {
        'launchSpeed': {'default_value': None, 'field_type': float},
        'launchAngle': {'default_value': None, 'field_type': float},
        'totalDistance': {'default_value': None, 'field_type': float},
        # ToDo - ALl Dater is empty
        'coordinates': {'default_value': {}, 'field_type': dict},
    }
