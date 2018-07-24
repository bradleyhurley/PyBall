from dataclasses import dataclass, field


@dataclass
class GameType:
    id: str = field(default=None)
    description: str = field(default=None)
