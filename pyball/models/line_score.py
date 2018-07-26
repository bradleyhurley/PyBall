from dataclasses import dataclass


@dataclass
class LineScore:
    runs: int = None
    hits: int = None
    errors: int = None
