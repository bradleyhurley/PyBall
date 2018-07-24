from dataclasses import dataclass, field


@dataclass
class SituationCode:
    code: str = field(default=None)
    sortOrder: int = field(default=None)
    navigationMenu: str = field(default=None)
    description: str = field(default=None)
    team: bool = field(default=None)
    batting: bool = field(default=None)
    fielding: bool = field(default=None)
