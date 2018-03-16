from PyBall.models.league import League
from PyBall.models.sport import Sport
from PyBall.models.base_model import BaseModel


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
