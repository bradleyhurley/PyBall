from pyball.models import BaseModel
from pyball.models.position.position import Batter
from pyball.models.position.position import InHole
from pyball.models.position.position import OnDeck
from pyball.models.position.position import Pitcher
from pyball.models.generic_team import Team


class Offense(BaseModel):
    _fields = {
        'batter': {'default_value': {}, 'field_type': Batter},
        'onDeck': {'default_value': {}, 'field_type': OnDeck},
        'inHole': {'default_value': {}, 'field_type': InHole},
        'pitcher': {'default_value': {}, 'field_type': Pitcher},
        'team': {'default_value': {}, 'field_type': Team},
    }
