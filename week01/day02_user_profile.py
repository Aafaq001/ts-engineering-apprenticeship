print("=========   USER  PROFILE   =========")

username = input("Username: ")
age = int(input("Age: "))
country = input("Country: ")
reports = int(input("Number of reports: "))

print("Username: ", username)
print("Age: ", age)
print("Country: ", country)
print("Reports: ", reports)
print("Reports per week: ", reports * 7)
print("reports per month: ", reports * 30)

print("=====================================")