import json
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



# Run validation loop
for user in users:
    try:
        validate_user_data(user)
        print(f"User ID {user['id']} ({user.get('username') or 'EMPTY'}): VALID")
    except ValueError as e:
        print(f"User ID {user['id']} ({user.get('username') or 'EMPTY'}): INVALID -> {e}")