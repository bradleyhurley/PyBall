from dataclasses import dataclass, field


@dataclass
class Platform:
    platformCode: str = field(default=None)
    platformDescription: str = field(default=None)
