from PyBall.models import BaseModel

from .count import Count
from .detail import Detail
from .type import Type
from .pitch_data import PitchData


class PlayEvent(BaseModel):
    _fields = {
        'details': {'default_value': {}, 'field_type': Detail},
        'count': {'default_value': {}, 'field_type': Count},
        'code': {'default_value': None, 'field_type': str},
        'ballColor': {'default_value': None, 'field_type': str},
        'trailColor': {'default_value': None, 'field_type': str},
        'isInPlay': {'default_value': None, 'field_type': bool},
        'isStrike': {'default_value': None, 'field_type': bool},
        'isBall': {'default_value': None, 'field_type': bool},
        'type': {'default_value': {}, 'field_type': Type},
        'hasReview': {'default_value': None, 'field_type': bool},
        'pitchData': {'default_value': {}, 'field_type': PitchData},

    }