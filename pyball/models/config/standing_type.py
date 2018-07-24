from dataclasses import dataclass, field


@dataclass
class StandingType:
    name: str = field(default=None)
    description: str = field(default=None)
