from PyBall.models.base_model import BaseModel


class PrimaryPostion(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
        'type': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
    }
