class PyBallError(Exception):
    pass


class BadRequestError(PyBallError):
    pass


class InvalidIdError(PyBallError):
    pass


class NotFound(PyBallError):
    pass
