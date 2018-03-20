from PyBall.models import BaseModel


class About(BaseModel):
    _fields = {
        'atBatIndex': {'default_value': None, 'field_type': int},
        'halfInning': {'default_value': None, 'field_type': str},
        'inning': {'default_value': None, 'field_type': int},
        'startTime': {'default_value': None, 'field_type': str},
        'endTime': {'default_value': None, 'field_type': str},
        'isComplete': {'default_value': None, 'field_type': bool},
        'isScoringPlay': {'default_value': None, 'field_type': bool},
        'hasReview': {'default_value': None, 'field_type': bool},
        'hasOut': {'default_value': None, 'field_type': bool},
        'captivatingIndex': {'default_value': None, 'field_type': int},
    }
