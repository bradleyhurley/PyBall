from PyBall.models.base_model import BaseModel


class PitchHand(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': str},
        'description': {'default_value': None, 'field_type': str},
    }
