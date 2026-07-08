import pandas as pd

from elo import get_elo
from fatigue import get_fatigue


def create_features(df):

    rows = []

    for _, match in df.iterrows():

        home = str(match["home_team"])
        away = str(match["away_team"])

        elo = get_elo(home, away)
        fatigue = get_fatigue(home, away)

        rows.append({

            # Elo
            "home_elo": elo["home_elo"],
            "away_elo": elo["away_elo"],
            "elo_diff": elo["elo_diff"],

            # Відпочинок
            "home_rest": fatigue["home_rest_days"],
            "away_rest": fatigue["away_rest_days"],
            "rest_diff": (
                fatigue["home_rest_days"]
                - fatigue["away_rest_days"]
            ),

            # Результат (ціль)
            "result": int(match["result"])

        })

    return pd.DataFrame(rows)
