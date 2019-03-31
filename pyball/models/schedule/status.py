from dataclasses import dataclass


@dataclass
class Status:
    abstractGameState: str = None
    codedGameState: str = None
    detailedState: str = None
    statusCode: str = None
    abstractGameCode: str = None
    startTimeTBD: bool = None
