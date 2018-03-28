class PyBallError(Exception):
    pass


class BadRequestError(PyBallError):
    pass


class InvalidIdError(PyBallError):
    pass


class TookTooLongError(PyBallError):
    pass
