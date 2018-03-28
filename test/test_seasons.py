import pytest
from PyBall import PyBall
from PyBall.constants import BASE_URL

from PyBall.exceptions import TookTooLongError


def test_get_season_took_too_long():
    pyball = PyBall()
    with pytest.raises(TookTooLongError):
        pyball._get("{0}/seasons".format(BASE_URL))


def test_get_season_by_id_took_too_long():
    pyball = PyBall()
    with pytest.raises(TookTooLongError):
        pyball._get("{0}/seasons/{1}".format(BASE_URL, "fall"))


def test_get_season():
    pyball = PyBall()
    with pytest.raises(NotImplementedError):
        pyball.get_seasons()


def test_get_season_by_id():
    pyball = PyBall()
    with pytest.raises(NotImplementedError):
        pyball.get_season_by_id("AnyValue")
