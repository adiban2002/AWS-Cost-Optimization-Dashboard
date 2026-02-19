import pandas as pd
from typing import List, Dict

from data_processing import DataPreprocessor


class IdleResourceDetector:
    """
    Detects idle EC2 resources and recommends actions.
    """

    CPU_IDLE_THRESHOLD = 5       # %
    CPU_UNDERUTILIZED = 20       # %

    def __init__(self):
        self.processor = DataPreprocessor()

    def analyze(self) -> pd.DataFrame:
        """
        Run optimization analysis and return recommendations.
        """
        datasets = self.processor.build_unified_dataset()
        ec2_df = datasets["ec2_metrics"]

        recommendations: List[Dict] = []

        for _, row in ec2_df.iterrows():

            instance_id = row["instance_id"]
            state = row["state"]
            cpu = row["avg_cpu_percent"]

            if state == "stopped":
                action = "Terminate"
                reason = "Instance is stopped but storage still incurs cost."

            elif cpu < self.CPU_IDLE_THRESHOLD:
                action = "Stop"
                reason = f"CPU utilization very low ({cpu}%). Instance is idle."

            elif cpu < self.CPU_UNDERUTILIZED:
                action = "Rightsize"
                reason = f"CPU utilization moderate ({cpu}%). Consider smaller instance."

            else:
                action = "Keep Running"
                reason = "Instance utilization is healthy."

            recommendations.append({
                "instance_id": instance_id,
                "state": state,
                "avg_cpu_percent": cpu,
                "recommended_action": action,
                "reason": reason
            })

        return pd.DataFrame(recommendations)


# ------------------------------------------------------------------
# Local test
# ------------------------------------------------------------------
if __name__ == "__main__":
    detector = IdleResourceDetector()
    result = detector.analyze()

    print("\n=== OPTIMIZATION RECOMMENDATIONS ===")
    print(result)
