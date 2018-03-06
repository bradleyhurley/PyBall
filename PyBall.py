import requests
from constants import BASE_URL

from models.people import People
from models.game_types import GameType
from models.venue import Venue

from error_parser import ErrorParser


class PyBall:
    def __init__(self):
        self.r = requests

    def _get(self, url):
        results = self.r.get(url).json()
        if 'messageNumber' in results:
            ErrorParser.parse_error(results)
        return results

    def get_player(self, player_id):
        url = "{0}/people/{1}".format(BASE_URL, player_id)
        results = self._get(url)
        return People(**results['people'][0])

    def get_game_types(self):
        game_types = []
        url = "{0}/gameTypes".format(BASE_URL)
        results = self._get(url)
        for game_type in results:
            game_types.append(GameType(**game_type))
        return game_types

    def get_venue(self, venue_id):
        url = "{0}/venues/{1}".format(BASE_URL, venue_id)
        results = self._get(url)
        return Venue(**results['venues'][0])
