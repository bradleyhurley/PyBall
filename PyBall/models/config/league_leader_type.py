from PyBall.models import BaseModel
from PyBall.models.config.valid_sport import ValidSport


class LeagueLeaderType(BaseModel):
    _fields = {
        'displayName': {'default_value': None, 'field_type': str},
        'hasMinimums': {'default_value': None, 'field_type': bool},
        'validSports': {'default_value': [], 'field_type': [ValidSport]},
    }
