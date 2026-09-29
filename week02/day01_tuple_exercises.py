risk_thresholds = (25, 50, 75)

print(f"First Threshold: {risk_thresholds[0]}")
print(f"Last Threshold: {risk_thresholds[-1]}\n")

for threshold in risk_thresholds:
    print(f"{threshold}")

    risk_thresholds[0] = 10

print(risk_thresholds)