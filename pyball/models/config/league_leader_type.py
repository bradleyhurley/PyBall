from pyball.models.config.valid_sport import ValidSport


class LeagueLeaderType:
    def __init__(self, displayName=None, validSports=None, hasMinimums=None):
        self.displayName = displayName
        self.hasMinimums = hasMinimums
        self.validSports = []

        for vs in validSports:
            self.validSports.append(ValidSport(**vs))
