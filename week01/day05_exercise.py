#Part 1 — List
#Exercise 01

users = ["Ali", "Sara", "John", "Hamza"]
print(f"{users[0]}")
print(f"{users[1]}")
print(f"{users[2]}")
print(f"{users[3]} \n")

print(f"{users[0]}")
print(f"{users[-1]}")

#Exercise 02
users.append("Ahmad")
users.remove("John")
users[1] = "Sarah"
print(users)

#Part 2 — indexing and slicing
#Practice

reports = [2, 5, 12, 3, 18, 1, 22]

print(f"First Element: {reports[0]}")
print(f"Last Element: {reports[-1]}")
print(f"First Three Elements: {reports[ : 3]}")
print(f"Last Three Elements: {reports[-3:]}")
print(f"elements from index 2 through 5: {reports[2:6]}")
for report in reports:
    if report % 2 == 0:
        print(f"Every 2nd element: {report}") #reports[::2] saw this logic later and understood it but i already had done this using loop

#Part 3 — Dictionaries
#Exercise 03
user = {
    "id": 1001,
    "username": "aafaq",
    "country": "Pakistan",
    "reports": 15,
    "warnings": 2,
    "banned": False
}

print(f"User name: {user['username']}")
print(f"User reports count: {user['reports']}")
user["reports"] = 20
print(f"Updated user reports count: {user['reports']}")
user["banned"] = True
print(f"Updated user banned status: {user['banned']}") 
user["risk_level"] = "HIGH"

#Part 4 — Dictionary iteration
for key, value in user.items():
    print(f"{key}-> {value} \n")

#Part 5 — Sets
countries = [
    "Pakistan",
    "UAE",
    "Pakistan",
    "USA",
    "UAE",
    "Pakistan"
]
unique_countries = set(countries)

#Exercise 4
print(f"Number of unique countries: {len(unique_countries)}")
print(f"Unique countries: {unique_countries}")
print(f"Is Pakistan in the list? {'Pakistan' in unique_countries}")
print(f"Is Canada in the list? {'Canada' in unique_countries} \n")

#Part 6 — Tuples
user_location = ("Pakistan", "Islamabad")

print(f"Country: {user_location[0]}")
print(f"City: {user_location[1]}")

#user_location[0] = "USA" 
#print(f"Updated Country: {user_location[0]}") #threw error error because tuples are immutable

#Part 7 — Nested data

#already had a list name users so named it loggers
loggers = [
    {
        "id": 1,
        "name": "Ali",
        "country": "Pakistan",
        "reports": 12,
        "banned": False
    },
    {
        "id": 2,
        "name": "Sara",
        "country": "UAE",
        "reports": 4,
        "banned": True
    },
    {
        "id": 3,
        "name": "John",
        "country": "USA",
        "reports": 20,
        "banned": False
    }
]

high_reported_loggers = []
banned_users = []
no_reports = []

print(f"Ali's name is: {loggers[0]['name']}")
print(f"{loggers[1]['name']} lives in: {loggers[1]['country']}")
print(f"{loggers[2]['name']} have {loggers[2]['reports']} reports.")
print(f"Is Sara banned? { 'Yes' if loggers[1]['banned'] == True else 'No' }")

for logger in loggers:
    if logger['reports'] > 10:
        high_reported_loggers.append(logger['name'])
    elif logger['reports'] == 0:
        no_reports.append(logger['name'])
    if logger['banned'] == True:
        banned_users.append(logger['name'])
    

    print(f"{logger['name']} -> {logger['country']} -> {logger['reports']}")
    
#Part 8 — Filtering
#Exercise 5

print(f"users with reports more than 10: {high_reported_loggers}")


#Exercise 6

print(f"Banned users: {banned_users}")

#Exercise 7
if len(no_reports) == 0:
    print("There is no such user with zero reports")
else:
    print(f"Users with Zero Reports: {no_reports}")