from dataclasses import dataclass, field


@dataclass
class Home:
    city: str = field(default=None)
    country: str = field(default=None)
    state: str = field(default=None)
