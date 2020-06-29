from dataclasses import dataclass


@dataclass
class Position:
    shortName: str = None
    fullName: str = None
    abbrev: str = None
    code: str = None
    type: str = None
    outfield: bool = None
    pitcher: bool = None
    fielder: bool = None
    displayName: str = None
    formalName: str = None  # noqa: E701
    gamePosition: bool = None
