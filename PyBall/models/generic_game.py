from PyBall.models import BaseModel
from PyBall.models.team import Team
from PyBall.models.defense import Defense
from PyBall.models.offense import Offense
from PyBall.models.innings import Innings


class Game(BaseModel):
    _fields = {
        'currentInning': {'default_value': None, 'field_type': int},
        'currentInningOrdinal': {'default_value': None, 'field_type': int},
        'inningHalf': {'default_value': None, 'field_type': str},
        'isTopInning': {'default_value': None, 'field_type': bool},
        'scheduledInnings': {'default_value': None, 'field_type': str},
        'innings': {'default_value': {}, 'field_type': Innings},
        'team': {'default_value': {}, 'field_type': Team},
        'defense': {'default_value': {}, 'field_type': Defense},
        'offense': {'default_value': {}, 'field_type': Offense},
        'balls': {'default_value': None, 'field_type': int},
        'strikes': {'default_value': None, 'field_type': int},
        'outs': {'default_value': None, 'field_type': int},
    }
