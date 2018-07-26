from dataclasses import dataclass, InitVar, field
from typing import Dict, List, Any, Union

from .official import Official
from .note import Note
from .team_boxscore import TeamBoxScore


@dataclass
class BoxScore:
    copyright: InitVar[str]
    teams: InitVar[Dict[str, Any]]
    home: TeamBoxScore = None
    away: TeamBoxScore = None
    officials: List[Union[Dict[str, Any], Official]] = field(default_factory=list)
    info: List[Union[Note, Dict[str, Any]]] = field(default_factory=dict)
    pitchingNotes: List[str] = field(default_factory=list)

    def __post_init__(self, copyright: str, teams: Dict[str, Any]):
        if teams:
            self.home = TeamBoxScore(**teams.get('home'))
            self.away = TeamBoxScore(**teams.get('away'))

        self.officials = [
            Official(**official)
            for official
            in self.officials
        ]

        self.info = [
            Note(**note)
            for note
            in self.info
        ]
