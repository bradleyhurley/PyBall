from pyball.models.base_model import BaseModel


class Sport(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': int},
        'code': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
        'abbreviation': {'default_value': None, 'field_type': str},
    }
