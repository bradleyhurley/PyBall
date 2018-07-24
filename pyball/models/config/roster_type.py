from dataclasses import dataclass, field


@dataclass
class RosterType:
    description: str = field(default=None)
    lookupName: str = field(default=None)
    parameter: str = field(default=None)
