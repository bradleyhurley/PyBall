import pytest
from PyBall import PyBall
from PyBall.models.config import Platform


@pytest.fixture(scope='module')
def test_platform():
    pyball = PyBall()
    return pyball.get_platforms()


def test_get_platform_returns_platform(test_platform):
    assert isinstance(test_platform, list)
    assert isinstance(test_platform[0], Platform)
