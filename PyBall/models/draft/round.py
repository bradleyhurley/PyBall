from PyBall.models.draft.pick import Pick
from PyBall.models import BaseModel


class Round(BaseModel):
    _fields = {
        'roundNumber': {'default_value': None, 'field_type': int},
        'picks': {'default_value': [], 'field_type': [Pick]},
    }
