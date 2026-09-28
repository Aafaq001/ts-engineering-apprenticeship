#Exercises
try:
    def calculate_risk(warnings, reports, bans):
        if warnings >= 0 or reports >= 0 or bans >= 0:
            raise ValueError("values cannot be negative")
        return reports + (warnings * 5) + (bans * 10)

    username = input("Enter Username: ")
    reports = int(input("Enter reports: "))
    warnings = int(input("Enter warning: "))
    bans = int(input("Enter Bans: "))
except ValueError:
    print("Value must be a number/valid.")
else:
    print(f"{username}\nReports: {reports} Warnings: {warnings} Bans: {bans}")
finally:
    print("Program finished.")

score = calculate_risk(warnings, reports, bans)
print(f"{username}'s Risk score: {score}")
