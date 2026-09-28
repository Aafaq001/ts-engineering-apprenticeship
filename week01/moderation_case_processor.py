import json

with open("week01/moderation_cases.json", "r") as file:
    users = json.load(file)

def validate_case(case):
    if (case["warnings"] < 0 or case["reports"] < 0 or case["bans"] < 0):
        raise ValueError("Values cannot be negative.")
    if case["username"] == "":
        raise ValueError("Username cannot be empty.")
    else:
        return True

def calculate_risk(user):
     return user['reports'] + (user['warnings'] * 5) + (user['bans'] * 10)

def classify_risk(score):
    if score <= 25:
        return "LOW"
    elif score <= 50:
        return "MEDIUM"
    elif score <= 75:
        return "HIGH"
    else:
        return "CRITICAL"

results = []

for user in users:
    try:
        if validate_case(user):
            risk_score = calculate_risk(user)
            risk_level = classify_risk(risk_score)
            print(f"User: {user["username"]}\nRisk Score: {risk_score}\nRisk Level: {risk_level}\n")
            user_results = {
                    "id": user["id"],
                    "username": user["username"],
                    "risk_score": risk_score,
                    "risk_level": risk_level,
                }
            results.append(user_results)
    except ValueError as e:
        print(f"Skipping profile for {user.get('username', 'Unknown')} due to error: {e}")

with open("week01/moderation_results.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

print("Export complete! Generated 'week01/moderation_results.json'")

