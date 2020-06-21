from dataclasses import dataclass


@dataclass
class LeagueRecord:
    wins: int = None
    losses: int = None
    pct: float = None
