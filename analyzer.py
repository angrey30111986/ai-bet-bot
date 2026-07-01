import random

def analyze_match(team1, team2):
    score = random.randint(50, 95)

    if score >= 80:
        recommendation = "Висока ймовірність"
    elif score >= 65:
        recommendation = "Середня ймовірність"
    else:
        recommendation = "Пропустити"

    return {
        "team1": team1,
        "team2": team2,
        "confidence": score,
        "recommendation": recommendation
    }
