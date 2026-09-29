risk_thresholds = (25, 50, 75)

print(f"First Threshold: {risk_thresholds[0]}")
print(f"Last Threshold: {risk_thresholds[-1]}\n")

for threshold in risk_thresholds:
    print(f"{threshold}")

try:
    risk_thresholds[3] = 100
    risk_thresholds[0] = 0
except:
    print(f"Tuples are not mutable.")

    print(f"TypeError: 'tuple' object does not support item assignment. This was the error given from python without try/except block.")

print(risk_thresholds)