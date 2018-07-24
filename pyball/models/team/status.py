from dataclasses import dataclass


@dataclass
class Status:
    code: str = None
    description: str = None
