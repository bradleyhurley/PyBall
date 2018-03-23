from inspect import Signature, Parameter
import logging


def make_sig(**fields):
    params = [Parameter(name, Parameter.KEYWORD_ONLY, default=attrs['default_value'])
              for name, attrs
              in fields.items()]
    return Signature(params)


class BaseModelType(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(**clsdict.get('_fields', {}))
        return super().__new__(cls, clsname, bases, clsdict)


class BaseModel(metaclass=BaseModelType):
    _fields = {}
    log = logging.getLogger("PyBall.models")

    def __init__(self, **kwargs):
        for name in self._fields:
            default_value = self._fields[name]['default_value']
            raw_value = kwargs.get(name, default_value)
            field_type = self._fields[name]['field_type']
            if isinstance(field_type, list):
                value = [field_type[0](**x) for x in raw_value]
            elif issubclass(field_type, BaseModel):
                value = field_type(**raw_value)
            else:
                value = raw_value
            setattr(self, name, value)

        extra_fields = kwargs.keys() - self._fields.keys()
        if extra_fields:
            self.log.warn("Extra fields found: {}. Upgrade PyBall to access new data fields."
                          .format(', '.join(extra_fields)))
