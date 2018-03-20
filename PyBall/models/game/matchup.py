from PyBall.models import BaseModel
from .batter import Batter
from .batter_hot_cold_zone_stats import BatterHotColdZoneStats
from PyBall.models import BatSide
from PyBall.models import PitchHand
from PyBall.models.position import Pitcher


class MatchUp(BaseModel):
    _fields = {
        'batter': {'default_value': {}, 'field_type': Batter},
        'batSide': {'default_value': {}, 'field_type': BatSide},
        'pitcher': {'default_value': {}, 'field_type': Pitcher},
        'pitchHand': {'default_value': {}, 'field_type': PitchHand},
        'batterHotColdZoneStats': {'default_value': {}, 'field_type': BatterHotColdZoneStats},
        'batterHotColdZones': {'default_value': [], 'field_type': list},
        'pitcherHotColdZones': {'default_value': [], 'field_type': list},
        'splits': {'default_value': {}, 'field_type': dict},

    }
