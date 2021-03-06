from pyball.exceptions import *


class ErrorParser:

    @staticmethod
    def parse_error(err_json):
        err_code = err_json['messageNumber']
        err_message = err_json['message']
        if err_code == 1:
            raise NotFound(err_message)
        elif err_code == 10:
            raise InvalidIdError(err_message)
        elif err_code == 11:
            raise BadRequestError(err_message)
        elif err_code == 13:
            raise TookTooLongError(err_message)
        else:
            raise PyBallError(err_message)
