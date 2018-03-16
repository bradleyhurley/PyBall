from PyBall.models import BaseModel
from PyBall.models.draft.home import Home
from PyBall.models.draft.school import School
from PyBall.models.draft.person import Person


class Pick(BaseModel):
    _fields = {
        'person': {'default_value': {}, 'field_type': Person},
        'bisPlayerId': {'default_value': None, 'field_type': int},
        'draftPlayerId': {'default_value': None, 'field_type': int},
        'pickRound': {'default_value': None, 'field_type': int},
        'pickNumber': {'default_value': None, 'field_type': int},
        'rank': {'default_value': None, 'field_type': int},
        'pickedTeamCode': {'default_value': None, 'field_type': str},
        'home': {'default_value': {}, 'field_type': Home},
        'scoutingReport': {'default_value': None, 'field_type': str},
        'photoFlag': {'default_value': None, 'field_type': bool},
        'school': {'default_value': {}, 'field_type': School},
        'comments': {'default_value': None, 'field_type': str},
    }
