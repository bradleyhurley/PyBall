import pytest
from pyball import PyBall
from pyball.models import People

from pyball.exceptions import InvalidIdError, BadRequestError


@pytest.fixture(scope='module')
def test_player():
    pyball = PyBall()
    return pyball.get_player(446372)


def test_get_player_endpoint_returns_player(test_player):
    assert isinstance(test_player, People)


def test_bad_player_id():
    pyball = PyBall()
    with pytest.raises(InvalidIdError):
        pyball.get_player(-1)


def test_player_id_not_a_num():
    pyball = PyBall()
    with pytest.raises(BadRequestError):
        pyball.get_player("not_an_id")
