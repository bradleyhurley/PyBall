from PyBall.models import BaseModel
from PyBall.models.position.position import Center
from PyBall.models.position.position import First
from PyBall.models.position.position import Left
from PyBall.models.position.position import Pitcher
from PyBall.models.position.position import Right
from PyBall.models.position.position import Second
from PyBall.models.position.position import Shortstop
from PyBall.models.position.position import Third
from PyBall.models.position.position import Catcher

from PyBall.models.team import Team


class Defense(BaseModel):
    _fields = {
        'pitcher': {'default_value': {}, 'field_type': Pitcher},
        'catcher': {'default_value': {}, 'field_type': Catcher},
        'first': {'default_value': {}, 'field_type': First},
        'second': {'default_value': {}, 'field_type': Second},
        'third': {'default_value': {}, 'field_type': Third},
        'shortstop': {'default_value': {}, 'field_type': Shortstop},
        'left': {'default_value': {}, 'field_type': Left},
        'center': {'default_value': {}, 'field_type': Center},
        'right': {'default_value': {}, 'field_type': Right},
        'team': {'default_value': {}, 'field_type': Team},
    }
