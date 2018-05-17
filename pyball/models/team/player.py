from pyball.models import BaseModel
from .person import Person
from .status import Status


class Player(BaseModel):
    _fields = {
        'person': {'default_value': {}, 'field_type': Person},
        'jerseyNumber': {'default_value': None, 'field_type': str},
        'status': {'default_value': {}, 'field_type': Status},
        'parentTeamId': {'default_value': None, 'field_type': int},

    }
