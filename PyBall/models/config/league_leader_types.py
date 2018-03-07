from PyBall.models.config.valid_sports import ValidSports


class LeagueLeaderTypes:
    def __init__(self, displayName=None, validSports=None, hasMinimums=None):
        self.displayName = displayName
        self.hasMinimums = hasMinimums
        self.validSports = []

        for vs in validSports:
            self.validSports.append(ValidSports(**vs))
