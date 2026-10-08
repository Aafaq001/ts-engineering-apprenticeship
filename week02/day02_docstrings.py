def validate_user_data(user):
    """
    Check if a user's data contains all required keys and is valid.
    
    Args:
        user (dict): The user data dictionary containing profile details.
        
    Returns:
        True if the user data is valid, ValueError otherwise.   
    """

def calculate_risk(reports, warnings, bans):
    """
    Calculate a user's risk score.

    Args:
        reports: Number of reports.
        warnings: Number of warnings.
        bans: Number of bans.

    Returns:
        The calculated risk score.
    """

def classify_risk(score):
    """
    Classify score into risk level

    Args:
        if score >= 50 risk level is high 
        else if score is between 25 to 49 risk level is medium
        else risk level is low

    Returns:
        Risk Level, Low, Medium, High
    """

def generate_risk_message(name, score, level):
    """
    generate message against each user
    
    Args:
        name: Username.
        score: score calculated from calculate_risk(reports, warnings, bans).
        level: Risk level calculated from classify_risk(score).
    
    Returns:
        Returns message with username score and risk level.
    """