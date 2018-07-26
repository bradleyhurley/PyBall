import requests
from datetime import datetime
from typing import List, Dict, Any, Union

from pyball.constants import BASE_URL
from pyball.models.config.game_type import GameType

from pyball.models import League
from pyball.models import Person
from pyball.models import Venue

from pyball.error_parser import ErrorParser

from pyball.models.config.language import Language
from pyball.models.config.league_leader_type import LeagueLeaderType
from pyball.models.config.metric import Metric
from pyball.models.config.platform import Platform
from pyball.models.config.position import Position
from pyball.models.config.roster_type import RosterType
from pyball.models.config.schedule_event_type import ScheduleEventType
from pyball.models.config.situation_code import SituationCode
from pyball.models.config.stats_group import StatsGroup
from pyball.models.config import StatsType
from pyball.models.config import StandingType
from pyball.models.config import GameStatus

from pyball.models.divisions import Division

from pyball.models.conference import Conference

from pyball.models.draft import Draft
from pyball.models.draft import Prospect
from pyball.models import Team
from pyball.models import Sport
from pyball.models.team import Coach
from pyball.models.team import Player

from pyball.models.game import BoxScore


class PyBall:
    def __init__(self):
        self.r = requests

    def _get(self, url: str) -> Union[Dict[str, Any], List[Any]]:
        results = self.r.get(url).json()
        if 'messageNumber' in results:
            ErrorParser.parse_error(results)
        return results

    def get_player(self, player_id: int) -> Person:
        url = "{0}/people/{1}".format(BASE_URL, player_id)
        results = self._get(url)
        return Person(**results['people'][0])

    def get_venue(self, venue_id: int) -> Venue:
        url = "{0}/venues/{1}".format(BASE_URL, venue_id)
        results = self._get(url)
        return Venue(**results['venues'][0])

    def get_game_status(self) -> List[GameStatus]:
        url = "{0}gameStatus".format(BASE_URL)
        results = self._get(url)
        return [GameStatus(**game_status) for game_status in results]

    def get_game_types(self) -> List[GameType]:
        url = "{0}/gameTypes".format(BASE_URL)
        results = self._get(url)
        return [GameType(**game_type) for game_type in results]

    def get_standing_types(self) -> List[StandingType]:
        url = "{0}/standingsTypes".format(BASE_URL)
        results = self._get(url)
        return [StandingType(**standing_type) for standing_type in results]

    def get_languages(self) -> List[Language]:
        url = "{0}/languages".format(BASE_URL)
        results = self._get(url)
        return [Language(**lang) for lang in results]

    def get_league_leader_types(self) -> List[LeagueLeaderType]:
        url = "{0}/leagueLeaderTypes".format(BASE_URL)
        results = self._get(url)
        return [LeagueLeaderType(**leader_type) for leader_type in results]

    def get_metrics(self) -> List[Metric]:
        url = "{0}/metrics".format(BASE_URL)
        results = self._get(url)
        return [Metric(**metric) for metric in results]

    def get_platforms(self) -> List[Platform]:
        url = "{0}/platforms".format(BASE_URL)
        results = self._get(url)
        return [Platform(**platform) for platform in results]

    def get_positions(self) -> List[Position]:
        url = "{0}/positions".format(BASE_URL)
        results = self._get(url)
        return [Position(**position) for position in results]

    def get_roster_types(self) -> List[RosterType]:
        url = "{0}/rosterTypes".format(BASE_URL)
        results = self._get(url)
        return [RosterType(**roster_type) for roster_type in results]

    def get_schedule_event_types(self) -> List[ScheduleEventType]:
        url = "{0}/scheduleEventTypes".format(BASE_URL)
        results = self._get(url)
        return [ScheduleEventType(**schedule_event_type) for schedule_event_type in results]

    def get_situation_codes(self) -> List[SituationCode]:
        url = "{0}/situationCodes".format(BASE_URL)
        results = self._get(url)
        return [SituationCode(**situation_code) for situation_code in results]

    def get_stats_groups(self) -> List[StatsGroup]:
        url = "{0}/statGroups".format(BASE_URL)
        results = self._get(url)
        return [StatsGroup(**stats_group) for stats_group in results]

    def get_stats_type(self) -> List[StatsType]:
        url = "{0}/statTypes".format(BASE_URL)
        results = self._get(url)
        return [StatsType(**stats_type) for stats_type in results]

    def get_divisions(self) -> List[Division]:
        url = "{0}/divisions".format(BASE_URL)
        results = self._get(url)
        return [Division(**division) for division in results['divisions']]

    def get_division_by_id(self, division_id: int) -> Division:
        url = "{0}/divisions/{1}".format(BASE_URL, division_id)
        results = self._get(url)
        return Division(**results['divisions'][0])

    def get_conferences(self) -> List[Conference]:
        url = "{0}/conferences/".format(BASE_URL)
        results = self._get(url)
        return [Conference(**conference) for conference in results['conferences']]

    def get_conference_by_id(self, conference_id: int) -> Conference:
        url = "{0}/conferences/{1}".format(BASE_URL, conference_id)
        results = self._get(url)
        return Conference(**results['conferences'][0])

    def get_draft(self):
        raise NotImplementedError

    def get_draft_prospects(self):
        raise NotImplementedError

    def get_draft_by_year(self, year: int=datetime.now().year - 1) -> Draft:
        url = "{0}/draft/{1}".format(BASE_URL, year)
        results = self._get(url)
        return Draft(**results['drafts'])

    def get_draft_prospects_by_year(self, year: int=datetime.now().year - 1) -> List[Prospect]:
        url = "{0}/draft/prospects/{1}".format(BASE_URL, year)
        results = self._get(url)
        return [Prospect(**prospect) for prospect in results['prospects']]

    def get_teams(self) -> List[Team]:
        url = "{0}/teams".format(BASE_URL)
        results = self._get(url)
        return [Team(**team) for team in results['teams']]

    def get_team_by_id(self, team_id: int) -> Team:
        url = "{0}/teams/{1}".format(BASE_URL, team_id)
        results = self._get(url)
        return Team(**results['teams'][0])

    def get_team_affiliates(self, team_id: int) -> List[Team]:
        url = "{0}/teams/{1}/affiliates".format(BASE_URL, team_id)
        results = self._get(url)
        return [Team(**team) for team in results['teams']]

    def get_teams_coaches(self, team_id: int) -> List[Coach]:
        url = "{0}/teams/{1}/coaches".format(BASE_URL, team_id)
        results = self._get(url)
        return [Coach(**coach) for coach in results['roster']]

    def get_roster_for_team(self, team_id: int, roster_type: str) -> List[Player]:
        url = "{0}teams/{1}/roster/{2}".format(BASE_URL, team_id, roster_type)
        results = self._get(url)
        return [Player(**player) for player in results['roster']]

    def get_league_by_id(self, league_id: int) -> League:
        url = "{0}/league/{1}".format(BASE_URL, league_id)
        results = self._get(url)
        return League(**results['leagues'][0])

    def get_sports(self) -> List[Sport]:
        url = "{0}sports".format(BASE_URL)
        results = self._get(url)
        return [Sport(**sport) for sport in results['sports']]

    def get_sport_by_id(self, sport_id: int) -> Sport:
        url = "{0}sports/{1}".format(BASE_URL, sport_id)
        results = self._get(url)
        return Sport(**results['sports'][0])

    def get_seasons(self):
        # url = "{0}seasons/".format(BASE_URL)
        # results = self._get(url)
        raise NotImplementedError

    def get_season_by_id(self, season_id):
        # url = "{0}seasons/{1}".format(BASE_URL, season_id)
        # results = self._get(url)
        raise NotImplementedError

    def get_boxscore_by_id(self, game_id: int) -> BoxScore:
        url = f"{BASE_URL}game/{game_id}/boxscore"
        results = self._get(url)
        return BoxScore(**results)
