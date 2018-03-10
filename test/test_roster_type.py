import pytest
from PyBall import PyBall
from PyBall.models.config import RosterType


@pytest.fixture(scope='module')
def test_roster_types():
    pyball = PyBall()
    return pyball.get_roster_types()


def test_get_roster_types_returns_roster_types(test_roster_types):
    assert isinstance(test_roster_types, list)
    assert isinstance(test_roster_types[0], RosterType)
