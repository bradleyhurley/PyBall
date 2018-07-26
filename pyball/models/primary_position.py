from dataclasses import dataclass


@dataclass(order=False)
class PrimaryPosition:
    code: str = None
    name: str = None
    type: str = None
    abbreviation: str = None
