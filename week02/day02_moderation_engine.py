import json
from risk_utils import calculate_risk, classify_risk

with open("week02/moderation_cases.json", "r") as f:
    users = json.load(f)

def validate_user_data(user):
    required_fields = ["username", "country", "reports", "warnings", "bans"]
    
    #Check for missing fields
    for field in required_fields:
        if field not in user:
            raise ValueError(f"Missing required field: {field}")
            
    # Validate rules: username must not be empty string or non-string
    if not isinstance(user.get("username"), str) or not user.get("username").strip():
        raise ValueError("username must not be empty")
        
    # Validate rules: country must not be empty string or non-string
    if not isinstance(user.get("country"), str) or not user.get("country").strip():
        raise ValueError("country must not be empty")
        
    # Validate rules: reports, warnings, and bans must be >= 0
    if not isinstance(user.get("reports"), (int, float)) or user.get("reports") < 0:
        raise ValueError("reports must be >= 0")
        
    if not isinstance(user.get("warnings"), (int, float)) or user.get("warnings") < 0:
        raise ValueError("warnings must be >= 0")
        
    if not isinstance(user.get("bans"), (int, float)) or user.get("bans") < 0:
        raise ValueError("bans must be >= 0")
        
    # If all checks pass
    return True

def generate_risk_message(name, score, level):
    return f"{name} has {score} score and risk level is {level} Valid."

total_users = 0
valid_users = 0
invalid_users = 0

low_risks = medium_risks = high_risks = 0
risks = []
total_score = avg_score = 0

def find_highest_risk_user(score, name, highest_score, highest_risk_user):
    if score > highest_score:
        highest_score = score
        highest_risk_user = name
    return highest_score, highest_risk_user

highest_score = -1
highest_risk_user = None

for user in users:
    total_users += 1
    try:
        if validate_user_data(user):
            valid_users += 1
            score = calculate_risk(user["reports"], user["warnings"], user["bans"])
            level = classify_risk(score)
            risks.append(level)
            total_score = total_score + score
            highest_score, highest_risk_user = find_highest_risk_user(score, user["username"], highest_score, highest_risk_user)
            

            message = generate_risk_message(
                user["username"],
                score,
                level,
            )
            print(message)
    except ValueError as e:
        invalid_users += 1
        print(f"User ID {user['id']} ({user.get('username') or 'EMPTY'}): INVALID -> {e}")   

for risk in risks:
    if risk == "low":
        low_risks += 1
    elif risk == "medium":
        medium_risks += 1
    else:
        high_risks += 1

if total_score is not 0:
    avg_score = round(total_score / valid_users)


print(f"\nUSERS\nTotal Users:{total_users}\nValid Users:{valid_users}\nInvalid Users: {invalid_users}\n")
print(f"RISKS\nLow Risks: {low_risks}\nMedium Risks: {medium_risks}\nHigh Risks: {high_risks}\n")
print(f"SCORES\nHighest Risk Score: {highest_score}\nAverage Risk Score: {avg_score}\n")
print(f"Highest Risk User:\nHighest Risk User: {highest_risk_user}\nRisk Score {highest_score}")