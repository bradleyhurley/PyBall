from dataclasses import dataclass, field


@dataclass
class Metric:
    group: str = field(default=None)
    name: str = field(default=None)
    unit: str = field(default=None)
    metricId: int = field(default=None)
