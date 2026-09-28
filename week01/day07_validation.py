def calculate_risk(warnings, reports, bans):        
    return reports + (warnings * 5) + (bans * 10)

def validate_user_data(reports, warnings, bans):
    if warnings < 0 or reports < 0 or bans < 0:
        raise ValueError("Values cannot be negative.")
    else:
        return True

try:
    username = input("Enter Username: ")
    reports = int(input("Enter reports: "))
    warnings = int(input("Enter warning: "))
    bans = int(input("Enter Bans: "))
    
except ValueError:
    print("Please enter a valid number.")

else:
    # This block ONLY runs if no exception occurred above
    try:
        validation = validate_user_data(reports, warnings, bans)
        if validation:
            score = calculate_risk(warnings, reports, bans)
        print(f"\n{username}")
        print(f"Reports: {reports} | Warnings: {warnings} | Bans: {bans}")
        print(f"{username}'s Risk score: {score}")
    except ValueError as e:
        print(f"Error: {e}")

finally:
    print("Program finished.")
