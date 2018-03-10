class BaseModel:
    _fields = {}

    def __init__(self, **kwargs):
        for name in self._fields:
            raw_value = kwargs.get(name, self._fields[name]['default_value'])
            field_type = self._fields[name]['field_type']
            if issubclass(field_type, BaseModel):
                value = field_type(raw_value)
            else:
                value = raw_value
            setattr(self, name, value)
