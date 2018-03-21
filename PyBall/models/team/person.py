from PyBall.models import BaseModel


class Person(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'link': {'default_value': None, 'field_type': str},
        'fullName': {'default_value': None, 'field_type': str},
    }
