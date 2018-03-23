from PyBall.models.base_model import BaseModel


class BatSide(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': int},
        'description': {'default_value': None, 'field_type': str},
    }
