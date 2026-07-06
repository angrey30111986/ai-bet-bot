import joblib
import pandas as pd

model = joblib.load("football_ai.pkl")

def predict(features):

    df = pd.DataFrame([features])

    probability = model.predict_proba(df)[0]

    return {

        "П1": round(probability[1] * 100, 1),

        "Х": round(probability[0] * 100, 1),

        "П2": round(probability[2] * 100, 1)

    }
