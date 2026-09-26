users = [
    {
        "id": 1,
        "username": "alex_dev",
        "country": "Canada",
        "reports": 4,
        "warnings": 2,
        "bans": 1,
        "banned": False
    },
    {
        "id": 2,
        "username": "samira_tech",
        "country": "Pakistan",
        "reports": 8,
        "warnings": 4,
        "bans": 0,
        "banned": False
    },
    {
        "id": 3,
        "username": "mike_codes",
        "country": "United States",
        "reports": 16,
        "warnings": 6,
        "bans": 2,
        "banned": True
    },
    {
        "id": 4,
        "username": "luna_writer",
        "country": "United Kingdom",
        "reports": 0,
        "warnings": 0,
        "bans": 0,
        "banned": False
    },
    {
        "id": 5,
        "username": "daniel_x",
        "country": "Germany",
        "reports": 16,
        "warnings": 6,
        "bans": 2,
        "banned": False
    },
    {
        "id": 6,
        "username": "noor_dev",
        "country": "Pakistan",
        "reports": 18,
        "warnings": 8,
        "bans": 4,
        "banned": True
    },
    {
        "id": 7,
        "username": "emma_designs",
        "country": "Australia",
        "reports": 3,
        "warnings": 1,
        "bans": 0,
        "banned": False
    },
    {
        "id": 8,
        "username": "ryan_tech",
        "country": "United States",
        "reports": 12,
        "warnings": 4,
        "bans": 2,
        "banned": True
    },
    {
        "id": 9,
        "username": "sofia_codes",
        "country": "Spain",
        "reports": 13,
        "warnings": 3,
        "bans": 1,
        "banned": False
    },
    {
        "id": 10,
        "username": "omar_builder",
        "country": "United Arab Emirates",
        "reports": 14,
        "warnings": 4,
        "bans": 2,
        "banned": True
    },
    {
        "id": 11,
        "username": "mia_python",
        "country": "France",
        "reports": 4,
        "warnings": 1,
        "bans": 0,
        "banned": False
    },
    {
        "id": 12,
        "username": "ethan_dev",
        "country": "Japan",
        "reports": 18,
        "warnings": 6,
        "bans": 2,
        "banned": True
    }
]

report_threshold = []
risk_scores = []
low_count = medium_count = high_count = critical_count = 0
banned_users = []
users_frm_pak = []
countries = []


def get_users_above_report_threshold(reports, name):
    if reports > 10:
        report_threshold.append(name)


def get_banned_users(name, banned):
    if banned:
        banned_users.append(name)


def get_users_from_country(country, name):
    if country == "Pakistan":
        users_frm_pak.append(name)


def get_highest_reported_user(user, current_highest):
    if current_highest is None:
        return [user]
    
    if user['reports'] > current_highest[0]['reports']:
        return [user]
    elif user['reports'] == current_highest[0]['reports']:
        current_highest.append(user)
        
    return current_highest


def calculate_total_reports(current_total, reports):
    return current_total + reports


def calculate_average_reports(total_reports, user_count):
    return total_reports / user_count if user_count > 0 else 0


def calculate_risk(reports: int, warnings: int, bans: int):
    """Take reports, warnings, and bans of a user and calculate Risk score"""
    score = reports + (warnings * 5) + (bans * 10)
    risk_scores.append(score)


def classify_risk(score: int):
    """Take Risk Score and classify the severity/risk level"""
    global low_count, medium_count, high_count, critical_count
    if score <= 25:
        low_count += 1
    elif score <= 50:
        medium_count += 1
    elif score <= 75:
        high_count += 1
    else:
        critical_count += 1


highest_reported_users = None
total_reports = 0

# Process users in loop
for user in users:
    countries.append(user["country"])
    get_users_above_report_threshold(user["reports"], user["username"])
    get_banned_users(user["username"], user["banned"])
    get_users_from_country(user["country"], user["username"])
    highest_reported_users = get_highest_reported_user(user, highest_reported_users)
    total_reports = calculate_total_reports(total_reports, user["reports"])
    calculate_risk(user["reports"], user["warnings"], user["bans"])

# Post-loop calculations
average_reports = calculate_average_reports(total_reports, len(users))

for score in risk_scores:
    classify_risk(score)


# Print Output
print(f"Total Users: {len(users)}")
print(f"Unique Countries: {len(set(countries))}")
print(f"Users with more than 10 reports: {report_threshold}")
print(f"Banned Users: {banned_users}")
print(f"Users from Pakistan: {users_frm_pak}")

for u in highest_reported_users:
    print(f"Highest reported user: {u['username']}")

print(f"Total Reports: {total_reports}")
print(f"Average Reports: {average_reports:.2f}")

print(f"\nRisk Summary:\nLow: {low_count}\nMedium: {medium_count}\nHigh: {high_count}\nCritical: {critical_count}")
print(f"\nUser scores: {risk_scores}")