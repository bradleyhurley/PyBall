from dataclasses import dataclass, field


@dataclass
class ScheduleEventType:
    code: str = field(default=None)
    name: str = field(default=None)
