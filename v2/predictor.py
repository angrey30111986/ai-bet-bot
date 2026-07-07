import pandas as pd

from collector import collect_data
from model import load_model


def predict(home_team, away_team, fixture_id=None):

    model = load_model()

    if model is None:
        raise Exception("Model not trained")

    data = collect_data(home_team, away_team, fixture_id)

    X = pd.DataFrame([{
        "home_elo": data["home_elo"],
        "away_elo": data["away_elo"],
        "elo_diff": data["elo_diff"],
        "home_rest": data["home_rest_days"],
        "away_rest": data["away_rest_days"],
        "rest_diff": data["home_rest_days"] - data["away_rest_days"],
        "home_injuries": data["home_injuries"],
        "away_injuries": data["away_injuries"]
    }])

    proba = model.predict_proba(X)[0]

    return {
        "home": round(proba[2] * 100),
        "draw": round(proba[1] * 100),
        "away": round(proba[0] * 100)
    }
