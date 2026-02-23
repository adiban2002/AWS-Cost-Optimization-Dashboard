from typing import Dict, List
import pandas as pd


class CostAnalyzer:

    def __init__(self, ce_response: Dict):
        self.ce_response = ce_response

    def extract_service_costs(self) -> pd.DataFrame:
        records: List[Dict] = []

        results = self.ce_response.get("ResultsByTime", [])

        for time_block in results:
            groups = time_block.get("Groups", [])
            for group in groups:
                service_name = group["Keys"][0]
                cost_amount = float(
                    group["Metrics"]["UnblendedCost"]["Amount"]
                )

                records.append(
                    {
                        "service": service_name,
                        "cost_usd": cost_amount,
                    }
                )

        df = pd.DataFrame(records)

        if df.empty:
            return df

        
        df = (
            df.groupby("service", as_index=False)
              .sum()
              .sort_values("cost_usd", ascending=False)
        )

        return df

    def get_total_cost(self) -> float:
        df = self.extract_service_costs()
        if df.empty:
            return 0.0

        return round(df["cost_usd"].sum(), 6)

    def get_top_services(self, top_n: int = 5) -> pd.DataFrame:
        df = self.extract_service_costs()
        return df.head(top_n)

if __name__ == "__main__":
    from data_source.aws_cost_explorer.cost_explorer_client import (
        CostExplorerClient
    )

    ce_client = CostExplorerClient()
    raw_cost_data = ce_client.get_last_30_days_cost()

    analyzer = CostAnalyzer(raw_cost_data)

    service_cost_df = analyzer.extract_service_costs()
    print("\nService-wise cost breakdown:")
    print(service_cost_df)

    total_cost = analyzer.get_total_cost()
    print("\nTotal AWS cost (USD):", total_cost)

    print("\nTop cost-consuming services:")
    print(analyzer.get_top_services())
