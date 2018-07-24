from dataclasses import dataclass


@dataclass
class GameStatus:
    abstractGameState: str = None
    codedGameState: str = None
    detailedState: str = None
    statusCode: int = None
    reason: int = None
    abstractGameCode: int = None
