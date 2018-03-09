import pytest
from PyBall.PyBall import PyBall
from PyBall.models.config.league_leader_type import LeagueLeaderType

from PyBall.exceptions import *


@pytest.fixture(scope='module')
def test_league_leader_types():
    pyball = PyBall()
    return pyball.get_league_leader_types()


def test_get_league_leader_types_returns_leagueLeaderTypes(test_league_leader_types):
    assert isinstance(test_league_leader_types, list)
    assert isinstance(test_league_leader_types[0], LeagueLeaderType)