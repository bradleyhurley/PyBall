import pytest
from PyBall import PyBall
from PyBall.constants import BASE_URL


def test_get_not_implemented_standings():
    pyball = PyBall()
    with pytest.raises(NotImplementedError):
        pyball.get_standings(standing_type="byDivision")


def test_get_standings_is_empty_list():
    pyball = PyBall()
    url = "{0}/standings/{1}".format(BASE_URL, "byDivision")
    results = pyball._get(url)
    assert isinstance(results['records'], list)
    assert results['records'] == []
