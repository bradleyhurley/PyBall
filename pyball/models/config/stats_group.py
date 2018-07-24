from dataclasses import dataclass, field


@dataclass
class StatsGroup:
    displayName: str = field(default=None)
