import pytest
from pyball import PyBall
from pyball.models.divisions import Division
from pyball.models.divisions import Sport
from pyball.models.divisions import League

from pyball.exceptions import BadRequestError


@pytest.fixture(scope='module')
def test_division():
    pyball = PyBall()
    return pyball.get_division_by_id(201)


@pytest.fixture(scope='module')
def test_divisions():
    pyball = PyBall()
    return pyball.get_divisions()


def test_get_divisions_returns_divisions(test_divisions):
    assert isinstance(test_divisions, list)
    assert isinstance(test_divisions[0], Division)
    assert isinstance(test_divisions[0].sport, Sport)
    assert isinstance(test_divisions[0].league, League)


def test_get_division_returns_division(test_division):
    assert isinstance(test_division, Division)


def test_bad_division():
    pyball = PyBall()
    with pytest.raises(BadRequestError):
        pyball.get_division_by_id("InvalidID")
