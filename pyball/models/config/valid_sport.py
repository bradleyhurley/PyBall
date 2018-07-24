from dataclasses import dataclass, field


@dataclass
class ValidSport:
    name: str = field(default=None)
    explictModeOn: bool = field(default=None)
