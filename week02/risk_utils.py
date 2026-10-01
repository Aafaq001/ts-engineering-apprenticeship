def classify_risk(score: int) -> str:
    """Return the risk level for a given score."""
    if score <= 25:
        return "LOW"
    elif score <= 50:
        return "MEDIUM"
    elif score <= 75:
        return "HIGH"
    else:
        return "CRITICAL"

def calculate_risk(reports: int, warnings: int, bans: int) -> int:
    """Calculate and return a user's risk score."""
    score = reports + (warnings * 5) + (bans * 10)
    return score

