from PyBall.models.sport import Sport
from PyBall.models.league import League
from PyBall.models.base_model import BaseModel


class Conference(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'link': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
        'hasWildcard': {'default_value': None, 'field_type': bool},
        'nameShort': {'default_value': {}, 'field_type': str},
        'league': {'default_value': {}, 'field_type': League},
        'sport': {'default_value': None, 'field_type': Sport},
    }
