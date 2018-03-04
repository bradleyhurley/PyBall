import requests
from constants import BASE_URL

from models.people import People


class PyBall:
    def __init__(self):
        self.r = requests

    def get_player(self, player_id):
        url = "{0}/people/{1}".format(BASE_URL, player_id)
        results = self.r.get(url).json()
        return People(**results['people'][0])

