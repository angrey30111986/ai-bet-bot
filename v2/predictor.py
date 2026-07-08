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
        "rest_diff": (
            data["home_rest_days"]
            - data["away_rest_days"]
        )

    }])

    proba = model.predict_proba(X)[0]

    result = {
        "home": 0,
        "draw": 0,
        "away": 0
    }

    for cls, p in zip(model.classes_, proba):

        if cls == 0:
            result["home"] = round(p * 100)

        elif cls == 1:
            result["draw"] = round(p * 100)

        elif cls == 2:
            result["away"] = round(p * 100)

    return result
