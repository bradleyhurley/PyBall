from PyBall.models import BaseModel
from .type import Type
from .group import Group


class Stat(BaseModel):
    _fields = {
        'type': {'default_value': {}, 'field_type': Type},
        'group': {'default_value': {}, 'field_type': Group},
        'splits': {'default_value': [], 'field_type': int},
    }
