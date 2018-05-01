from PyBall.models.base_model import BaseModel


class SeasonDate(BaseModel):
    _fields = {
        'regularSeasonStartDate': {'default_value': None, 'field_type': str},
        'regularSeasonEndDate': {'default_value': None, 'field_type': str},
    }
