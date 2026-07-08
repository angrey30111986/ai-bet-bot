import pandas as pd

from elo import process_match, reset
from fatigue import get_fatigue


def create_features(df):

    reset()

    rows = []

    for _, match in df.iterrows():

        home = str(match["home_team"])
        away = str(match["away_team"])

        result = int(match["result"])

        # Elo ДО початку матчу
        elo = process_match(home, away, result)

        fatigue = get_fatigue(
            home,
            away,
            match.to_dict()
        )

        rows.append({

            "home_elo": elo["home_elo"],
            "away_elo": elo["away_elo"],
            "elo_diff": elo["elo_diff"],

            "home_rest": fatigue["home_rest_days"],
            "away_rest": fatigue["away_rest_days"],
            "rest_diff": fatigue["home_rest_days"] - fatigue["away_rest_days"],

            "result": result

        })

    return pd.DataFrame(rows)
