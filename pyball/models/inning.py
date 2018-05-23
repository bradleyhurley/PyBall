from pyball.models import BaseModel
from pyball.models.line_score import LineScore


class Inning(BaseModel):
    _fields = {
        'num': {'default_value': None, 'field_type': int},
        'ordinalNum': {'default_value': None, 'field_type': int},
        'home': {'default_value': {}, 'field_type': LineScore},
        'away': {'default_value': {}, 'field_type': LineScore},
    }
