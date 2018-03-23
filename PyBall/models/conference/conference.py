from PyBall.models.base_model import BaseModel
from .sport import Sport
from .league import League


class Conference(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'link': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
        'hasWildcard': {'default_value': None, 'field_type': bool},
        'nameShort': {'default_value': None, 'field_type': str},
        'league': {'default_value': {}, 'field_type': League},
        'sport': {'default_value': {}, 'field_type': Sport},
    }
