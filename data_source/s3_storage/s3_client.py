import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Create S3 client
s3_client = boto3.client("s3", region_name=AWS_REGION)


def upload_file_to_s3(file_content: str, object_key: str):
    """
    Uploads content to S3 bucket.

    :param file_content: JSON/string data to upload
    :param object_key: Path inside bucket (e.g. reports/2026-02-16/report.json)
    """
    try:
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=object_key,
            Body=file_content.encode("utf-8"),
            ContentType="application/json"
        )
        print(f"Uploaded successfully → {object_key}")

    except Exception as e:
        print(f"S3 Upload Failed: {str(e)}")
