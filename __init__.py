"""
HMHS Era - Zero-API Local AI Framework
A decentralized, air-gapped AI ecosystem for edge execution.
Enhanced with HMHSFPS.dll hardware acceleration.
"""

__version__ = "1.0.0"
__author__ = "HMHS Team"
__description__ = "Advanced local-first AI framework with zero cloud dependencies and hardware acceleration"

from core.engine import HMHSEngine
from core.agent import HMHSAgent
from storage.vector_store import LocalVectorDB
from performance_monitor import PerformanceMonitor
from fps_accelerator import HMHSFPSAccelerator

__all__ = [
    "HMHSEngine",
    "HMHSAgent", 
    "LocalVectorDB",
    "PerformanceMonitor",
    "HMHSFPSAccelerator",
]

