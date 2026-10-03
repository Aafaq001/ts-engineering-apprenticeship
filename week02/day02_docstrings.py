def validate_user_data(user):
    """
    check if user's data is valid or not across all users 
    
    Returns:
        True if data is valid else False    
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
        score: Get against each user from calculate_risk(reports, warnings, bans)

    Returns:
        Risk Level, Low, Medium, High or Critical
    """

def generate_risk_message(name, score, level):
    """
    generate message against each user
    
    Args:
        name: Username.
        Score: Score calculated from calculate_risk(reports, warnings, bans).
        level: Risk level calculated from classify_risk(score).
    
    Returns:
        Returns message with username score and risk level.
    """