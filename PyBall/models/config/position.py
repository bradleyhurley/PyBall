class Position:
    def __init__(self, shortName=None, fullName=None, abbrev=None, code=None, type=None,
                 pitcher=None, fielder=None, outfield=None, displayName=None):
        self.shortName = shortName
        self.fullName = fullName
        self.abbrev = abbrev
        self.code = code
        self.type = type
        self.pitcher = pitcher
        self.outfield = outfield
        self.fielder = fielder
        self.displayName = displayName
