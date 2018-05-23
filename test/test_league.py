import pytest
from pyball import PyBall
from pyball.models import League


@pytest.fixture(scope='module')
def league():
    pyball = PyBall()
    league_id = pyball.get_teams()[0].league.id
    return pyball.get_league_by_id(league_id)


def test_get_league_returns_league(league):
    assert isinstance(league, League)
