from pyball.models import BaseModel
from pyball.models.sport import Sport
from pyball.models.generic_league import League
from pyball.models.venue import Venue
from pyball.models.division import Division
from pyball.models.springLeague import SpringLeague


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
        'shortName': {'default_value': None, 'field_type': str},
        'springLeague': {'default_value': {}, 'field_type': SpringLeague},
        'active': {'default_value': None, 'field_type': bool},
        'parentOrgId': {'default_value': None, 'field_type': int},
        'parentOrgName': {'default_value': None, 'field_type': str},
    }
