import pytest
from PyBall.PyBall import PyBall
from PyBall.models.config.language import Language

from PyBall.exceptions import *


@pytest.fixture(scope='module')
def test_languages():
    pyball = PyBall()
    return pyball.get_languages()


def test_get_languages_returns_languages(test_languages):
    assert isinstance(test_languages, list)
    assert isinstance(test_languages[0], Language)
