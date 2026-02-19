import os
import boto3
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()


class EC2Client:
    def __init__(self):
        # Read regions from environment
        regions_env = os.getenv("TARGET_REGIONS", "ap-south-1")
        self.regions = [r.strip() for r in regions_env.split(",")]

    def list_instances(self):
        """
        Fetch instances from ALL configured regions
        """
        all_instances = []

        for region in self.regions:
            ec2 = boto3.client("ec2", region_name=region)

            response = ec2.describe_instances()

            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:
                    all_instances.append({
                        "instance_id": instance["InstanceId"],
                        "instance_type": instance["InstanceType"],
                        "state": instance["State"]["Name"],
                        "launch_time": str(instance["LaunchTime"]),
                        "region": region
                    })

        return all_instances

    def get_average_cpu_utilization(self, instance_id, region):
        """
        Fetch CPU utilization from the SAME region where instance exists
        """
        cloudwatch = boto3.client("cloudwatch", region_name=region)

        end_time = datetime.now(timezone.utc)
        start_time = end_time - timedelta(hours=1)

        response = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[
                {
                    "Name": "InstanceId",
                    "Value": instance_id
                }
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=["Average"]
        )

        datapoints = response["Datapoints"]

        if not datapoints:
            return 0

        avg_cpu = sum(d["Average"] for d in datapoints) / len(datapoints)
        return round(avg_cpu, 2)


if __name__ == "__main__":
    ec2_client = EC2Client()

    instances = ec2_client.list_instances()

    if not instances:
        print("No EC2 instances found.")
    else:
        print("\nEC2 Instances Across Regions:\n")

        for inst in instances:
            print(inst)

            cpu = ec2_client.get_average_cpu_utilization(
                inst["instance_id"],
                inst["region"]
            )

            print(f"Average CPU (last 1 hour): {cpu}%\n")
