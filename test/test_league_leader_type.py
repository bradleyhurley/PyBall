import pytest
from PyBall import PyBall
from PyBall.models.config import LeagueLeaderType


@pytest.fixture(scope='module')
def test_league_leader_types():
    pyball = PyBall()
    return pyball.get_league_leader_types()


def test_get_league_leader_types_returns_leagueLeaderTypes(test_league_leader_types):
    assert isinstance(test_league_leader_types, list)
    assert isinstance(test_league_leader_types[0], LeagueLeaderType)
