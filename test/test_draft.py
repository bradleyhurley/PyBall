import pytest
from PyBall import PyBall
from PyBall.models.draft import Draft
from PyBall.models.draft import Prospect
from PyBall.models.draft import Round
from PyBall.models.draft import Pick
from PyBall.models.draft import Home
from PyBall.models.draft import School
from PyBall.models.draft import Person

from PyBall.exceptions import BadRequestError, NotFound
from PyBall.constants import BASE_URL


@pytest.fixture(scope='module')
def test_draft():
    pyball = PyBall()
    return pyball.get_draft_by_year(2017)


@pytest.fixture(scope='module')
def test_prospects():
    pyball = PyBall()
    return pyball.get_draft_prospects_by_year(2017)


def test_get_prospects_returns_prospects(test_prospects):
    assert isinstance(test_prospects, list)
    assert isinstance(test_prospects[0], Prospect)


def test_get_draft_returns_draft(test_draft):
    assert isinstance(test_draft, Draft)
    assert test_draft.draftYear == 2017
    assert isinstance(test_draft.rounds[0], Round)
    assert isinstance(test_draft.rounds[0].picks[0], Pick)
    assert isinstance(test_draft.rounds[0].picks[0].home, Home)
    assert isinstance(test_draft.rounds[0].picks[0].school, School)
    assert isinstance(test_draft.rounds[0].picks[0].person, Person)


def test_bad_draft_year():
    pyball = PyBall()
    with pytest.raises(BadRequestError):
        pyball.get_draft_by_year("BadYear")


def test_get_not_implemented_draft():
    pyball = PyBall()
    with pytest.raises(NotImplementedError):
        pyball.get_draft()


def test_get_not_implemented_draft_prospects():
    pyball = PyBall()
    with pytest.raises(NotImplementedError):
        pyball.get_draft_prospects()


def test_get_not_found_draft():
    pyball = PyBall()
    with pytest.raises(NotFound):
        pyball._get("{}/draft".format(BASE_URL))


def test_get_not_found_draft_prospects():
    pyball = PyBall()
    with pytest.raises(NotFound):
        pyball._get("{}/draft/prospects".format(BASE_URL))

