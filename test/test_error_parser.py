import pytest
from PyBall.error_parser import ErrorParser
from PyBall.exceptions import *

INVALID_ID_CODE = 10
BAD_REQUEST_CODE = 11


@pytest.fixture()
def error_message(request):
    return {
        'messageNumber': request.param,
        'message': 'test message',
    }


@pytest.mark.parametrize(
    'error_message',
    (INVALID_ID_CODE,),
    indirect=True)
def test_parse_invalid_id(error_message):
    with pytest.raises(InvalidIdError):
        ErrorParser.parse_error(error_message)


@pytest.mark.parametrize(
    'error_message',
    (BAD_REQUEST_CODE,),
    indirect=True)
def test_parse_bad_request(error_message):
    with pytest.raises(BadRequestError):
        ErrorParser.parse_error(error_message)


@pytest.mark.parametrize(
    'error_message',
    (0, -1),
    indirect=True)
def test_parse_unknown_error(error_message):
    with pytest.raises(PyBallError):
        ErrorParser.parse_error(error_message)
