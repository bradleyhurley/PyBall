from dataclasses import dataclass


@dataclass
class Position:
    code: str = None
    name: str = None
    type: str = None
    abbreviation: str = None
