from PyBall.models.base_model import BaseModel
from PyBall.models.league import SeasonDate
from PyBall.models.sport import Sport


class League(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'name': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
        'seasonState':  {'default_value': None, 'field_type': str},
        'hasWildCard': {'default_value': None, 'field_type': bool},
        'hasSplitSeason': {'default_value': None, 'field_type': bool},
        'hasPlayoffPoints': {'default_value': None, 'field_type': bool},
        'numTeams': {'default_value': None, 'field_type': int},
        'seasonDateInfo': {'default_value': {}, 'field_type': SeasonDate},
        'orgCode': {'default_value': None, 'field_type': str},
        'conferencesInUse': {'default_value': None, 'field_type': bool},
        'divisionsInUse': {'default_value': None, 'field_type': bool},
        'sport': {'default_value': {}, 'field_type': Sport}
    }
