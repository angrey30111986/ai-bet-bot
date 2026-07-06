import joblib

model = joblib.load("football_ai.pkl")

def predict(features):
    probs = model.predict_proba([features])[0]

    return {
        "home": round(probs[0] * 100, 1),
        "draw": round(probs[1] * 100, 1),
        "away": round(probs[2] * 100, 1)
    }
