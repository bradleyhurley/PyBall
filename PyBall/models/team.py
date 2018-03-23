from PyBall.models import BaseModel
from PyBall.models.sport import Sport
from PyBall.models.league import League
from PyBall.models.venue import Venue
from PyBall.models.division import Division
from PyBall.models.springLeague import SpringLeague


class Team(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'link': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
        'venue': {'default_value': {}, 'field_type': Venue},
        'teamCode': {'default_value': None, 'field_type': str},
        'fileCode': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
        'teamName': {'default_value': None, 'field_type': str},
        'locationName': {'default_value': None, 'field_type': str},
        'firstYearOfPlay': {'default_value': None, 'field_type': str},
        'league': {'default_value': {}, 'field_type': League},
        'division': {'default_value': {}, 'field_type': Division},
        'sport': {'default_value': {}, 'field_type': Sport},
        'springLeague': {'default_value': {}, 'field_type': SpringLeague},
        'active': {'default_value': None, 'field_type': bool},
    }
