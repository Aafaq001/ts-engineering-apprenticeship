import json
with open("week02/moderation_cases.json", "r") as f:
    users = json.load(f)

    def calculate_total_reports(users):
        total_reports = 0
        for user in users:
            total_reports += user.get("reports", 0)
        return total_reports

    total = calculate_total_reports(users)
    print(total)

def greet_user(username):
    return f"Hello, {username}!"
message = greet_user("alex_dev")
print(message)

def create_user(username, country, reports=0):

    return {
        "username": username,
        "country": country,
        "reports": reports
    }

user1 = create_user("alex", "Canada")
user2 = create_user("samira", "Pakistan", 10)
user3 = create_user(
    username="mike",
    country="Germany",
    reports=5
)

print(user1)
print(user2)
print(user3)

def classify_user(score):
    if score <= 25:
        return "LOW"
    elif score <= 50:
        return "MEDIUM"
    elif score <= 75:
        return "HIGH"
    else:
        return "CRITICAL"


def generate_risk_message(username, score):
    risk_level = classify_user(score)
    return f"{username} has a risk score of {score} which is classified as {risk_level}."

print(generate_risk_message("alex", 30))