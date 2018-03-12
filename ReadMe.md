## PyBall - A MLB.com Stats API Python Client

[![Build Status](https://travis-ci.org/bradleyhurley/PyBall.svg?branch=master)](https://travis-ci.org/bradleyhurley/PyBall)

## API Documentation:
http://statsapi.mlb.com/docs/#


```python
import PyBall


def main():
    pyball = PyBall()
    kluber = pyball.get_player(446372)
    print(kluber.fullName)
    print(kluber.pitchHand.description)
    print(kluber.batSide.description)


if __name__ == '__main__':
    main()

```
##### This is very much in ~~beta~~ alpha.
