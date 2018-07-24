from dataclasses import dataclass, field


@dataclass
class Language:
    name: str = field(default=None)
    languageCode: str = field(default=None)
    locale: str = field(default=None)
