reports = int(input("Number of reports: "))
warnings = int(input("Number of warnings: "))
previous_bans = int(input("Number of previous bans: "))

risk_score = (reports * 2) + (warnings * 5) + (previous_bans * 10)

if risk_score <= 25:
    print(f"Risk Score: {risk_score} - Low Risk")
elif risk_score <= 50:
    print(f"Risk Score: {risk_score} - Medium Risk")
elif risk_score <= 75:
    print(f"Risk Score: {risk_score} - High Risk")
else:
    print(f"Risk Score: {risk_score} - Critical")