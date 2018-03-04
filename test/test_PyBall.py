from PyBall import PyBall


def main():
    pyball = PyBall()

    kluber = pyball.get_player(446372)
    print(kluber.fullName)
    print(kluber.pitchHand.description)
    print(kluber.batSide.description)


if __name__ == '__main__':
    main()
