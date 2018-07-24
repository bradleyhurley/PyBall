from dataclasses import dataclass


@dataclass(order=False)
class PrimaryPosition:
    code: str
    name: str
    type: str
    abbreviation: str
