import pytest
from PyBall.PyBall import PyBall
from PyBall.models.config.roster_type import RosterType

from PyBall.exceptions import *


@pytest.fixture(scope='module')
def test_roster_types():
    pyball = PyBall()
    return pyball.get_roster_types()


def test_get_roster_types_returns_roster_types(test_roster_types):
    assert isinstance(test_roster_types, list)
    assert isinstance(test_roster_types[0], RosterType)