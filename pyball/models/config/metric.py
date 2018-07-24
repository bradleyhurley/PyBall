from dataclasses import dataclass


@dataclass
class Metric:
    group: str = None
    name: str = None
    unit: str = None
    metricId: int = None
