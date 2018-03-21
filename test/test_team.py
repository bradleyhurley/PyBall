import pytest
from PyBall import PyBall
from PyBall.models import Team
from PyBall.models import Sport
from PyBall.models import League
from PyBall.models import Venue
from PyBall.models import Division
from PyBall.models import SpringLeague



@pytest.fixture(scope='module')
def test_game_teams():
    pyball = PyBall()
    return pyball.get_teams()


@pytest.fixture(scope='module')
def test_game_teams_by_id():
    pyball = PyBall()
    return pyball.get_team_by_id(114)


@pytest.fixture(scope='module')
def test_get_team_affiliates():
    pyball = PyBall()
    return pyball.get_team_affiliates(114)


def test_get_teams_returns_list_of_teams(test_game_teams):
    assert isinstance(test_game_teams, list)
    assert isinstance(test_game_teams[0], Team)


def test_get_team_by_id(test_game_teams_by_id):
    assert isinstance(test_game_teams_by_id, Team)


def test_get_teams_affiliates_returns_list_of_teams(test_get_team_affiliates):
    assert isinstance(test_get_team_affiliates, list)
    assert isinstance(test_get_team_affiliates[0], Team)
    assert isinstance(test_get_team_affiliates[0].venue, Venue)
    assert isinstance(test_get_team_affiliates[0].league, League)
    assert isinstance(test_get_team_affiliates[0].division, Division)
    assert isinstance(test_get_team_affiliates[0].sport, Sport)
    assert isinstance(test_get_team_affiliates[0].springLeague, SpringLeague)
    assert isinstance(test_get_team_affiliates[0].active, bool)
    assert isinstance(test_get_team_affiliates[0].id, int)
