import pytest
from PyBall.PyBall import PyBall
from PyBall.models.config.schedule_event_types import ScheduleEventTypes

from PyBall.exceptions import *


@pytest.fixture(scope='module')
def test_schedule_event_types():
    pyball = PyBall()
    return pyball.get_schedule_event_types()


def test_get_schedule_event_types_returns_schedule_event_types(test_schedule_event_types):
    assert isinstance(test_schedule_event_types, list)
    assert isinstance(test_schedule_event_types[0], ScheduleEventTypes)