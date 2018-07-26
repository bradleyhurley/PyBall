import pytest
from pyball import PyBall
from pyball.models.game import BoxScore


@pytest.fixture(scope='module')
def boxscore():
    pyball = PyBall()
    return pyball.get_boxscore_by_id(533979)


def test_get_boxscore_by_id_returns_boxscore(boxscore):
    assert isinstance(boxscore, BoxScore)
