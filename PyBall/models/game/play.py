from PyBall.models import BaseModel

from .result import Result
from .count import Count
from .about import About
from .play_event import PlayEvent


class Play(BaseModel):
    _fields = {
        'result': {'default_value': {}, 'field_type': Result},
        'count': {'default_value': {}, 'field_type': Count},
        'about': {'default_value': {}, 'field_type': About},
        'pitchIndex': {'default_value': [], 'field_type': list},
        'actionIndex': {'default_value': [], 'field_type': list},
        'runnerIndex': {'default_value': [], 'field_type': list},
        'runners': {'default_value': [], 'field_type': list},
        'playEvents': {'default_value': [], 'field_type': [PlayEvent]},
        'index': {'default_value': None, 'field_type': int},
        'pfxId': {'default_value': None, 'field_type': str},
        'playId': {'default_value': None, 'field_type': str},
        'pitchNumber': {'default_value': None, 'field_type': int},
        'startTime': {'default_value': None, 'field_type': str},
        'endTime': {'default_value': None, 'field_type': str},
        'isPitch': {'default_value': None, 'field_type': bool},
        'type': {'default_value': None, 'field_type': str},
    }