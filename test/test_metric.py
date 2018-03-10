import pytest
from PyBall import PyBall
from PyBall.models.config import Metric


@pytest.fixture(scope='module')
def test_metrics():
    pyball = PyBall()
    return pyball.get_metrics()


def test_get_metrics_returns_metrics(test_metrics):
    assert isinstance(test_metrics, list)
    assert isinstance(test_metrics[0], Metric)
