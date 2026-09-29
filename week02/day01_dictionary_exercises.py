from week01.day07_risk_utils import calculate_risk

user = {
    "id": 101,
    "username": "alex_dev",
    "country": "Canada",
    "reports": 12,
    "warnings": 3,
    "bans": 1,
    "banned": False
}

print(f"Username: {user['username']}")
print(f"Country: {user['country']}")
user["reports"] += 3
user["banned"] = True
risk_score = calculate_risk(user["reports"], user["warnings"], user["bans"])
user["risk_score"] = risk_score
user.get("email")
print(f"Keys: {user.keys}")
print(f"Values: {user.values}")
for key, value in user.items():
    print(f"Key: {key} -> Value: {value}")