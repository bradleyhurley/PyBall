import pytest
from PyBall import PyBall
from PyBall.models.generic_sport import Sport


@pytest.fixture(scope='module')
def sports():
    pyball = PyBall()
    return pyball.get_sports()


@pytest.fixture(scope='module')
def sport():
    pyball = PyBall()
    return pyball.get_sport_by_id(512)


def test_get_sports_returns_list_of_sports(sports):
    assert isinstance(sports, list)
    assert isinstance(sports[0], Sport)


def test_get_sport_by_id_returns_sport(sport):
    assert isinstance(sport, Sport)
