import pytest
from pyball import PyBall
from datetime import date
from pyball.models.schedule import Schedule, Game, Team, Status, Content, Teams, Home, Away
from pyball.models.venue import Venue


@pytest.fixture(scope='module')
def schedules():
    pyball = PyBall()
    return pyball.get_schedule(start_date=date(2019, 4, 1), end_date=date(2019, 4, 1),
                               team_id=114, game_type='R')


def test_get_schedule_returns_list_of_schedules(schedules):
    assert isinstance(schedules, list)
    assert isinstance(schedules[0], Schedule)
    assert isinstance(schedules[0].games, list)
    assert isinstance(schedules[0].games[0], Game)
    assert isinstance(schedules[0].games[0].teams, Teams)
    assert isinstance(schedules[0].games[0].teams.home, Home)
    assert isinstance(schedules[0].games[0].teams.home.team, Team)
    assert isinstance(schedules[0].games[0].teams.away, Away)
    assert isinstance(schedules[0].games[0].teams.away.team, Team)
    assert isinstance(schedules[0].games[0].status, Status)
    assert isinstance(schedules[0].games[0].venue, Venue)
    assert isinstance(schedules[0].games[0].content, Content)
