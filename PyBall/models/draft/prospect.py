from PyBall.models import BaseModel
from PyBall.models.draft.home import Home
from PyBall.models.draft.school import School
from PyBall.models.draft.person import Person


class Prospect(BaseModel):
    _fields = {
        'bisPlayerId': {'default_value': None, 'field_type': int},
        'draftPlayerId': {'default_value': None, 'field_type': int},
        'pickRound': {'default_value': None, 'field_type': float},
        'pickNumber': {'default_value': None, 'field_type': float},
        'rank': {'default_value': None, 'field_type': float},
        'pickedTeamCode': {'default_value': None, 'field_type': str},
        'home': {'default_value': {}, 'field_type': Home},
        'scoutingReport': {'default_value': None, 'field_type': str},
        'school': {'default_value': {}, 'field_type': School},
        'comments': {'default_value': None, 'field_type': str},
        'person': {'default_value': {}, 'field_type': Person},
        'photoFlag': {'default_value': None, 'field_type': bool},
    }
