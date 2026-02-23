import pandas as pd
from typing import List, Dict

from data_source.aws_cost_explorer.cost_explorer_client import CostExplorerClient
from data_processing.cost_analysis import CostAnalyzer
from data_source.ec2_client import EC2Client


class DataPreprocessor:

    def __init__(self):
        self.ce_client = CostExplorerClient()
        self.ec2_client = EC2Client()

    def build_ec2_dataset(self) -> pd.DataFrame:
        instances = self.ec2_client.list_instances()

        records: List[Dict] = []

        for inst in instances:
            region = inst["region"]

            cpu_avg = self.ec2_client.get_average_cpu_utilization(
                inst["instance_id"],
                region
            )

            records.append(
                {
                    "instance_id": inst["instance_id"],
                    "instance_type": inst["instance_type"],
                    "state": inst["state"],
                    "region": region,
                    "avg_cpu_percent": cpu_avg,
                }
            )

        return pd.DataFrame(records)

    def build_cost_dataset(self) -> pd.DataFrame:
        raw_cost_data = self.ce_client.get_last_30_days_cost()
        analyzer = CostAnalyzer(raw_cost_data)

        return analyzer.extract_service_costs()

    def build_unified_dataset(self) -> Dict[str, pd.DataFrame]:
        ec2_df = self.build_ec2_dataset()
        cost_df = self.build_cost_dataset()

        return {
            "ec2_metrics": ec2_df,
            "service_costs": cost_df,
        }
if __name__ == "__main__":
    processor = DataPreprocessor()
    datasets = processor.build_unified_dataset()

    print("\n=== EC2 METRICS DATASET ===")
    print(datasets["ec2_metrics"])

    print("\n=== SERVICE COST DATASET ===")
    print(datasets["service_costs"])
