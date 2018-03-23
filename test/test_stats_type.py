import pytest
from PyBall import PyBall
from PyBall.models.config import StatsType


@pytest.fixture(scope='module')
def test_stats_type():
    pyball = PyBall()
    return pyball.get_stats_type()


def test_get_situation_codes_returns_situation_codes(test_stats_type):
    assert isinstance(test_stats_type, list)
    assert isinstance(test_stats_type[0], StatsType)
