from pyball.models.draft.pick import Pick
from pyball.models import BaseModel


class Round(BaseModel):
    _fields = {
        'roundNumber': {'default_value': None, 'field_type': int},
        'picks': {'default_value': [], 'field_type': [Pick]},
    }
