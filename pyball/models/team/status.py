from pyball.models import BaseModel


class Status(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': str},
        'description': {'default_value': None, 'field_type': str},
    }
