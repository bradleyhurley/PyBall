## PyBall - A MLB.com Stats API Python Client

[![Build Status](https://travis-ci.org/bradleyhurley/PyBall.svg?branch=master)](https://travis-ci.org/bradleyhurley/PyBall)
[![codecov](https://codecov.io/gh/bradleyhurley/PyBall/branch/master/graph/badge.svg)](https://codecov.io/gh/bradleyhurley/PyBall)

## API Documentation:
http://statsapi.mlb.com/docs/#

If anyone has any connection to MLB and can get access to the API documentation I would really appreciate it.

```python
import pyball

def main():
    pb = pyball.PyBall()
    kluber = pb.get_player(446372)
    print(kluber.fullName)
    print(kluber.pitchHand.description)
    print(kluber.batSide.description)


if __name__ == '__main__':
    main()

```

##### This is very much in ~~beta~~ alpha.

## Logging

This library uses logging to alert when the current version of this library does not match the
MLB.com API. All loggers use _PyBall._ as a naming prefix. Use this to disable logging if you do
not desire these alerts.
