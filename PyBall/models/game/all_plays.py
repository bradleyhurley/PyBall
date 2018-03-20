from PyBall.models import BaseModel


from .play import Play


class AllPlays(BaseModel):
    _fields = {
        'allPlays': {'default_value': {}, 'field_type': [Play]},
    }
