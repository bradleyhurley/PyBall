import requests

from PyBall.constants import BASE_URL
from PyBall.models.config.game_types import GameType
from PyBall.models.people import People
from PyBall.models.venue import Venue

from PyBall.error_parser import ErrorParser

from PyBall.models.config.languages import Languages
from PyBall.models.config.league_leader_types import LeagueLeaderTypes
from PyBall.models.config.metrics import Metrics
from PyBall.models.config.platform import Platform
from PyBall.models.config.positions import Positions
from PyBall.models.config.roster_types import RosterTypes
from PyBall.models.config.schedule_event_types import ScheduleEventTypes
from PyBall.models.config.situation_codes import SituationCodes

from PyBall.models.divisions.division import Division


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

    def get_venue(self, venue_id):
        url = "{0}/venues/{1}".format(BASE_URL, venue_id)
        results = self._get(url)
        return Venue(**results['venues'][0])

    def get_game_status(self):
        pass

    def get_game_types(self):
        game_types = []
        url = "{0}/gameTypes".format(BASE_URL)
        results = self._get(url)
        for game_type in results:
            game_types.append(GameType(**game_type))
        return game_types

    def get_languages(self):
        languages = []
        url = "{0}/languages".format(BASE_URL)
        results = self._get(url)
        for lang in results:
            languages.append(Languages(**lang))
        return languages

    def get_league_leader_types(self):
        leader_types = []
        url = "{0}/leagueLeaderTypes".format(BASE_URL)
        results = self._get(url)
        for leader_type in results:
            leader_types.append(LeagueLeaderTypes(**leader_type))
        return leader_types

    def get_metrics(self):
        metrics = []
        url = "{0}/metrics".format(BASE_URL)
        results = self._get(url)
        for metric in results:
            metrics.append(Metrics(**metric))
        return metrics

    def get_platforms(self):
        platforms = []
        url = "{0}/platforms".format(BASE_URL)
        results = self._get(url)
        for platform in results:
            platforms.append(Platform(**platform))
        return platforms

    def get_positions(self):
        positions = []
        url = "{0}/positions".format(BASE_URL)
        results = self._get(url)
        for position in results:
            positions.append(Positions(**position))
        return positions

    def get_roster_types(self):
        roster_types = []
        url = "{0}/rosterTypes".format(BASE_URL)
        results = self._get(url)
        for roster_type in results:
            roster_types.append(RosterTypes(**roster_type))
        return roster_types

    def get_schedule_event_types(self):
        schedule_event_types = []
        url = "{0}/scheduleEventTypes".format(BASE_URL)
        results = self._get(url)
        for schedule_event_type in results:
            schedule_event_types.append(ScheduleEventTypes(**schedule_event_type))
        return schedule_event_types

    def get_situation_codes(self):
        situation_codes = []
        url = "{0}/situationCodes".format(BASE_URL)
        results = self._get(url)
        for situation_code in results:
            situation_codes.append(SituationCodes(**situation_code))
        return situation_codes

    def get_stats_groups(self):
        pass

    def get_stats_type(self):
        pass

    def get_divisions(self):
        divisions = []
        url = "{0}/divisions".format(BASE_URL)
        results = self._get(url)
        for division in results:
            divisions.append(Division(**division))
        return divisions

    def get_division_by_id(self, division_id):
        url = "{0}/divisions/{1}".format(BASE_URL, division_id)
        results = self._get(url)
        return Division(**results['divisions'][0])
