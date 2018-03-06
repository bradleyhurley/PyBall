class Position:
    def __init__(self, id=None, fullName=None, link=None):
        self.id = id
        self.fullName = fullName
        self.link = link


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
