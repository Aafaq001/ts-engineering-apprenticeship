import json
from risk_utils import calculate_risk, classify_risk

# Load user data from the JSON file
with open("week02/moderation_cases.json", "r") as f:
    users = json.load(f)

def process_user(user):
    """Calculate risk metrics and format a summary message for a user."""
    score = calculate_risk(user["reports"], user["warnings"], user["bans"])
    level = classify_risk(score)
    return f"User {user['id']} has {score} score and risk level is {level}."

# Process and print risk details for every user
for user in users:
    user_data = process_user(user)
    print(user_data)
