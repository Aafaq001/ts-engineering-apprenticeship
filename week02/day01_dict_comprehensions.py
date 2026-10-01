from week01.day07_risk_utils import calculate_risk
import json

with open("week01/moderation_cases.json", "r") as file:
    users = json.load(file)

    user_reports = {
        user["username"]: user["reports"]
        for user in users if user.get("username")
    }
    risk_scores = {
        user["username"]: calculate_risk(user["reports"], user["warnings"], user["bans"])
        for user in users if user.get("username")
    }
    user_country = {
        user["username"]: user["country"]
        for user in users if user.get("username")
    }
    banned_users = {
        user["username"]: calculate_risk(user["reports"], user["warnings"], user["bans"])
        for user in users if user.get("username") and user["banned"]
    }


print(f"User Reports: {user_reports}\n")
print(f"Risk Scores: {risk_scores}\n")
print(f"User Countries: {user_country}\n")
print(f"Banned Users: {banned_users}\n")