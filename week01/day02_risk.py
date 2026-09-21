reports = int(input("reports: "))
warning = int(input("warning: "))
previous_bans = int(input("previous bans: "))

risk_score = (reports * 2) + (warning * 5) + (previous_bans * 10)
print("Risk Score: ", risk_score)