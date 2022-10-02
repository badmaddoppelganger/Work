"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    """Data-only class with attrs:
    volume
    pistons
    """
    volume: float = None
    pistons: int = None
