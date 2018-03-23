from PyBall.models.draft.round import Round
from PyBall.models import BaseModel


class Draft(BaseModel):
    _fields = {
        'draftYear': {'default_value': None, 'field_type': int},
        'rounds': {'default_value': [], 'field_type': [Round]},
    }
