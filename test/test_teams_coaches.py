import pytest
from pyball import PyBall
from pyball.models.team import Coach


@pytest.fixture(scope='module')
def test_team_coaches():
    pyball = PyBall()
    return pyball.get_teams_coaches(114)


def test_get_teams_returns_list_of_teams(test_team_coaches):
    assert isinstance(test_team_coaches, list)
    assert isinstance(test_team_coaches[0], Coach)
