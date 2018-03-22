from PyBall.models import BaseModel
from PyBall.models.position.position import Batter
from PyBall.models.position.position import InHole
from PyBall.models.position.position import OnDeck
from PyBall.models.position.position import Pitcher
from PyBall.models.team import Team


class Offense(BaseModel):
    _fields = {
        'batter': {'default_value': {}, 'field_type': Batter},
        'onDeck': {'default_value': {}, 'field_type': OnDeck},
        'inHole': {'default_value': {}, 'field_type': InHole},
        'pitcher': {'default_value': {}, 'field_type': Pitcher},
        'team': {'default_value': {}, 'field_type': Team},
    }
