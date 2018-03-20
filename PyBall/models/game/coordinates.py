from PyBall.models import BaseModel


class Coordinates(BaseModel):
    _fields = {
        'aY': {'default_value': None, 'field_type': float},
        'aZ': {'default_value': None, 'field_type': float},
        'pfxX': {'default_value': None, 'field_type': float},
        'pfxZ': {'default_value': None, 'field_type': float},
        'pX': {'default_value': None, 'field_type': float},
        'pZ': {'default_value': None, 'field_type': float},
        'vX0': {'default_value': None, 'field_type': float},
        'vY0': {'default_value': None, 'field_type': float},
        'vZ0': {'default_value': None, 'field_type': float},
        'x': {'default_value': None, 'field_type': float},
        'y': {'default_value': None, 'field_type': float},
        'x0': {'default_value': None, 'field_type': float},
        'y0': {'default_value': None, 'field_type': float},
        'z0': {'default_value': None, 'field_type': float},
        'aX': {'default_value': None, 'field_type': float},
    }
