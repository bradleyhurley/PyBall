import pytest
from PyBall import PyBall
from PyBall.models.config import StatsGroup


@pytest.fixture(scope='module')
def test_stats_group():
    pyball = PyBall()
    return pyball.get_stats_groups()


def test_get_situation_codes_returns_situation_codes(test_stats_group):
    assert isinstance(test_stats_group, list)
    assert isinstance(test_stats_group[0], StatsGroup)
