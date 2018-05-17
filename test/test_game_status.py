import pytest
from pyball import PyBall
from pyball.models.config import GameStatus


@pytest.fixture(scope='module')
def test_game_status():
    pyball = PyBall()
    return pyball.get_game_status()


def test_get_game_status_returns_list_of_game_statuses(test_game_status):
    assert isinstance(test_game_status, list)
    assert isinstance(test_game_status[0], GameStatus)
