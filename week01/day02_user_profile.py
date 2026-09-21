print("=========   USER  PROFILE   =========")

username = input("Username: ")
age = int(input("Age: "))
country = input("Country: ")
reports = int(input("Number of reports per day: "))

print(f"Username: {username}")
print(f"Age: {age}")
print(f"Country: {country}")
print(f"Reports: {reports}")
print(f"Reports per week: {reports * 7}")
print(f"Reports per month: {reports * 30}")

print("=====================================")