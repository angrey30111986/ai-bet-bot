import joblib
import pandas as pd

# Завантаження моделі
model = joblib.load("football_ai.pkl")


def predict(features):
    """
    features = {
        "elo_diff": ...,
        "fatigue_diff": ...,
        "form_diff": ...,
        "home_advantage": ...,
        "goal_diff": ...
    }
    """

    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]

    return {
        "prediction": prediction,
        "home": round(probabilities[0] * 100, 1),
        "draw": round(probabilities[1] * 100, 1),
        "away": round(probabilities[2] * 100, 1)
    }
