import pytest
from PyBall.PyBall import PyBall
from PyBall.models.config.situation_codes import SituationCodes

from PyBall.exceptions import *


@pytest.fixture(scope='module')
def test_situation_codes():
    pyball = PyBall()
    return pyball.get_situation_codes()


def test_get_situation_codes_returns_situation_codes(test_situation_codes):
    assert isinstance(test_situation_codes, list)
    assert isinstance(test_situation_codes[0], SituationCodes)