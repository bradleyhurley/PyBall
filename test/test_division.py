import pytest
from PyBall.PyBall import PyBall
from PyBall.models.divisions.division import Division

from PyBall.exceptions import *


@pytest.fixture(scope='module')
def test_division():
    pyball = PyBall()
    return pyball.get_division_by_id(201)


def test_get_venue_endpoint_returns_venue(test_division):
    assert isinstance(test_division, Division)


def test_bad_division():
    pyball = PyBall()
    with pytest.raises(BadRequestError):
        pyball.get_division_by_id("InvalidID")
