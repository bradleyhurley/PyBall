from PyBall.models import BaseModel


class Language(BaseModel):
    _fields = {
        'name': {'default_value': None, 'field_type': str},
        'languageCode': {'default_value': None, 'field_type': str},
        'locale': {'default_value': None, 'field_type': str},
    }
