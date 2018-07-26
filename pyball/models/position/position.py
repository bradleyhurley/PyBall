from dataclasses import dataclass


@dataclass
class Position:
    id: str = None
    fullName: str = None
    link: str = None


@dataclass
class Pitcher(Position):
    pass


@dataclass
class Catcher(Position):
    pass


@dataclass
class First(Position):
    pass


@dataclass
class Second(Position):
    pass


@dataclass
class Third(Position):
    pass


@dataclass
class Shortstop(Position):
    pass


@dataclass
class Left(Position):
    pass


@dataclass
class Center(Position):
    pass


@dataclass
class Right(Position):
    pass


@dataclass
class Batter(Position):
    pass


@dataclass
class OnDeck(Position):
    pass


@dataclass
class InHole(Position):
    pass
