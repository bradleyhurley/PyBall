from PyBall.models.draft.round import Round


class Draft:
    def __init__(self, rounds=None, draftYear=None):
        self.draftYear = draftYear
        self.rounds = []
        for rnd in rounds:
            self.rounds.append(Round(**rnd))
