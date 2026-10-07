import json

from risk_utils import classify_risk, calculate_risk

with open("week02/moderation_cases.json", "r") as f:
    users = json.load(f)


def process_user(user):
        

        score = calculate_risk(user["reports"], user["warnings"], user["bans"])

        level = classify_risk(score)

        return f"User {user['id']} has {score} score and risk level is {level}."

for user in users:

    user_data = process_user(user)
    
    print(user_data)
