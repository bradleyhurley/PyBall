from pyball.models.draft.round import Round


class Draft:
    def __init__(self, rounds=None, draftYear=None):
        self.draftYear = draftYear
        self.rounds = [Round(**rnd) for rnd in rounds]
