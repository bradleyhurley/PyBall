from dataclasses import dataclass


@dataclass
class Sport:
    id: int = None
    code: str = None
    link: str = None
    name: str = None
    abbreviation: str = None
    sortOrder: int = None
    activeStatus: bool = None
