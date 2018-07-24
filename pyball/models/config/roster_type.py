from dataclasses import dataclass


@dataclass
class RosterType:
    description: str = None
    lookupName: str = None
    parameter: str = None
