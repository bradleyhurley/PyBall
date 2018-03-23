from PyBall.models import BaseModel


class SpringLeague(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'link': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
    }
