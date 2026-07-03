import random

def analyze_match(home, away):
    confidence = random.randint(55, 90)

    if confidence >= 75:
        prediction = "П1"
        winner = home
    elif confidence >= 65:
        prediction = "X"
        winner = "Нічия"
    else:
        prediction = "П2"
        winner = away

    print(f"Аналіз матчу: {home} - {away}")

    return {
        "winner": winner,
        "confidence": confidence,
        "prediction": prediction
    }
