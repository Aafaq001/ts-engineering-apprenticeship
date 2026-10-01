import json

with open("week01/moderation_cases.json", "r") as file:
    users = json.load(file)

    usernames = []
    countries = []
    unique_countries = set()
    banned_users = []
    user_reports_threshold = 10
    reported_users = []
    total_reports = 0
    avg_reports = 0

    for user in users:
        if not user.get("username"):
            print(f"Skipping user with ID:{user.get('id', 'Unknown')} due to missing username.")
            continue
        usernames.append(user["username"])
        countries.append(user["country"])
        unique_countries.add(user["country"])
        if user["banned"]:
            banned_users.append(user["username"])
        if user["reports"] > user_reports_threshold:
            reported_users.append(user["username"])
        total_reports += user["reports"]
            

avg_reports = total_reports / len(users)

print(f"Usernames: {usernames}\n")
print(f"Countries: {countries}\n")
print(f"Unique Countries: {unique_countries}\n")
print(f"Banned Users: {banned_users}\n")
print(f"Reported Users (more than {user_reports_threshold} reports): {reported_users}\n")
print(f"Total Reports: {total_reports}\n")
print(f"Average Reports per User: {avg_reports}")