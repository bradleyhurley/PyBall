from dataclasses import dataclass, field


@dataclass
class StatsType:
    displayName: str = field(default=None)
