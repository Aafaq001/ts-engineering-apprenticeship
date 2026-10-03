def classify_risk(score: int) -> str:
    """Return the risk level for a given score."""
    if score >= 50:
        level = "high"
    elif score >= 25:
        level = "medium"
    else:
        level = "low"
    return level

def calculate_risk(reports: int, warnings: int, bans: int) -> int:
    """Calculate and return a user's risk score."""
    score = reports + (warnings * 5) + (bans * 10)
    return score

