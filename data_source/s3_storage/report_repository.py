import json
from datetime import datetime
from .s3_client import upload_file_to_s3


def save_cost_report(report_data: dict):
    """
    Saves processed cost optimization report to S3
    """

    today = datetime.now().strftime("%Y-%m-%d")
    object_key = f"reports/{today}/cost_report.json"

    json_data = json.dumps(report_data, indent=4)

    upload_file_to_s3(json_data, object_key)

    return object_key
