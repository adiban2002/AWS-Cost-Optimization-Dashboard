"""
Optimization Engine Package

This package contains modules responsible for analyzing AWS resource
utilization and generating cost optimization recommendations.
"""

from .idle_resource_detector import IdleResourceDetector
from .rightsizing import RightsizingAnalyzer
from .savings_recommendations import SavingsEstimator

__all__ = [
    "IdleResourceDetector",
    "RightsizingAnalyzer",
    "SavingsEstimator",
]
