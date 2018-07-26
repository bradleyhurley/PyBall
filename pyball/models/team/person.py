from dataclasses import dataclass


@dataclass
class Person:
    id: int = None
    link: str = None
    fullName: str = None
