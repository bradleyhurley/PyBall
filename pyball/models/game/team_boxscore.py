from dataclasses import dataclass, InitVar, field
from typing import Dict, List, Any, Union

from .note import Note
from pyball.models import Team


@dataclass
class Record:
    gamesPlayed: int = None
    wildCardGamesBack: str = None
    leagueGamesBack: str = None
    springLeagueGamesBack: str = None
    sportGamesBack: str = None
    divisionGamesBack: str = None
    conferenceGamesBack: str = None
    leagueRecord: InitVar[Dict[str, Any]] = None
    wins: int = None
    losses: int = None
    pct: float = None
    records: Dict[Any, Any] = field(default_factory=dict)
    divisionLeader: bool = None

    def __post_init__(self, leagueRecord: Dict[str, Any]):
        if leagueRecord:
            pct = leagueRecord.get('pct')
            if pct:
                self.pct = float(pct)

        if not self.wins and leagueRecord.get('wins'):
            self.wins = leagueRecord.get('wins')
        if not self.losses and leagueRecord.get('losses'):
            self.losses = leagueRecord.get('losses')


@dataclass
class CurrentTeam(Team):
    record: Union[Record, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        self.record = Record(**self.record)

@dataclass
class TeamBoxScore:
    team: Union[CurrentTeam, Dict[str, Any]] = field(default_factory=dict)
    teamStats: Dict[str, Any] = field(default_factory=dict)
    players: Dict[str, Any] = field(default_factory=dict)
    batters: List[int] = field(default_factory=list)
    pitchers: List[int] = field(default_factory=list)
    bench: List[int] = field(default_factory=list)
    bullpen: List[int] = field(default_factory=list)
    battingOrder: List[int] = field(default_factory=list)
    info: List[Dict[str, Any]] = field(default_factory=list)
    note: List[Union[Note, Dict[str, Any]]] = field(default_factory=list)

    def __post_init__(self):
        self.note = [
            Note(**note)
            for note
            in self.note
        ]
        self.team = CurrentTeam(**self.team)
