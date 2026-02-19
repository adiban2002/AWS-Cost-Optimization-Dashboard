import pandas as pd

from optimization_engine.idle_resource_detector import IdleResourceDetector


class SavingsEstimator:
    """
    Maps instance types to estimated pricing and calculates savings.
    """

    # Approximate On-Demand hourly pricing (USD) for ap-south-1
    INSTANCE_PRICING = {
        "t2.micro": 0.0116,
        "t2.small": 0.023,
        "t2.medium": 0.0464,
    }

    HOURS_PER_MONTH = 24 * 30  # Simplified monthly estimate

    def __init__(self):
        self.detector = IdleResourceDetector()

    def estimate(self) -> pd.DataFrame:
        """
        Generate savings estimation report.
        """
        recommendations_df = self.detector.analyze()

        savings_records = []

        for _, row in recommendations_df.iterrows():
            instance_type = "t2.micro"  # from preprocessing (can generalize later)
            action = row["recommended_action"]

            hourly_price = self.INSTANCE_PRICING.get(instance_type, 0)
            monthly_cost = hourly_price * self.HOURS_PER_MONTH

            if action in ["Terminate", "Stop"]:
                estimated_savings = monthly_cost
            elif action == "Rightsize":
                estimated_savings = monthly_cost * 0.5  # assume 50% saving
            else:
                estimated_savings = 0

            savings_records.append({
                "instance_id": row["instance_id"],
                "recommended_action": action,
                "estimated_monthly_cost_usd": round(monthly_cost, 2),
                "estimated_monthly_savings_usd": round(estimated_savings, 2)
            })

        return pd.DataFrame(savings_records)


# ------------------------------------------------------------------
# Local test
# ------------------------------------------------------------------
if __name__ == "__main__":
    estimator = SavingsEstimator()
    report = estimator.estimate()

    print("\n=== SAVINGS ESTIMATION REPORT ===")
    print(report)
