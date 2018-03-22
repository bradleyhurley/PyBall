import requests
from datetime import datetime

from pyball.constants import BASE_URL
from pyball.models.config.game_type import GameType
from pyball.models.people import People
from pyball.models.venue import Venue

from pyball.error_parser import ErrorParser

from pyball.models.config.language import Language
from pyball.models.config.league_leader_type import LeagueLeaderType
from pyball.models.config.metric import Metric
from pyball.models.config.platform import Platform
from pyball.models.config.position import Position
from pyball.models.config.roster_type import RosterType
from pyball.models.config.schedule_event_type import ScheduleEventType
from pyball.models.config.situation_code import SituationCode

from pyball.models.divisions import Division

from pyball.models.conference import Conference

from pyball.models.draft import Draft
from pyball.models.draft import Prospect


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
        return [Language(**lang) for lang in results]

    def get_league_leader_types(self):
        url = "{0}/leagueLeaderTypes".format(BASE_URL)
        results = self._get(url)
        return [LeagueLeaderType(**leader_type) for leader_type in results]

    def get_metrics(self):
        url = "{0}/metrics".format(BASE_URL)
        results = self._get(url)
        return [Metric(**metric) for metric in results]

    def get_platforms(self):
        url = "{0}/platforms".format(BASE_URL)
        results = self._get(url)
        return [Platform(**platform) for platform in results]

    def get_positions(self):
        url = "{0}/positions".format(BASE_URL)
        results = self._get(url)
        return [Position(**position) for position in results]

    def get_roster_types(self):
        url = "{0}/rosterTypes".format(BASE_URL)
        results = self._get(url)
        return [RosterType(**roster_type) for roster_type in results]

    def get_schedule_event_types(self):
        url = "{0}/scheduleEventTypes".format(BASE_URL)
        results = self._get(url)
        return [ScheduleEventType(**schedule_event_type) for schedule_event_type in results]

    def get_situation_codes(self):
        url = "{0}/situationCodes".format(BASE_URL)
        results = self._get(url)
        return [SituationCode(**situation_code) for situation_code in results]

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

    def get_draft_by_year(self, year=datetime.now().year - 1):
        url = "{0}/draft/{1}".format(BASE_URL, year)
        results = self._get(url)
        return Draft(**results['drafts'][0])

    def get_draft_prospects_by_year(self, year=datetime.now().year - 1):
        url = "{0}/draft/prospects/{1}".format(BASE_URL, year)
        results = self._get(url)
        return [Prospect(**prospect) for prospect in results['prospects']]
