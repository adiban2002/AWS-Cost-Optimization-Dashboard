from .notifier import AlertNotifier


class BudgetMonitor:
    def __init__(self, threshold_amount=100):
        self.threshold = threshold_amount
        self.notifier = AlertNotifier()

    def evaluate_cost(self, total_cost, region):
        if total_cost > self.threshold:
            subject = "Budget Threshold Exceeded"

            message = f"""
Cost Alert for Region: {region}

Total Monthly Cost: ${total_cost}
Threshold Limit: ${self.threshold}

Recommendation:
Review running resources and apply optimization.
"""

            self.notifier.send_alert(subject, message)
        else:
            print("Cost within budget. No alert triggered.")
