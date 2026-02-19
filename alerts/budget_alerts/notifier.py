import boto3
import os
from dotenv import load_dotenv

load_dotenv()

class AlertNotifier:
    """
    Sends alerts using AWS SNS
    """

    def __init__(self):
        self.sns = boto3.client("sns", region_name=os.getenv("AWS_REGION"))
        self.topic_arn = os.getenv("SNS_TOPIC_ARN")

    def send_alert(self, subject, message):
        try:
            response = self.sns.publish(
                TopicArn=self.topic_arn,
                Subject=subject,
                Message=message
            )
            print("Alert sent successfully.")
            return response
        except Exception as e:
            print(f"Failed to send alert: {str(e)}")
