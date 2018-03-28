import pytest
from PyBall import PyBall
from PyBall.models.config import StandingType


@pytest.fixture(scope='module')
def test_standing_types():
    pyball = PyBall()
    return pyball.get_standing_types()


def test_get_standing_types_returns_list_of_standing_types(test_standing_types):
    assert isinstance(test_standing_types, list)
    assert isinstance(test_standing_types[0], StandingType)
