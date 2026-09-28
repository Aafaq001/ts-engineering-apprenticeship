from day07_risk_utils import calculate_risk, classify_risk
from user_dataset_analyzer_v2 import users

def print_result(score: int, level: str) -> None:
    """Print the risk score and risk level."""
    print(f"Risk Score: {score}")
    print(f"Risk Level: {level}")

for user in users:
    score = calculate_risk(user["reports"], user["warnings"], user["bans"])
    level = classify_risk(score)
    print_result(score, level)