from PyBall.models.base_model import BaseModel


class GameType(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': str},
        'description': {'default_value': None, 'field_type': str},
    }
