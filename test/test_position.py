import pytest
from PyBall import PyBall
from PyBall.models.config import Position


@pytest.fixture(scope='module')
def test_positions():
    pyball = PyBall()
    return pyball.get_positions()


def test_get_positions_returns_positions(test_positions):
    assert isinstance(test_positions, list)
    assert isinstance(test_positions[0], Position)
