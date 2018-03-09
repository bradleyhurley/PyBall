from PyBall.models.sport import Sport
from PyBall.models.league import League
from PyBall.models.venue import Venue


class Team:
    def __init__(self, id=None, name=None, link=None, teamCode=None, fileCode=None,
                 abbreviation=None, teamName=None, locationName=None, firstYearOfPlay=None,
                 shortName=None, active=None, sport=None, venue=None, league=None):
        self.id = id
        self.name = name
        self.link = link
        self.teamCode = teamCode
        self.fileCode = fileCode
        self.abbreviation = abbreviation
        self.teamName = teamName
        self.locationName = locationName
        self.firstYearOfPlay = firstYearOfPlay
        self.shortName = shortName
        self.active = active
        self.sport = Sport(**sport)
        self.league = League(**league)
        self.venue = Venue(**venue)
