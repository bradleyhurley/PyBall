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

from PyBall.models.conference.conference import Conference


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
        url = "{0}/gameTypes".format(BASE_URL)
        results = self._get(url)
        return [GameType(**game_type) for game_type in results]

    def get_languages(self):
        url = "{0}/languages".format(BASE_URL)
        results = self._get(url)
        return [Languages(**lang) for lang in results]

    def get_league_leader_types(self):
        url = "{0}/leagueLeaderTypes".format(BASE_URL)
        results = self._get(url)
        return [LeagueLeaderTypes(**leader_type) for leader_type in results]

    def get_metrics(self):
        url = "{0}/metrics".format(BASE_URL)
        results = self._get(url)
        return [Metrics(**metric) for metric in results]

    def get_platforms(self):
        url = "{0}/platforms".format(BASE_URL)
        results = self._get(url)
        return [Platform(**platform) for platform in results]

    def get_positions(self):
        url = "{0}/positions".format(BASE_URL)
        results = self._get(url)
        return [Positions(**position) for position in results]

    def get_roster_types(self):
        url = "{0}/rosterTypes".format(BASE_URL)
        results = self._get(url)
        return [RosterTypes(**roster_type) for roster_type in results]

    def get_schedule_event_types(self):
        url = "{0}/scheduleEventTypes".format(BASE_URL)
        results = self._get(url)
        return [ScheduleEventTypes(**schedule_event_type) for schedule_event_type in results]

    def get_situation_codes(self):
        url = "{0}/situationCodes".format(BASE_URL)
        results = self._get(url)
        return [SituationCodes(**situation_code) for situation_code in results]

    def get_stats_groups(self):
        pass

    def get_stats_type(self):
        pass

    def get_divisions(self):
        url = "{0}/divisions".format(BASE_URL)
        results = self._get(url)
        return [Division(**division) for division in results['divisions']]

    def get_division_by_id(self, division_id):
        url = "{0}/divisions/{1}".format(BASE_URL, division_id)
        results = self._get(url)
        return Division(**results['divisions'][0])

    def get_conferences(self):
        url = "{0}/conferences/".format(BASE_URL)
        results = self._get(url)
        return [Conference(**conference) for conference in results['conferences']]

    def get_conference_by_id(self, conference_id):
        url = "{0}/conferences/{1}".format(BASE_URL, conference_id)
        results = self._get(url)
        return Conference(**results['conferences'][0])
