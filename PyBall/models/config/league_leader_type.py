from PyBall.models.config.valid_sport import ValidSport
from PyBall.models.base_model import BaseModel


class LeagueLeaderType(BaseModel):
    _fields = {
        'displayName': {'default_value': None, 'field_type': str},
        'hasMinimums': {'default_value': None, 'field_type': bool},
        'validSports': {'default_value': [], 'field_type': [ValidSport]},
    }
