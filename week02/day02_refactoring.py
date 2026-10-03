import json

from risk_utils import classify_risk, calculate_risk

with open("week02/moderation_cases.json", "r") as f:
    users = json.load(f)

def proocess_user(name, score, level):
    return f"{name} has {score} score and risk level is {level}."


for user in users:
    

        score = calculate_risk(user["reports"], user["warnings"], user["bans"])

        level = classify_risk(score)

        message = proocess_user(
                        user["username"],
                        score,
                        level
                    )
        print(message)
