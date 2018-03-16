from PyBall.models.base_model import BaseModel
from .league import League
from .sport import Sport


class Division(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'name': {'default_value': None, 'field_type': str},
        'nameShort': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
        'league': {'default_value': {}, 'field_type': League},
        'sport': {'default_value': {}, 'field_type': Sport},
        'hasWildcard': {'default_value': None, 'field_type': bool},
    }
