from PyBall.models import BaseModel
from PyBall.models.inning import Inning


class Innings(BaseModel):
    _fields = {
        'inning': {'default_value': {}, 'field_type': Inning},
    }
