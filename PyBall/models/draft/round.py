from PyBall.models.draft.pick import Pick


class Round:
    def __init__(self, roundNumber=None, picks=None):
        self.roundNumber = roundNumber
        self.picks = []

        for pick in picks:
            self.picks.append(Pick(**pick))
