from dataclasses import dataclass, field


@dataclass
class League:
    id: int = field(default=None)
    link: str = field(default=None)
