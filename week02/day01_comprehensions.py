import json
with open("week01/moderation_cases.json", "r") as file:
    users = json.load(file)

    usernames = [user["username"] for user in users if user.get("username")]
    countries = [user["country"] for user in users]
    unique_countries = {user["country"] for user in users}
    banned_users = [user["username"] for user in users if user.get("username") and user["banned"]]
    reports = [user["reports"] for user in users]
    upper_case_usernames = [user["username"].upper() for user in users if user.get("username")]

print(f"Usernames: {usernames}\n")
print(f"Countries: {countries}\n")
print(f"Unique Countries: {unique_countries}\n")
print(f"Banned Users: {banned_users}\n")
print(f"Reports: {reports}\n")
print(f"Upper Case Usernames: {upper_case_usernames}\n")