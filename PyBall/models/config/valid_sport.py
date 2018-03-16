from PyBall.models.base_model import BaseModel


class ValidSport(BaseModel):
    _fields = {
        'name': {'default_value': None, 'field_type': str},
        'explictModeOn': {'default_value': None, 'field_type': bool},
    }
