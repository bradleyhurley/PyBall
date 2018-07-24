from dataclasses import dataclass, field


@dataclass
class School:
    name: str = field(default=None)
    schoolClass: str = field(default=None)
    city: str = field(default=None)
    country: str = field(default=None)
    state: str = field(default=None)
