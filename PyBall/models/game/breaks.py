from PyBall.models import BaseModel


class Break(BaseModel):
    _fields = {
        'breakAngle': {'default_value': None, 'field_type': float},
        'breakLength': {'default_value': None, 'field_type': float},
        'breakY': {'default_value': None, 'field_type': float},
    }