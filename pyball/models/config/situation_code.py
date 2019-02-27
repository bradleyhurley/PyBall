from dataclasses import dataclass


@dataclass
class SituationCode:
    code: str = None
    sortOrder: int = None
    navigationMenu: str = None
    description: str = None
    team: bool = None
    batting: bool = None
    fielding: bool = None
    pitching: bool = None
