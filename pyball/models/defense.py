from pyball.models import BaseModel
from pyball.models.position.position import Center
from pyball.models.position.position import First
from pyball.models.position.position import Left
from pyball.models.position.position import Pitcher
from pyball.models.position.position import Right
from pyball.models.position.position import Second
from pyball.models.position.position import Shortstop
from pyball.models.position.position import Third
from pyball.models.position.position import Catcher

from pyball.models.generic_team import Team


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
