from dataclasses import dataclass, field


@dataclass
class Position:
    shortName: str = field(default=None)
    fullName: str = field(default=None)
    abbrev: str = field(default=None)
    code: str = field(default=None)
    type: str = field(default=None)
    outfield: bool = field(default=None)
    pitcher: bool = field(default=None)
    fielder: bool = field(default=None)
    displayName: str = field(default=None)
    formalName: str = field(default=None)
