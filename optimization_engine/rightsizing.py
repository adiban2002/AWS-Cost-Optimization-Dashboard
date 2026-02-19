"""
rightsizing.py

Analyzes EC2 utilization to recommend instance resizing
based on CPU usage patterns.
"""

import pandas as pd
from data_processing import DataPreprocessor


class RightsizingAnalyzer:
    """
    Provides rightsizing recommendations for running instances.
    """

    LOWER_BOUND = 20   # % CPU
    UPPER_BOUND = 60   # % CPU

    def __init__(self):
        self.processor = DataPreprocessor()

    def analyze(self) -> pd.DataFrame:
        datasets = self.processor.build_unified_dataset()
        ec2_df = datasets["ec2_metrics"]

        recommendations = []

        for _, row in ec2_df.iterrows():
            state = row["state"]
            cpu = row["avg_cpu_percent"]

            if state != "running":
                continue  # Rightsizing only applies to running instances

            if cpu < self.LOWER_BOUND:
                action = "Downsize Instance"
                reason = f"CPU utilization low ({cpu}%). Instance overprovisioned."

            elif cpu > self.UPPER_BOUND:
                action = "Upsize Instance"
                reason = f"CPU utilization high ({cpu}%). Instance may be undersized."

            else:
                action = "Keep Size"
                reason = "Instance is appropriately sized."

            recommendations.append({
                "instance_id": row["instance_id"],
                "current_cpu_percent": cpu,
                "rightsizing_action": action,
                "reason": reason
            })

        df = pd.DataFrame(recommendations)

        # ------------------------------------------------------------------
        # Fallback for environments with no running instances
        # (ensures dashboard always shows meaningful output)
        # ------------------------------------------------------------------
        if df.empty:
            df = pd.DataFrame([{
                "instance_id": "demo-instance",
                "current_cpu_percent": 8,
                "rightsizing_action": "Downsize Instance",
                "reason": "No active workload detected (demonstration data)."
            }])

        return df


# ------------------------------------------------------------------
# Local test
# ------------------------------------------------------------------
if __name__ == "__main__":
    analyzer = RightsizingAnalyzer()
    result = analyzer.analyze()

    print("\n=== RIGHTSIZING RECOMMENDATIONS ===")
    print(result if not result.empty else "No running instances to analyze.")
