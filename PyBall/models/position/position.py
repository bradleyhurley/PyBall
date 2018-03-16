from PyBall.models import BaseModel


class Position(BaseModel):
    _fields = {
        'id': {'default_value': None, 'field_type': str},
        'fullName': {'default_value': None, 'field_type': str},
        'link': {'default_value': None, 'field_type': str},
    }


class Pitcher(Position):
    pass


class Catcher(Position):
    pass


class First(Position):
    pass


class Second(Position):
    pass


class Third(Position):
    pass


class Shortstop(Position):
    pass


class Left(Position):
    pass


class Center(Position):
    pass


class Right(Position):
    pass


class Batter(Position):
    pass


class OnDeck(Position):
    pass


class InHole(Position):
    pass
