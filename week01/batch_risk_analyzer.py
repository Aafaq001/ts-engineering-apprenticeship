users = [
    {"name": "Ali", "reports": 3, "warnings": 1, "bans": 0},
    {"name": "Sara", "reports": 15, "warnings": 4, "bans": 2},
    {"name": "John", "reports": 25, "warnings": 5, "bans": 3},
]
risk_scores = []
total_risk_scores = 0
average_risk_scores = 0
high_risk_users = 0
critical_users = 0
highest_risk_user = ""
highest_score = 0

print("=========== Risk Report ===========")

for user in users:
    risk_score = (user["reports"] * 1) + (user["warnings"] * 5) + (user["bans"] * 10)
    total_risk_scores += risk_score
    average_risk_scores = round(total_risk_scores/len(users))
    risk_scores.append(risk_score)
    risk_level = ""
    if risk_score <= 25:
        risk_level = "LOW"
    elif risk_score <= 50:
        risk_level = "MEDIUM"   
    elif risk_score <= 75:
       risk_level = "HIGH"
       high_risk_users += 1
    else:
       risk_level = "CRITICAL"
       critical_users += 1 
    if risk_score > highest_score:
        highest_score = risk_score
        highest_risk_user = user["name"] 
    print(f"User: {user['name']}")
    print(f"Risk Score: {risk_score}")
    print(f"Risk Level: {risk_level} \n")


highest_risk_user = user["name"]
print(f"Total users: {len(users)}")
print(f"High-risk Users: {high_risk_users}")
print(f"Critical Users: {critical_users}")
print(f"Average Risk Score: {average_risk_scores}")
print(f"Highest Risk User: {highest_risk_user}")