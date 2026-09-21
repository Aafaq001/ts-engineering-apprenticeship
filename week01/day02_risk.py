reports = int(input("reports: "))
warnings = int(input("warnings: "))
previous_bans = int(input("previous bans: "))

risk_score = (reports * 2) + (warnings * 5) + (previous_bans * 10)
print(f"Risk Score: {risk_score}")