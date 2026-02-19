"""
AWS Cost Explorer data source package.

This package is responsible for fetching raw cost and usage
data from AWS Cost Explorer using boto3.
"""

from .cost_explorer_client import CostExplorerClient

__all__ = ["CostExplorerClient"]
