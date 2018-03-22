from pyball.models.sport import Sport
from pyball.models.league import League


class Conference:
    def __init__(self, id=None, link=None, name=None, abbreviation=None, hasWildcard=None,
                 nameShort=None, league=None, sport=None):
        self.id = id
        self.link = link
        self.name = name
        self.abbreviation = abbreviation
        self.hasWildCard = hasWildcard
        self.nameShort = nameShort
        self.league = League(**league)
        self.sport = Sport(**sport)
