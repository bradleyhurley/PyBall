from pyball.models import BaseModel
from pyball.models.line_score import LineScore


class Teams(BaseModel):
    _fields = {
        'home': {'default_value': {}, 'field_type': LineScore},
        'away': {'default_value': {}, 'field_type': LineScore},
    }
