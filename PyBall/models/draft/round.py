from PyBall.models.draft.pick import Pick


class Round:
    def __init__(self, roundNumber=None, picks=None):
        self.roundNumber = roundNumber
        self.picks = [Pick(**pick) for pick in picks]
