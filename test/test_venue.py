import pytest
from PyBall import PyBall
from PyBall.models import Venue

from PyBall.exceptions import BadRequestError, InvalidIdError


@pytest.fixture(scope='module')
def test_venue():
    pyball = PyBall()
    return pyball.get_venue(1)


def test_get_venue_endpoint_returns_venue(test_venue):
    assert isinstance(test_venue, Venue)


def test_bad_venue_id():
    pyball = PyBall()
    with pytest.raises(InvalidIdError):
        pyball.get_venue(-1)


def test_venue_id_not_a_num():
    pyball = PyBall()
    with pytest.raises(BadRequestError):
        pyball.get_venue("not_an_id")
