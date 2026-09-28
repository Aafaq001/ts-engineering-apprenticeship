import json
from day07_risk_utils import classify_risk, calculate_risk

with open("week01/moderation_cases.json", "r") as file:
    users = json.load(file)

def validate_case(case):
    if (case["warnings"] < 0 or case["reports"] < 0 or case["bans"] < 0):
        raise ValueError("Values cannot be negative.")
    if not case.get("username"):
        raise ValueError("Username cannot be empty or missing.")
    else:
        return True


results = []

for user in users:
    try:
        if validate_case(user):
            risk_score = calculate_risk(user["reports"], user["warnings"], user["bans"])
            risk_level = classify_risk(risk_score)
            print(
                f"User: {user['username']}\n"
                f"Risk Score: {risk_score}\n"
                f"Risk Level: {risk_level}\n"
            )
            user_results = {
                    "id": user["id"],
                    "username": user["username"],
                    "risk_score": risk_score,
                    "risk_level": risk_level,
                }
            results.append(user_results)
    except ValueError as e:
        print(f"Skipping profile for user ID:{user.get('id', 'Unknown')} due to error: {e}")

with open("week01/moderation_results.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

print("Export complete! Generated 'week01/moderation_results.json'")

