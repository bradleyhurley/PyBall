from PyBall.models import BaseModel

from .call import Call
from .type import Type


class Detail(BaseModel):
    _fields = {
        'call': {'default_value': {}, 'field_type': Call},
        'description': {'default_value': None, 'field_type': str},
        'code': {'default_value': None, 'field_type': str},
        'ballColor': {'default_value': None, 'field_type': str},
        'trailColor': {'default_value': None, 'field_type': str},
        'isInPlay': {'default_value': None, 'field_type': bool},
        'isStrike': {'default_value': None, 'field_type': bool},
        'isBall': {'default_value': None, 'field_type': bool},
        'type': {'default_value': {}, 'field_type': Type},
        'hasReview': {'default_value': None, 'field_type': bool},
    }
