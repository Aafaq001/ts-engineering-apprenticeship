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

countries = []
userreports = []
highest_reported = {
    'hrepname': users[0]['username'],
    'hrepreports': users[0]['reports']
    }

bannedUsers = []
usersfrmPak = []
totalReports = 0
userwnoReports = []
riskSummary = []
lowCount = mediumCount = highCount = criticalCount = 0
    
for user in users:
    countries.append(user['country'])
    if user['reports'] > 10:
        userreports.append(user['username'])
    if user['reports'] > highest_reported['hrepreports']:
        highest_reported['hrepname'] = user["username"]
        highest_reported["hrepreports"] = user["reports"]
    if user["country"] == 'Pakistan':
        usersfrmPak.append(user["username"])
    if user["banned"] == True:
        bannedUsers.append(user["username"])
    if user["reports"] == 0:
        userwnoReports.append(user["username"])
    #userrisk.update(user)
    
    riskSummary.append((user["reports"] * 1) + (user["warnings"] * 5) + (user["bans"] * 10))
    

    totalReports = totalReports + user['reports']
    

#1
print(f"Total Users: {len(users)}")

#2
print(f"Unique Countries: {len(set(countries))}")

#3
print(f"Users with more than 10 reports: {userreports}")

#4
print(f"Banned Users: {bannedUsers}")

#5
print(f"Users from Pakistan: {usersfrmPak}")

#6
print(f"Highest reported user: {highest_reported['hrepname']}")

#7
print(f"Total Reports: {totalReports}")

#8
print(f"Average Reports: {totalReports/len(users)}")

#9
print(f"Users with no Reports: {userwnoReports}")

#10

for risk in riskSummary:
    if risk <= 25:
        lowCount += 1
    elif risk <= 50:
        mediumCount += 1
    elif risk <= 75:
        highCount += 1
    else:
        criticalCount += 1

print(f"Risk Summary: \nLow:  {lowCount} \nMedium:  {mediumCount} \nHigh:  {highCount} \nCritical:  {criticalCount} \n")