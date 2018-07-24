from dataclasses import dataclass, field


@dataclass
class GameStatus:
    abstractGameState: str = field(default=None)
    codedGameState: str = field(default=None)
    detailedState: str = field(default=None)
    statusCode: int = field(default=None)
    reason: int = field(default=None)
    abstractGameCode: int = field(default=None)
