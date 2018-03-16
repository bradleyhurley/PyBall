from PyBall.models.base_model import BaseModel


class ScheduleEventType(BaseModel):
    _fields = {
        'code': {'default_value': None, 'field_type': str},
        'name': {'default_value': None, 'field_type': str},
    }
