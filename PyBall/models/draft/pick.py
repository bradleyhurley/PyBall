from PyBall.models.draft.home import Home
from PyBall.models.draft.school import School
from PyBall.models.draft.person import Person


class Pick:
    def __init__(self, bisPlayerId=None, draftPlayerId=None, pickRound=None, pickNumber=None, rank=None,
                 pickedTeamCode=None, home=None, scoutingReport=None, school=None, comments=None, person=None,
                 photoFlag=None):
        self.bisPlayerId = bisPlayerId
        self.draftPlayerId = draftPlayerId
        self.pickRound = pickRound
        self.pickNumber = pickNumber
        self.rank = rank
        self.pickedTeamCode = pickedTeamCode
        self.home = Home(**home)
        self.scoutingReport = scoutingReport
        self.school = School(**school)
        self.comments = comments
        self.person = Person(**person)
        self.photoFlag = photoFlag
