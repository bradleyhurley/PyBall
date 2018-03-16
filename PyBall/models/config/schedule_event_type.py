from PyBall.models import BaseModel


class ScheduleEventType(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
    }
