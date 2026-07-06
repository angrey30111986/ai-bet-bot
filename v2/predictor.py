import joblib
import pandas as pd

# Завантажуємо модель
model = joblib.load("football_ai.pkl")


def predict(
    home_elo,
    away_elo,
    home_rest,
    away_rest
):

    data = pd.DataFrame([{

        "home_elo": home_elo,
        "away_elo": away_elo,
        "elo_diff": home_elo - away_elo,

        "home_rest": home_rest,
        "away_rest": away_rest,
        "rest_diff": home_rest - away_rest

    }])

    probs = model.predict_proba(data)[0]

    return {

        "П1": round(probs[0] * 100, 2),
        "Х": round(probs[1] * 100, 2),
        "П2": round(probs[2] * 100, 2),

        "впевненість": round(max(probs) * 100, 2)

    }


if __name__ == "__main__":

    print(

        predict(

            1650,
            1580,

            7,
            4

        )

    )
