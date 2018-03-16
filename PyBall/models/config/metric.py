from PyBall.models import BaseModel


class Metric(BaseModel):
    _fields = {
        'group': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': bool},
        'unit': {'default_value': None, 'field_type': str},
        'metricId': {'default_value': None, 'field_type': int},
    }
