reported_users = {
    "alex_dev",
    "samira_tech",
    "mike_codes",
    "noor_dev"
}

banned_users = {
    "mike_codes",
    "noor_dev",
    "omar_builder"
}

users_in_both_sets = reported_users | banned_users
print(f"Users in either sets: {users_in_both_sets}")

users_reported_and_banned = reported_users & banned_users
print(f"Users both reported and banned: {users_reported_and_banned}")

users_reported_not_banned = reported_users - banned_users
print(f"Users reported not banned: {users_reported_not_banned}")

users_banned_not_reported = banned_users - reported_users
print(f"Users banned not reported: {users_banned_not_reported}")

checking_banned_status = "mike_codes" in banned_users
print(f"Check mike_codes banned status: {checking_banned_status}")

banned_users.add("luna_writer")
print(f"Banned users set: {banned_users}")