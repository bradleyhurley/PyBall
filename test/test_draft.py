import pytest
from pyball import PyBall
from pyball.models.draft import Draft
from pyball.models.draft import Prospect
from pyball.models.draft import Round
from pyball.models.draft import Pick
from pyball.models.draft import Home
from pyball.models.draft import School
from pyball.models.draft import Person

from pyball.exceptions import BadRequestError


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
