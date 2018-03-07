import pytest
from PyBall.PyBall import PyBall
from PyBall.models.config.game_types import GameType

from PyBall.exceptions import *

@pytest.fixture(scope='module')
def test_game_type():
    pyball = PyBall()
    return pyball.get_game_types()


def test_get_game_types_returns_list_of_game_types(test_game_type):
    assert isinstance(test_game_type, list)
    assert isinstance(test_game_type[0], GameType)
