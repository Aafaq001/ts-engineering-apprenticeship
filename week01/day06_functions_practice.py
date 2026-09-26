# Exercise 01

def user_name():
    print(f"Ali")
    print(f"Sara")
    print(f"John")

user_name()
user_name()
user_name()

# Exercise 02

def fun_a():
    return "result_a"
def fun_b():
    return "result_b"
print(f"{fun_a()}")
print(f"{fun_b()}")

# Exercise 03

def calculate_risk(reports, warnings, bans):
    print(f"{(reports) + (warnings * 5) + (bans*10)}")

calculate_risk(17,8,3)

# Exercise 04

def calculate_risk(reports : int, warnings : int, bans : int) -> int:

    """Take reports, warnings, and bans of a user and calculate Risk score"""

    return (reports) + (warnings * 5) + (bans*10)
def classify_risk(risk_score : int) -> str:

    """Take Risk Score and classify the severity/risk level"""

    if risk_score <= 25:
        return "Low"
    elif risk_score <= 50:
        return "Medium"
    elif risk_score <= 75:
        return "High"
    else:
        return "Critical"

risk_score = calculate_risk(17,8,3)
risk_level = classify_risk(risk_score)

print(f"Risk Score: {risk_score} \nRisk Level: {risk_level}")

# Exercise 05

status = "working"

def home():
    status = "Relaxing"
    print(f'I am {status}')
home()
print(f'I am {status}')

# Exercise 06

def name(fname, lname = "Doe"):
    print(f"Hello, {fname} {lname}")

name("john")

# Exercise 07

def calculate_risk(reports, warnings, bans):

    """Take reports, warnings, and bans of a user and calculate Risk score"""

    return (reports) + (warnings * 5) + (bans*10)

risk1 = calculate_risk(10,5,1)
print(f"Positionally: {risk1}")

risk2 = calculate_risk(reports=10, warnings=10, bans=2)
print(f"Keyword argument: {risk2}")

# Exercise 08 and 09

#defined and user in the earlier functions

