import pytest
from PyBall import PyBall
from PyBall.models.conference import Conference

from PyBall.exceptions import BadRequestError


@pytest.fixture(scope='module')
def test_conference():
    pyball = PyBall()
    return pyball.get_conference_by_id(302)


@pytest.fixture(scope='module')
def test_conferences():
    pyball = PyBall()
    return pyball.get_conferences()


def test_get_conference_returns_list_of_conferences(test_conferences):
    assert isinstance(test_conferences, list)
    assert isinstance(test_conferences[0], Conference)


def test_get_conference_returns_conference(test_conference):
    assert isinstance(test_conference, Conference)


def test_bad_conference():
    pyball = PyBall()
    with pytest.raises(BadRequestError):
        pyball.get_conference_by_id("InvalidID")
