from PyBall.models.league import League
from PyBall.models.sport import Sport


class Division:
    def __init__(self, id=None, name=None, nameShort=None, link=None, abbreviation=None,
                 league=None, sport=None, hasWildcard=None):
        self.id = id
        self.name = name
        self.nameShort = nameShort
        self.link = link
        self.abbreviation = abbreviation
        self.league = League(**(league or {}))
        self.sport = Sport(**(sport or {}))
        self.hasWildcard = hasWildcard
