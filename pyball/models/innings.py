from pyball.models import BaseModel
from pyball.models.inning import Inning


class Innings(BaseModel):
    _fields = {
        'inning': {'default_value': {}, 'field_type': Inning},
    }
