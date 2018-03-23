import pytest
from PyBall import PyBall
from PyBall.models.team import Player
from PyBall.models.team import Status
from PyBall.models.team import Person


@pytest.fixture(scope='module')
def test_roster_for_team():
    pyball = PyBall()
    return pyball.get_roster_for_team(114, "40Man")


def test_get_roster_for_team_returns_list_of_players(test_roster_for_team):
    assert isinstance(test_roster_for_team, list)
    assert isinstance(test_roster_for_team[0], Player)
    assert isinstance(test_roster_for_team[0].status, Status)
    assert isinstance(test_roster_for_team[0].person, Person)
