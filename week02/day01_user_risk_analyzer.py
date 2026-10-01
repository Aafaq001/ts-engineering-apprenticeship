from risk_utils import classify_risk, calculate_risk
import json

with open("week02/moderation_cases.json", "r") as file:
    users = json.load(file)

    total_users = len(users)
    unique_countries = set(user["country"] for user in users)
    banned_users = [user["username"] for user in users if user.get("banned")]
    high_reported_users = [user["username"] for user in users if user.get("reports", 0) > 10]
    users_from_country = {user["country"]: len([u for u in users if u["country"] == user["country"]])
                        for user in users
                        }
    user_risk_scores = {user["username"] : calculate_risk(user.get("reports", 0), user.get("warnings", 0), user.get("bans", 0))
                        for user in users
                        }
    max_score = -1
    max_score_user = None
    for user, score in user_risk_scores.items():
        if score > max_score:
            max_score = score
            max_score_user = user
    highest_risk_user = {max_score_user: max_score}
    average_reports = sum(user.get("reports", 0) for user in users) / total_users
    banned_countries = {user["country"] for user in users if user.get("banned")}
    unbanned_countries = {user["country"] for user in users if not user.get("banned")}
    common_countries = banned_countries & unbanned_countries


print(f"Total users: {total_users}\n")
print(f"Unique countries: {len(unique_countries)}\n")
print(f"Banned users: {banned_users}\n")
print(f"Users with more than 10 reports: {high_reported_users}\n")
print(f"Users from each country: {users_from_country}\n")
print(f"User risk scores: {user_risk_scores}\n")
print(f"Highest risk user: {highest_risk_user}")
print(f"Average reports per user: {average_reports}\n")
print(f"Banned countries: {banned_countries}")
print(f"Unbanned countries: {unbanned_countries}")
print(f"Common countries: {common_countries}\n")