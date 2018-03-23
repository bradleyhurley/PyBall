from PyBall.models import BaseModel
from .person import Person


class Coach(BaseModel):
    _fields = {
        'person': {'default_value': {}, 'field_type': Person},
        'jerseyNumber': {'default_value': None, 'field_type': str},
        'job': {'default_value': None, 'field_type': str},
        'jobId': {'default_value': None, 'field_type': str},
    }
