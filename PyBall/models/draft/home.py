from PyBall.models.base_model import BaseModel


class Home(BaseModel):
    _fields = {
        'city': {'default_value': None, 'field_type': str},
        'state': {'default_value': None, 'field_type': str},
        'country': {'default_value': None, 'field_type': str},
    }
