import boto3
from datetime import date, timedelta


class CostExplorerClient:
    """
    Wrapper around AWS Cost Explorer API
    """

    def __init__(self):
        # Cost Explorer is a GLOBAL service
        self.client = boto3.client(
            "ce",
            region_name="us-east-1"
        )

    def get_last_30_days_cost(self):
        """
        Fetch service-wise cost for last 30 days
        """
        end_date = date.today()
        start_date = end_date - timedelta(days=30)

        response = self.client.get_cost_and_usage(
            TimePeriod={
                "Start": start_date.strftime("%Y-%m-%d"),
                "End": end_date.strftime("%Y-%m-%d"),
            },
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key": "SERVICE"
                }
            ]
        )

        return response


if __name__ == "__main__":
    ce = CostExplorerClient()
    data = ce.get_last_30_days_cost()
    print(data)
