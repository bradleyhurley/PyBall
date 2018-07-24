from dataclasses import dataclass, field


@dataclass
class Sport:
    id: int = field(default=None)
    link: str = field(default=None)
